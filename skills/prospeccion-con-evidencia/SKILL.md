---
name: prospeccion-con-evidencia
description: "Orquesta una auditoria web publica y la preparacion comercial posterior, conservando la frontera entre hechos, hipotesis y datos del negocio. Usar cuando el usuario quiera revisar un prospecto de punta a punta: auditar su sitio, decidir si existe una razon honesta para conversar y preparar preguntas de descubrimiento. No usar para contactar al prospecto, publicar resultados ni saltar directamente a una oferta o precio."
---

# Prospeccion con evidencia

Coordina dos capacidades especializadas sin mezclar sus criterios. La auditoria cierra primero; la preparacion comercial consume despues un handoff estable.

## Fuentes de verdad

1. Lee `../auditoria-web-prospectos/SKILL.md` antes de investigar el sitio y sigue sus limites, clasificacion y entregables.
2. Usa `../shared/auditoria-a-venta.md` para producir y comprobar `handoff-comercial.md`.
3. Lee `../venta-con-criterio/SKILL.md` solo despues de cerrar la auditoria. Carga sus referencias segun la etapa comercial solicitada.

Las skills especializadas mandan sobre sus respectivas etapas. Esta skill decide el orden y los criterios de paso, no duplica sus reglas.

## Flujo

### 1. Definir el resultado de la ejecucion

Con una URL publica alcanza para iniciar. Identifica el prospecto, la fecha y si el usuario pide:

- solo auditoria;
- auditoria y preparacion de preguntas;
- o una etapa comercial posterior respaldada por respuestas internas ya disponibles.

Una solicitud de punta a punta incluye por defecto auditoria y preparacion de preguntas. No incluye contacto, publicacion, propuesta ni precio.

### 2. Cerrar la auditoria

Ejecuta `auditoria-web-prospectos` hasta que existan, como minimo:

- `informe.md`;
- `rutas.csv`;
- `pruebas-navegador.md`;
- `handoff-comercial.md`.

Guarda la ejecucion bajo `auditorias/<prospecto>/<AAAA-MM-DD>/`. Trata esa carpeta como salida local privada: no la copies a `examples/`, no la publiques y no la agregues a Git sin autorizacion explicita posterior del usuario para ese caso.

La etapa esta cerrada cuando cada hallazgo transferido tiene evidencia, consecuencia observable, estado y control probable; tambien puede cerrar con un veredicto de que no existe una oportunidad suficiente.

### 3. Aplicar la puerta comercial

Lee el veredicto del handoff:

- Si no hay razon suficiente para conversar, registra el descarte y termina. No fabriques preguntas ni una oferta.
- Si la evidencia justifica validar una incertidumbre, continua a preparacion comercial.
- Si hacen falta permisos o accesos para confirmar el propio hallazgo, formula ese paso antes de dimensionar valor.

### 4. Preparar la conversacion

Aplica `venta-con-criterio` usando `handoff-comercial.md` como entrada. Crea `preparacion-conversacion.md` en la misma carpeta con:

1. razon para conversar;
2. una incertidumbre principal;
3. mapa de evidencia, hipotesis y datos faltantes;
4. entre tres y ocho preguntas priorizadas;
5. decision que habilita cada respuesta;
6. limites y siguiente paso minimo.

Conserva todas las etiquetas epistemicas. La etapa termina antes de oferta o precio salvo que el usuario haya pedido expresamente avanzar y haya aportado datos suficientes del negocio.

### 5. Entregar

Resume:

- veredicto de la auditoria;
- evidencia de entrada;
- objetivo de la conversacion;
- preguntas prioritarias;
- afirmaciones que siguen sin demostrarse;
- enlaces a los artefactos locales.

La ejecucion termina sin contactar al prospecto ni publicar los resultados.
