# Plantilla del informe

```markdown
# [Prospecto] - auditoria publica para prospeccion

Fecha: [fecha]. Sitio: [URL]. Revision externa, [sin/con] acceso autenticado.

## Evaluacion comercial

[Conclusion: tipo y tamano probable de oportunidad. Separar evidencia tecnica de demanda comercial.]

## Negocio y recorridos evaluados

- Conversion principal: [...]
- Conversiones secundarias: [...]
- Plataforma e integraciones observadas: [...]
- Recorridos elegidos: [...]
- Documentos y handoffs externos: [...]

## Cobertura y limites

[Rutas descubiertas, revisadas, muestras interactivas, viewport, fecha y exclusiones.]

### Artefactos de evidencia

- `rutas.csv`: [...]
- `pruebas-navegador.md`: [...]
- `handoff-comercial.md`: [...]
- [otros]: [...]

## Hallazgos priorizados

### [ID] - [Titulo]

**Prioridad [alta/media/baja] - [confirmado/inferido/hipotesis/pendiente].**

- Pagina o recorrido: [...]
- Reproduccion: [...]
- Esperado: [...]
- Obtenido: [...]
- Consecuencia observable: [...]
- Impacto comercial posible: [hipotesis explicita]
- Control probable: [negocio / tema o app / plataforma / desconocido]
- Oportunidad minima: [...]
- Criterio de cierre: [...]
- Pendientes: [...]

## Seguridad: resultado y alcance

[Que se observo pasivamente, que no se probo y por que no equivale a un pentest.]

## Funciones o mejoras que conviene validar

- [Hipotesis] - [dato o conversacion necesarios para validarla]

## Observaciones descartadas

- [Candidato] - [evidencia que impidio declararlo hallazgo]

## Como usar estos resultados para prospectar

- Punto de entrada 1: [...]
- Punto de entrada 2: [...]
- Intervencion inicial razonable: [...]
- Lo que la evidencia todavia no justifica: [...]
- Preguntas antes de cotizar: [...]
- Medida de resultado y linea de base requerida: [...]

## Proxima prueba

[Siguiente paso mas pequeno, reversible y autorizado.]
```

Despues de completar el informe, crea `handoff-comercial.md` con el contrato compartido `../../shared/auditoria-a-venta.md`. No copies en el handoff todo el informe: conserva solo la evidencia necesaria para decidir y preparar la proxima conversacion.

## Columnas minimas de rutas.csv

```text
url,http_status,final_url,page_type,surface_owner,title,h1_count,description_present,canonical,sources,checked_at,notes
```

## Estructura minima de pruebas-navegador.md

Inclui fecha, entorno, viewport y una tabla con:

```text
prueba | resultado observado | evidencia y alcance | estado
```

Usa `estado` para `confirmado`, `pendiente` o `descartado`. Omiti credenciales, tokens, datos personales y URLs de sesion.
