---
name: auditoria-web-prospectos
description: Audita de forma externa y basada en evidencia el sitio publico de un negocio para detectar bugs reproducibles, fricciones de conversion, contradicciones, enlaces o recorridos rotos y oportunidades de mejora que puedan abrir una conversacion comercial honesta. Usar cuando el usuario quiera revisar una web, tienda, landing, SaaS, sitio de servicios o portal para prospectar clientes, recorrer su arbol de rutas, probar un flujo de compra o registro sin completarlo, o evaluar si hay trabajo tecnico vendible. No usar como sustituto de un pentest autorizado ni para explotar vulnerabilidades.
---

# Auditoria web para prospectar

## Objetivo

Converti una revision externa de un sitio en evidencia util para decidir si existe una oportunidad comercial real. Busca el problema mas pequeno que sea importante, reproducible y razonablemente controlable por el prospecto. No infles un conjunto de detalles menores hasta convertirlo en un proyecto grande.

La auditoria descubre indicios y oportunidades; no demuestra por si sola demanda, presupuesto, ventas perdidas ni voluntad de contratar.

## Entradas

Necesitas una URL publica. Aprovecha, si estan disponibles:

- nombre del negocio;
- tipo de negocio y conversion principal esperada;
- pais o mercado, cuando afecte moneda, entrega o condiciones;
- credenciales o cuenta que el usuario decida operar personalmente;
- alcance y autorizacion escrita para cualquier prueba activa de seguridad.

Si solo recibis la URL, empeza por la etapa publica y declara las inferencias. No detengas la auditoria para pedir datos que puedan descubrirse de forma segura.

## Limites de actuacion

Trabaja primero como visitante normal y con bajo impacto:

- Consulta contenido publico y respeta las instrucciones publicas relevantes del sitio.
- Usa una tasa baja, una solicitud a la vez y un limite explicito de rutas. Detente ante `429`, inestabilidad o senales de carga.
- No enumeres rutas privadas, fuerces parametros, evadas autenticacion, adivines credenciales, pruebes inyecciones, manipules importes ni busques datos de terceros.
- No envies formularios, mensajes, newsletters, reservas, pedidos o pagos sin autorizacion especifica en el momento de la accion.
- Podes agregar un elemento al carrito o avanzar por un flujo reversible si no crea una orden ni comunica con el negocio. Retira al terminar cualquier estado de prueba creado por vos.
- Para una cuenta, OTP, CAPTCHA o dato personal, deja que el usuario tome control. Nunca guardes contrasenas, codigos, tokens ni URLs de sesion en el informe.
- La seguridad es pasiva por defecto. Encabezados, HTTPS o errores visibles son indicadores; solo llama vulnerabilidad a una falla confirmada dentro de un alcance autorizado.

Si el usuario pide pruebas activas, confirma primero titularidad o autorizacion, dominios, tecnicas permitidas, ventana, limites de tasa y contacto de emergencia. Sin eso, ofrece una revision pasiva.

## Flujo de trabajo

### 1. Entender el negocio y sus recorridos

Identifica:

- que vende o que accion busca del visitante;
- conversion principal y conversiones secundarias;
- plataforma visible, integraciones y terceros;
- caminos de mayor valor o riesgo.

Adapta el recorrido al sitio:

- **Ecommerce:** portada, categoria, busqueda, producto, variantes, stock, carrito, envio, descuentos y comienzo del checkout.
- **SaaS:** propuesta, pricing, documentacion, registro, recuperacion de acceso y comienzo de onboarding.
- **Servicios:** oferta, casos, contacto, agenda, ubicacion y solicitud de presupuesto.
- **Contenido o membresia:** navegacion, busqueda, articulo, suscripcion y comienzo del acceso restringido.

No fuerces un checklist de ecommerce sobre un negocio distinto.

### 2. Inventariar la superficie publica

Descubre rutas desde la portada, `robots.txt`, sitemaps y enlaces internos. Normaliza fragmentos, tracking, filtros, ordenamientos, alias y paginacion para no crear combinaciones infinitas.

Si no hay sitemap o el sitio es una sola pagina, no lo trates como bloqueo ni inventes profundidad. Inventaria las secciones con ancla, los documentos enlazados y los handoffs que sostienen el recorrido —por ejemplo carta digital, agenda, mapas, WhatsApp o portal de pagos—. Revisa solo la pagina de destino necesaria para confirmar el contexto; no expandas el rastreo al dominio completo del proveedor.

Comprueba de forma pasiva el salto de HTTP a HTTPS y la variante habitual `www`/apex cuando corresponda. Una variante sin resolver es un hallazgo de configuracion, no una vulnerabilidad.

Registra por ruta, cuando sea posible:

- URL solicitada, estado HTTP y URL final;
- titulo, canonical, descripcion y cantidad de H1;
- fuentes internas que enlazan la ruta;
- tipo de pagina y fecha/hora de observacion.

Registra tambien quien controla cada superficie: prospecto, documento propio, integracion o tercero.

Distingue cobertura real de exhaustividad. Deci "todas las rutas publicas descubiertas" y no "todo el sitio" salvo que puedas demostrarlo.

### 3. Buscar senales y contradicciones

Usa el inventario para encontrar candidatos, no para declarar fallas automaticamente:

- 4xx/5xx, bucles y redirecciones a destinos semanticamente incorrectos;
- CTA o promociones que llevan a otro producto o recorrido;
- contenido vacio, controles sin respuesta y errores JavaScript visibles;
- condiciones contradictorias de precio, envio, devolucion, horarios o disponibilidad;
- campanas vencidas, paginas huerfanas, colecciones vacias y metadatos ausentes;
- formularios, buscadores, filtros, menu y estados de error confusos;
- indicadores pasivos de seguridad o privacidad que merezcan una revision autorizada.

Compara las fuentes que el visitante entiende como una sola experiencia: landing, carta o catalogo externo, PDF, ubicaciones y condiciones. Los documentos enlazados desde un CTA principal pueden contener el hallazgo mas importante aunque no sean HTML.

El HTML puede contener texto oculto, plantillas y estados que no se muestran. Confirma visualmente todo hallazgo comercial antes de presentarlo.

### 4. Reproducir en navegador

Prioriza una muestra dirigida por riesgo y cercania a la conversion. Prueba escritorio y al menos un viewport movil representativo cuando el diseno sea responsive.

Para cada candidato:

1. Registra pagina y recorrido exactos.
2. Describe la accion visible realizada.
3. Separa resultado esperado de resultado obtenido.
4. Repite una vez o busca una segunda evidencia antes de confirmarlo.
5. Revisa consola o red solo para explicar el comportamiento observado, sin convertir un error tecnico aislado en impacto comercial.
6. Limpia el estado reversible creado durante la prueba.

Registra tambien observaciones descartadas y por que. Evitar falsos positivos aumenta el valor del informe.

### 5. Clasificar la evidencia

Usa estas etiquetas de forma consistente:

- **Confirmado:** reproducido o corroborado con evidencia directa.
- **Inferido:** explicacion probable apoyada en evidencia, pero no demostrada.
- **Hipotesis:** posible efecto o mejora que necesita datos del negocio.
- **Pendiente:** requiere cuenta, dispositivo, dato, permiso o acceso interno.
- **Descartado:** la comprobacion mostro que no era una falla fiable.

No presentes una hipotesis como bug ni una consecuencia posible como perdida de ventas.

### 6. Atribuir control y alcance

Para cada hallazgo, separa:

- lo que controla directamente el negocio;
- tema, CMS, configuracion o app que el negocio puede modificar;
- integracion o plataforma con restricciones de plan;
- origen desconocido que requiere acceso interno.

Que un flujo use Shopify, WordPress, un proveedor de pagos u otra plataforma no elimina automaticamente la oportunidad. Puede ser tema, app, configuracion o comunicacion. Pero si la plataforma controla casi todo, baja la prioridad comercial y no vendas desarrollo a medida sin evidencia.

### 7. Priorizar por valor comercial verificable

Considera, en conjunto:

- proximidad a la conversion;
- cantidad de recorridos afectados;
- reproducibilidad y confianza;
- control probable del prospecto;
- esfuerzo aproximado y riesgo de cambio.

Usa prioridad comercial `alta`, `media` o `baja`; no la confundas con severidad de seguridad. Prefiere entre uno y tres hallazgos fuertes a una lista larga de detalles debiles.

Las features ausentes son hipotesis hasta comprobar que el negocio no las tiene y que resolverian una friccion real. Antes de proponer una, verifica capacidades existentes y formula que dato del negocio validaria su valor.

### 8. Formular la oportunidad sin sobreprometer

Por cada hallazgo confirmado documenta:

- identificador y titulo;
- prioridad y nivel de evidencia;
- pagina o recorrido;
- pasos de reproduccion;
- esperado y obtenido;
- consecuencia observable;
- impacto comercial posible, marcado como hipotesis;
- control probable: negocio, tema/app, plataforma o desconocido;
- intervencion minima razonable;
- criterio de cierre verificable;
- dudas que requieren acceso o conversacion.

Conclui si la evidencia sugiere:

- una correccion puntual;
- mantenimiento recurrente;
- una investigacion con acceso interno;
- una oportunidad de producto o automatizacion todavia no validada;
- o ningun trabajo atractivo.

Deci explicitamente que propuesta grande **no** esta justificada. No inventes ROI, trafico, conversion, ahorro ni urgencia.

### 9. Preparar el handoff comercial

Despues de cerrar la evidencia y el informe, crea `handoff-comercial.md` siguiendo `../shared/auditoria-a-venta.md`. El handoff no agrega conclusiones comerciales nuevas: transfiere hechos, consecuencias observables, hipotesis, vacios y preguntas cuya respuesta cambiaria una decision.

Prepara el artefacto incluso cuando el veredicto sea que no hay una razon suficiente para conversar. En ese caso, declara el descarte y evita fabricar preguntas para forzar una oportunidad.

Este paso no autoriza contacto, propuesta, cotizacion ni seguimiento. Si el usuario pide preparar la conversacion, entrega el handoff a la skill local `venta-con-criterio`.

## Entregables

Cuando haya filesystem disponible, crea `auditorias/<prospecto>/<AAAA-MM-DD>/` con:

- `informe.md`: lectura ejecutiva y hallazgos priorizados;
- `rutas.csv`: inventario publico;
- `pruebas-navegador.md`: bitacora de reproduccion, descartes y limites;
- `handoff-comercial.md`: evidencia transferible, hipotesis y preguntas para la siguiente conversacion;
- evidencia tecnica adicional solo si ayuda a reproducir o auditar el trabajo.

Usa la estructura exacta de [references/report-template.md](references/report-template.md). Para invocar el ejercicio fuera de esta skill, usa [references/prompt-base.md](references/prompt-base.md).

En el chat, entrega una sintesis con:

1. conclusion comercial;
2. cobertura y limites;
3. hasta tres hallazgos de entrada;
4. que no fue demostrado;
5. enlaces a los artefactos;
6. siguiente paso mas pequeno que requiere al usuario.

No contactes al prospecto, no publiques el informe y no redactes una acusacion de inseguridad salvo pedido separado del usuario.
