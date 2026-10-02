# Panicafe - handoff comercial

Fecha: 2 de octubre de 2026. Fuente: [informe.md](informe.md).

## Veredicto de entrada

Hay una razon concreta para abrir una conversacion breve: dos productos de la carta saludable tienen descripciones incompatibles con la carta digital vigente. La auditoria tambien confirma una variante `www` sin resolucion y un handoff de carta que siempre presenta Cerro de las Rosas.

La evidencia justifica validar una correccion puntual y el proceso que mantiene alineados esos canales. No demuestra demanda para un rediseño, una automatizacion, mantenimiento recurrente ni una perdida economica.

## Evidencia transferible

### P01 - La carta saludable publica ingredientes de otros productos

- Estado: confirmado.
- Evidencia: [informe.md, P01](informe.md#p01---la-carta-saludable-publica-ingredientes-de-otros-productos) y [pruebas-navegador.md](pruebas-navegador.md).
- Consecuencia observable: Ensalada Panicafe y Baguettin de guacamole se presentan con ingredientes distintos de la carta Butter enlazada por la misma landing.
- Control probable: contenido propio y proceso editorial del negocio o su proveedor de diseno.
- Intervencion minima plausible: corregir el PDF y revisar los cinco platos contra una fuente aprobada.
- Lo que todavia no sabemos: recetas vigentes, alcance por sucursal, quien aprueba la informacion y si hubo consultas o reclamos.

### P02 - `www.panicafe.com` no resuelve

- Estado: confirmado.
- Evidencia: [informe.md, P02](informe.md#p02---wwwpanicafecom-no-resuelve), [rutas.csv](rutas.csv) y [pruebas-navegador.md](pruebas-navegador.md).
- Consecuencia observable: quien ingresa mediante esa variante no llega al sitio.
- Control probable: DNS y configuracion de CloudFront/certificado.
- Intervencion minima plausible: crear el alias y redirigirlo al dominio apex.
- Lo que todavia no sabemos: si la variante aparece en materiales, enlaces antiguos o campanas y quien administra el dominio.

### P03 - Las cartas llevan siempre a una sola sucursal

- Estado: recorrido confirmado; impacto pendiente.
- Evidencia: [informe.md, P03](informe.md#p03---las-cartas-llevan-siempre-a-una-sola-sucursal) y [pruebas-navegador.md](pruebas-navegador.md).
- Consecuencia observable: las tres CTA abren una carta identificada como Cerro de las Rosas aunque la landing presenta siete sucursales.
- Control probable: destino configurado en la landing y capacidades o configuracion de Butter.
- Intervencion minima plausible: primero confirmar la regla real; cambiar el recorrido solo si las cartas difieren o el contexto actual confunde.
- Lo que todavia no sabemos: si las sucursales comparten carta, precios y disponibilidad.

## Hipotesis comerciales por validar

| ID | Hipotesis | Evidencia que la origina | Dato que la validaria o descartaria |
| --- | --- | --- | --- |
| H-01 | Existe una falla en el proceso de revision entre PDF y carta vigente | Dos platos del PDF repiten una descripcion que corresponde a un tercero | Quien mantiene cada canal, fuente aprobada y frecuencia de cambios |
| H-02 | La variante `www` produce visitas fallidas reales | El host no resuelve | Presencia de `www` en materiales, perfiles, enlaces o analitica |
| H-03 | El handoff a Cerro puede dar contexto incorrecto a otras sucursales | Todas las CTA llegan al mismo local | Diferencias reales de carta, precios o disponibilidad entre sucursales |
| H-04 | Una revision editorial periodica podria tener valor | P01 muestra una inconsistencia entre canales | Frecuencia de cambios, cantidad de piezas y recurrencia de errores |

## Preguntas priorizadas

| Orden | Pregunta | Proposito | Decision que habilita | Evidencia relacionada |
| --- | --- | --- | --- | --- |
| 1 | ¿Quien actualiza y aprueba hoy la carta de Butter, el PDF saludable y la landing? | Entender el proceso y la atribucion de control | Saber con quien validar y si la correccion depende del negocio o de proveedores | P01, P02, P03 |
| 2 | ¿Las descripciones actuales de Butter son la fuente aprobada para Ensalada Panicafe y Baguettin de guacamole? | Confirmar la referencia vigente | Corregir P01 o descartar la comparacion si la fuente correcta es otra | P01 |
| 3 | ¿Las siete sucursales comparten carta, precios y disponibilidad? | Validar el impacto del contexto Cerro de las Rosas | Corregir el recorrido, aclararlo o dejarlo sin cambios | P03 |
| 4 | ¿Con que frecuencia cambian ingredientes, promociones o piezas como este PDF? | Dimensionar recurrencia | Distinguir correccion puntual de un problema editorial repetido | P01, H-04 |
| 5 | ¿Usan `www.panicafe.com` en impresos, perfiles, campanas o enlaces antiguos? | Estimar exposicion real | Priorizar el alias DNS o tratarlo como higiene tecnica menor | P02 |
| 6 | ¿Reciben consultas o reclamos por diferencias de carta, horarios o sucursal? | Buscar consecuencia operativa observable | Decidir si vale investigar un flujo mas amplio entre canales | P01, P03 |

## Limites para la conversacion

- No demostrado: trafico afectado, reclamos, ventas perdidas, costo operativo, diferencias entre sucursales o recurrencia de los errores.
- No justifica todavia: rediseño, ecommerce, reemplazo de Butter, automatizacion grande, mensualidad o promesa de mayor facturacion.
- Permisos o accesos necesarios: confirmacion de recetas; responsables internos; acceso a DNS, landing y fuentes solo si se acuerda corregir.
- Senal para descartar la oportunidad: la carta Butter no es la fuente vigente, las sucursales comparten contexto sin confusion y el negocio ya tiene responsables corrigiendo PDF y DNS.

## Siguiente paso minimo

Validar con una persona responsable las recetas vigentes, el alcance de la carta por sucursal y quien controla cada superficie. Con esas respuestas se decide entre descartar, cotizar una correccion puntual o investigar un proceso editorial recurrente.
