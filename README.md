# Auditoria de prospectos

Skills portables para auditar sitios publicos con evidencia y transformar los hallazgos en preguntas comerciales sin inventar impacto. El mismo contenido se puede instalar en Codex, Claude Code y OpenCode.

## Cadena

1. `auditoria-web-prospectos` recorre la superficie publica, reproduce hallazgos y cierra el informe.
2. `handoff-comercial.md` conserva hechos, hipotesis, vacios y preguntas.
3. `venta-con-criterio` prepara descubrimiento y solo avanza a oferta o precio cuando existen datos suficientes.
4. `prospeccion-con-evidencia` orquesta las dos etapas anteriores cuando se necesita el recorrido completo.

La auditoria no autoriza contacto, publicacion, pruebas activas de seguridad ni acciones irreversibles sobre sistemas del prospecto.

## Instalar

Requiere Python 3.10 o posterior. La fuente canonica vive en `skills/`; el instalador copia el conjunto completo para conservar el contrato compartido.

### En el usuario

```bash
python3 scripts/manage_skills.py install codex --scope user
python3 scripts/manage_skills.py install claude --scope user
python3 scripts/manage_skills.py install opencode --scope user
```

Para los tres:

```bash
python3 scripts/manage_skills.py install all --scope user
```

Los destinos son:

| Plataforma | Usuario | Proyecto |
| --- | --- | --- |
| Codex | `~/.codex/skills/` | `.codex/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` |

### En otro proyecto

```bash
python3 scripts/manage_skills.py install all --scope project --target /ruta/al/proyecto
```

El instalador no reemplaza una instalacion distinta por defecto. Usa `--force` solo despues de revisar el destino; antes de reemplazar crea un respaldo junto a la skill existente. `--dry-run` muestra las operaciones sin escribir.

## Empaquetar

Genera un ZIP por plataforma, listo para extraer en la raiz de un proyecto:

```bash
python3 scripts/manage_skills.py package all --output dist
```

Los archivos resultantes contienen respectivamente `.codex/skills/`, `.claude/skills/` y `.opencode/skills/`. `dist/` es generado y no se versiona.

## Ejecutar

### Que skill usar

| Necesidad | Skill | Resultado esperado |
| --- | --- | --- |
| Auditar un sitio y revisar la evidencia antes de hablar de venta | `auditoria-web-prospectos` | Informe de auditoria y `handoff-comercial.md` |
| Preparar una conversacion a partir de una auditoria existente | `venta-con-criterio` | Diagnostico comercial y preguntas; oferta o precio solo si hay evidencia suficiente |
| Ejecutar todo el recorrido | `prospeccion-con-evidencia` | Auditoria, handoff y preparacion comercial |

La cadena completa es:

```text
auditoria-web-prospectos -> handoff-comercial.md -> venta-con-criterio
              \____________ prospeccion-con-evidencia ____________/
```

La ejecucion en dos etapas es la recomendada para las primeras pruebas: permite revisar los hechos y las hipotesis del handoff antes de preparar la conversacion. Ninguna invocacion autoriza contactar al prospecto.

### Codex

Usa `$nombre-de-la-skill` para seleccionarla de forma explicita:

```text
$auditoria-web-prospectos Audita https://ejemplo.com y detenete al generar handoff-comercial.md.

$venta-con-criterio Usa auditorias/ejemplo/AAAA-MM-DD/handoff-comercial.md para preparar las preguntas de descubrimiento. No armes oferta ni precio.

$prospeccion-con-evidencia Audita https://ejemplo.com y prepara la conversacion comercial. No contactes al prospecto.
```

Tambien podes abrir `/skills` para comprobar que las tres skills esten disponibles.

### Claude Code

Invoca cada skill como comando slash y agrega las instrucciones despues del argumento:

```text
/auditoria-web-prospectos https://ejemplo.com y detenete al generar handoff-comercial.md

/venta-con-criterio auditorias/ejemplo/AAAA-MM-DD/handoff-comercial.md prepara las preguntas de descubrimiento; no armes oferta ni precio

/prospeccion-con-evidencia https://ejemplo.com prepara la conversacion comercial sin contactar al prospecto
```

### OpenCode

La forma compatible entre versiones es pedir la skill por nombre:

```text
Usa la skill auditoria-web-prospectos para auditar https://ejemplo.com y detenete al generar handoff-comercial.md.

Usa la skill venta-con-criterio con auditorias/ejemplo/AAAA-MM-DD/handoff-comercial.md para preparar las preguntas de descubrimiento. No armes oferta ni precio.

Usa la skill prospeccion-con-evidencia para auditar https://ejemplo.com y preparar la conversacion comercial. No contactes al prospecto.
```

En versiones que exponen las skills como comandos slash, tambien podes usar `/auditoria-web-prospectos`, `/venta-con-criterio` y `/prospeccion-con-evidencia`.

Reemplaza `https://ejemplo.com` por el sitio del prospecto y la ruta de ejemplo por el `handoff-comercial.md` generado. Si instalaste las skills durante una sesion abierta y no aparecen, inicia una sesion nueva.

Cada plataforma puede seleccionar una skill automaticamente a partir de su descripcion, pero la invocacion explicita reduce ambiguedad durante las primeras pruebas.

Las rutas de instalacion siguen la documentacion de [Codex](https://developers.openai.com/blog/eval-skills), [Claude Code](https://code.claude.com/docs/en/skills) y [OpenCode](https://opencode.ai/docs/skills).

## Datos y ejemplos

`auditorias/` contiene resultados privados de ejecucion y esta ignorado por Git. Una auditoria nunca se copia, mueve ni adapta a `examples/` de manera automatica.

Un caso puede entrar en `examples/` **si y solo si Lucas lo autoriza explicitamente despues de esa ejecucion**. Esa autorizacion debe identificar el caso que puede publicarse; antes de versionarlo se revisan datos personales, credenciales, tokens, URLs de sesion y cualquier detalle que no sea necesario para enseñar el flujo.

## Desarrollo

```bash
python3 scripts/manage_skills.py verify
python3 -m unittest discover -s tests -v
python3 /ruta/a/skill-creator/scripts/quick_validate.py skills/auditoria-web-prospectos
python3 /ruta/a/skill-creator/scripts/quick_validate.py skills/venta-con-criterio
python3 /ruta/a/skill-creator/scripts/quick_validate.py skills/prospeccion-con-evidencia
```

La copia fuente original de `venta-con-criterio` no se modifica desde este repositorio.
