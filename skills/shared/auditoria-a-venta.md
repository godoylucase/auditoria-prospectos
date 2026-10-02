# Contrato de auditoria a conversacion comercial

Este contrato conecta una auditoria externa con una conversacion comercial sin convertir evidencia tecnica en demanda, impacto economico ni autorizacion para vender.

## Artefacto

La auditoria produce `handoff-comercial.md` despues de cerrar `informe.md`, `rutas.csv` y `pruebas-navegador.md`.

El handoff debe poder leerse sin volver a recorrer todo el sitio. Cada afirmacion conserva su estado epistemico y enlaza la evidencia que la sostiene.

## Estructura

```markdown
# [Prospecto] - handoff comercial

Fecha: [fecha]. Fuente: [ruta relativa a informe.md].

## Veredicto de entrada

[Hay/no hay una razon suficiente para conversar. Indicar alcance probable sin afirmar demanda, presupuesto ni perdida economica.]

## Evidencia transferible

### [ID] - [Hallazgo]

- Estado: [confirmado / inferido / hipotesis / pendiente / descartado]
- Evidencia: [ruta y ancla, URL o prueba reproducible]
- Consecuencia observable: [...]
- Control probable: [negocio / tema o app / plataforma / tercero / desconocido]
- Intervencion minima plausible: [...]
- Lo que todavia no sabemos: [...]

## Hipotesis comerciales por validar

| ID | Hipotesis | Evidencia que la origina | Dato que la validaria o descartaria |
| --- | --- | --- | --- |
| H-01 | [...] | [...] | [...] |

## Preguntas priorizadas

| Orden | Pregunta | Proposito | Decision que habilita | Evidencia relacionada |
| --- | --- | --- | --- | --- |
| 1 | [...] | [...] | [...] | [...] |

## Limites para la conversacion

- No demostrado: [...]
- No justifica todavia: [...]
- Permisos o accesos necesarios: [...]
- Senal para descartar la oportunidad: [...]

## Siguiente paso minimo

[Una sola accion reversible: validar una hipotesis, pedir un dato o acordar una revision interna.]
```

## Reglas de transferencia

- Conserva las etiquetas de evidencia; una hipotesis nunca asciende a hecho por aparecer en el handoff.
- Formula una pregunta solo si su respuesta cambia una decision: descartar, investigar, dimensionar, ofrecer o postergar.
- Separa consecuencia observable de impacto economico posible.
- No completes volumen, frecuencia, conversion, ahorro, urgencia, presupuesto ni autoridad de compra cuando faltan.
- Manten la atribucion de control. Un problema de un tercero puede requerir coordinacion y no desarrollo propio.
- Prefiere entre tres y ocho preguntas priorizadas. Evita convertir la conversacion en un interrogatorio exhaustivo.
- Si la evidencia no justifica una conversacion, decláralo en el veredicto y no fabriques preguntas para forzarla.
- El handoff no autoriza contacto, propuesta, cotizacion ni seguimiento. Es una entrada para decidir el siguiente paso con el usuario.

## Criterio de completitud

El handoff esta listo cuando otra persona puede distinguir, sin releer toda la auditoria:

1. que se comprobo;
2. que solo se sospecha;
3. que vale la pena preguntar;
4. que decision habilita cada respuesta;
5. que todavia no corresponde vender.
