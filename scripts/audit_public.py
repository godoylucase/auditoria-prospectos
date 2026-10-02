"""Low-rate GET-only inventory of public Voltra HTML. No auth or form submission."""
import collections
import csv
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

BASE = "https://voltra.com.ar"
OUT = pathlib.Path(__file__).resolve().parents[1] / "auditorias/voltra/2026-10-02"
OUT.mkdir(parents=True, exist_ok=True)


def get(url):
    time.sleep(0.65)
    result = subprocess.run([
        "curl", "--silent", "--show-error", "--location", "--max-time", "30",
        "--max-redirs", "5", "--user-agent", "PublicWebsiteReview/1.0",
        "--write-out", "\n__AUDIT_META__%{http_code}|%{url_effective}|%{time_total}|%{size_download}",
        url,
    ], capture_output=True, text=True)
    body, _, meta = result.stdout.rpartition("\n__AUDIT_META__")
    parts = meta.split("|")
    return body, {"status": int(parts[0] or 0) if parts else 0,
                  "final_url": parts[1] if len(parts) > 1 else url,
                  "seconds": parts[2] if len(parts) > 2 else "",
                  "bytes": parts[3] if len(parts) > 3 else "",
                  "error": result.stderr.strip()}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.links = []
        self.text = []
        self.main = []
        self.headings = []
        self.images = []
        self.meta = {}
        self.forms = []
        self.jsonld = []
        self.title = ""
        self.lang = ""
        self.canonical = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang", "")
        if tag == "meta": self.meta[a.get("name", a.get("property", ""))] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href", "")
        if tag == "img": self.images.append({k: a.get(k) for k in ("src", "alt", "loading", "width", "height")})
        if tag == "form": self.forms.append({k: a.get(k) for k in ("action", "method", "id")})
        item = {"tag": tag, "attrs": a, "text": []}
        if tag not in ("area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"):
            self.stack.append(item)

    def handle_data(self, data):
        for item in self.stack:
            if item["tag"] in ("a", "title", "h1", "h2", "h3", "script"): item["text"].append(data)
        if any(i["tag"] in ("script", "style", "noscript") for i in self.stack): return
        clean = " ".join(data.split())
        if clean:
            self.text.append(clean)
            if any(i["tag"] == "main" for i in self.stack): self.main.append(clean)

    def handle_endtag(self, tag):
        positions = [n for n, i in enumerate(self.stack) if i["tag"] == tag]
        if not positions: return
        n = positions[-1]
        item = self.stack[n]
        text = " ".join("".join(item["text"]).split())
        if tag == "a": self.links.append({"href": item["attrs"].get("href", ""), "text": text})
        if tag == "title": self.title = text
        if tag in ("h1", "h2", "h3"): self.headings.append({"level": tag, "text": text})
        if tag == "script" and item["attrs"].get("type") == "application/ld+json":
            try: self.jsonld.append(json.loads("".join(item["text"])))
            except ValueError: self.jsonld.append({"invalid_json": True})
        self.stack = self.stack[:n]


def normalize(href, source=BASE):
    p = urllib.parse.urlsplit(urllib.parse.urljoin(source, href))
    if p.hostname != "voltra.com.ar": return None
    path = p.path.rstrip("/") or "/"
    if path != "/" and not path.startswith(("/products/", "/collections", "/pages/", "/policies/", "/blogs/")): return None
    if path.endswith((".atom", ".json", ".xml")): return None
    # Collapse product aliases to the canonical product path; retain real pagination.
    if "/products/" in path: path = "/products/" + path.split("/products/", 1)[1]
    q = urllib.parse.parse_qs(p.query)
    query = "?page=" + q["page"][0] if "page" in q and q["page"][0].isdigit() else ""
    return BASE + path + query


sitemap_body, sitemap_meta = get(BASE + "/sitemap.xml")
root = ET.fromstring(sitemap_body)
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
maps = [loc.text for loc in root.findall("s:sitemap/s:loc", ns)]
origins = collections.defaultdict(set)
sitemaps = []
for sm in maps:
    if "agentic" in sm: continue
    body, meta = get(sm)
    tree = ET.fromstring(body)
    urls = [loc.text for loc in tree.findall("s:url/s:loc", ns)]
    sitemaps.append({"url": sm, "meta": meta, "urls": urls})
    for url in urls:
        n = normalize(url)
        if n: origins[n].add(sm)
origins[BASE + "/"].add("seed")
(OUT / "sitemaps.json").write_text(json.dumps(sitemaps, ensure_ascii=False, indent=2))
print("Sitemap routes:", len(origins), flush=True)
queue = collections.deque(origins)
seen = set()
records = []
with (OUT / "pages.jsonl").open("w") as evidence:
    while queue and len(seen) < 250:
        url = queue.popleft()
        if url in seen: continue
        seen.add(url)
        body, meta = get(url)
        p = Page()
        p.feed(body)
        record = {"url": url, **meta, "title": p.title, "canonical": p.canonical,
                  "lang": p.lang, "description": p.meta.get("description", ""),
                  "robots": p.meta.get("robots", ""), "headings": p.headings,
                  "main_text": "\n".join(p.main), "all_text": "\n".join(p.text),
                  "links": p.links, "forms": p.forms, "images": p.images,
                  "jsonld": p.jsonld, "sha256": hashlib.sha256(body.encode()).hexdigest(),
                  "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        evidence.write(json.dumps(record, ensure_ascii=False) + "\n")
        evidence.flush()
        records.append(record)
        for link in p.links:
            n = normalize(link["href"], url)
            if n:
                origins[n].add(url)
                if n not in seen and n not in queue: queue.append(n)
        print(f"{len(seen):3} {meta['status']} {url} ({len(queue)} pending)", flush=True)

with (OUT / "rutas.csv").open("w") as f:
    writer = csv.writer(f)
    writer.writerow(["url", "http_status", "final_url", "title", "h1_count", "description_present", "bytes", "seconds_single_request", "sources"])
    for p in records:
        writer.writerow([p["url"], p["status"], p["final_url"], p["title"], sum(h["level"] == "h1" for h in p["headings"]), bool(p["description"]), p["bytes"], p["seconds"], " | ".join(sorted(origins[p["url"]]))])
summary = {"checked": len(records), "pending": list(queue), "statuses": dict(collections.Counter(p["status"] for p in records)), "sitemap_urls": sum(len(s["urls"]) for s in sitemaps)}
(OUT / "crawl-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
print(json.dumps(summary, ensure_ascii=False), flush=True)
