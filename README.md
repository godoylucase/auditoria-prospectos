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

Cadena completa:

- Codex: `Usa $prospeccion-con-evidencia para auditar https://ejemplo.com y preparar las preguntas comerciales.`
- Claude Code: `/prospeccion-con-evidencia https://ejemplo.com`
- OpenCode: `Usa la skill prospeccion-con-evidencia para auditar https://ejemplo.com y preparar las preguntas comerciales.`

Ejecucion en dos etapas, recomendada cuando queres revisar la evidencia antes de preparar la conversacion:

1. Invoca `auditoria-web-prospectos` con la URL y detenete al generar `handoff-comercial.md`.
2. Revisa el informe e invoca `venta-con-criterio` con la ruta al handoff.

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
