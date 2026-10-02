# Panicafé - auditoría pública para prospección

Fecha: 2 de octubre de 2026. Sitio: https://panicafe.com/. Revisión externa, sin acceso autenticado.

## Evaluación comercial

Hay evidencia para ofrecer una intervención pequeña de integridad de contenido y configuración web. El punto de entrada más fuerte es una carta saludable enlazada como CTA principal que atribuye ingredientes incorrectos a dos platos. También hay una variante `www` que no resuelve y un recorrido de carta que siempre conduce a Cerro de las Rosas aunque la landing presenta siete sucursales.

Esto puede justificar revisar y corregir contenidos, dominios y recorridos entre canales. No demuestra que Panicafé necesite rediseñar el sitio, reemplazar Butter, construir pedidos online ni contratar mantenimiento recurrente. Tampoco conocemos tráfico, consultas, organización interna, proveedor actual, presupuesto o voluntad de contratar.

## Negocio y recorridos evaluados

- Conversión principal: consultar la carta y elegir una sucursal para visitar.
- Conversiones secundarias: abrir WhatsApp, llegar por Google Maps y cambiar al sitio de Estados Unidos.
- Plataforma e integraciones observadas: landing estática en Amazon S3/CloudFront, carta digital Butter, Google Maps, WhatsApp y PDF propio.
- Recorridos elegidos: portada → carta; portada → carta saludable; portada → sucursales; navegación interna; selector de país.
- Documentos y handoffs externos: PDF saludable de ocho páginas, carta Butter de Cerro de las Rosas, siete enlaces a Maps y sitio de Estados Unidos.

## Cobertura y límites

El sitio argentino es una landing de una sola página. `robots.txt` y `sitemap.xml` devuelven 404, por lo que la cobertura se construyó desde los enlaces de la portada. Se revisaron la única página HTML propia, el PDF enlazado, el destino de carta digital, el selector de país, las siete referencias de sucursales y las variantes HTTP/HTTPS y apex/`www`.

En navegador se probaron escritorio y emulación móvil 390 × 844. No se enviaron mensajes ni datos, y no se realizaron pedidos, reservas, pagos o pruebas activas de seguridad. No se confirmó si carta, precios u horarios son iguales en todas las sucursales.

### Artefactos de evidencia

- `rutas.csv`: superficies propias y handoffs críticos, con estado y control probable.
- `pruebas-navegador.md`: reproducciones, descartes y límites.
- `handoff-comercial.md`: evidencia, hipótesis y preguntas transferibles a la preparación comercial.

## Hallazgos priorizados

### P01 - La carta saludable publica ingredientes de otros productos

**Prioridad alta - confirmado.**

- Página o recorrido: portada → `Carta saludable PDF`, páginas de Ensalada Panicafé y Baguettín de guacamole.
- Reproducción: abrir el PDF y comparar ambos platos con sus fichas en la carta Butter enlazada por la misma landing.
- Esperado: cada recomendación describe la composición vigente del plato que nombra.
- Obtenido: ambas páginas repiten “Mini pan brioche hojaldrado, palta, salmón y queso crema”, una descripción que corresponde al Brioche de salmón.
- Consecuencia observable: la Ensalada Panicafé y el Baguettín de guacamole se presentan con ingredientes distintos de la carta digital actual. En Butter, la ensalada lleva hojas verdes, salmón, palta, brie y lino; el baguetín lleva masa madre, guacamole, huevo, tomates, limón y nachos.
- Impacto comercial posible: puede generar desconfianza o una elección basada en información incorrecta, especialmente porque el PDF formula recomendaciones de salud. No se comprobó que haya provocado reclamos ni se emite una conclusión médica o legal.
- Control probable: contenido propio y proceso editorial del negocio o su proveedor de diseño.
- Oportunidad mínima: corregir el PDF y revisar los cinco platos contra una fuente aprobada; establecer una única fuente para ingredientes y vigencia.
- Criterio de cierre: nombre, descripción e ingredientes coinciden entre PDF y carta vigente para todos los platos; un responsable del negocio aprueba la versión.
- Pendientes: confirmar recetas vigentes, alcance por sucursal y responsable de las afirmaciones nutricionales.

### P02 - `www.panicafe.com` no resuelve

**Prioridad media - confirmado mediante consulta HTTP.**

- Página o recorrido: ingreso directo a `https://www.panicafe.com/`.
- Reproducción: solicitar la variante `www`; la resolución DNS falla. `https://panicafe.com/` responde 200 y `http://panicafe.com/` redirige correctamente a HTTPS.
- Esperado: la variante habitual conduce al dominio canónico o, al menos, resuelve y redirige.
- Obtenido: el host `www` no resuelve.
- Consecuencia observable: quien escriba o siga esa variante no llega al sitio.
- Impacto comercial posible: pérdida de algunas visitas directas o enlaces antiguos; su volumen no está medido.
- Control probable: DNS y configuración de CloudFront/certificado.
- Oportunidad mínima: crear el alias y redirigirlo permanentemente al dominio apex.
- Criterio de cierre: HTTP y HTTPS con `www` resuelven sin advertencias y terminan en `https://panicafe.com/`.
- Pendientes: confirmar acceso al DNS y si existen enlaces o materiales impresos con `www`.

### P03 - Las cartas llevan siempre a una sola sucursal

**Prioridad media - recorrido confirmado; impacto condicionado.**

- Página o recorrido: cualquiera de las tres CTA `Ver carta` de la landing.
- Reproducción: abrirlas y revisar el encabezado y las opciones del destino Butter.
- Esperado: elegir sucursal antes de ver una carta específica, o dejar claro que la misma carta aplica a las siete.
- Obtenido: todas abren `PaniCafe - Cerro de las Rosas`; el panel muestra Av. Rafael Núñez 4385 y no mostró selector de sucursal.
- Consecuencia observable: el visitante que venía de una landing con siete sucursales recibe el contexto de Cerro de las Rosas.
- Impacto comercial posible: podría mostrar disponibilidad, precios o productos incorrectos si existen diferencias entre locales. Esa diferencia todavía no fue demostrada.
- Control probable: destino configurado en la landing y capacidades/configuración de Butter.
- Oportunidad mínima: confirmar la regla real; si las cartas difieren, elegir sucursal antes del handoff o enlazar cada local con su carta. Si son iguales, comunicarlo y usar un destino sin ambigüedad.
- Criterio de cierre: el visitante entiende a qué sucursal aplica la carta antes de usarla.
- Pendientes: confirmar si las siete sucursales comparten carta, precios y disponibilidad.

## Seguridad: resultado y alcance

No se confirmó ninguna vulnerabilidad. El dominio HTTP redirige a HTTPS. La respuesta pública de la landing no mostró HSTS, CSP, `X-Frame-Options` ni `X-Content-Type-Options`; en una landing estática esto es una oportunidad pasiva de endurecimiento, no evidencia de explotación ni un argumento para afirmar que el sitio es inseguro.

No se probaron inyecciones, fuerza bruta, autenticación, datos de terceros, manipulación de precios o carga. El sitio propio no expone formularios ni cuentas en el recorrido revisado.

## Funciones o mejoras que conviene validar

- Horarios y contacto por sucursal: validar primero cuántas consultas reciben preguntando si un local está abierto.
- Selector de sucursal antes de carta o WhatsApp: depende de que existan diferencias operativas o derivación por local.
- Datos estructurados `LocalBusiness`: no se observaron en la landing; priorizarlos solo con evidencia de búsqueda local y fichas verificadas.
- Flujo editorial único para carta, PDF y piezas de campaña: P01 aporta evidencia directa para revisarlo.

## Observaciones descartadas

- Dos H1 en el HTML: uno está dentro del selector de país oculto; no se declaró duplicación visible.
- Falta de sitemap y robots: no rompe la experiencia de una landing de una URL y no sostiene por sí sola una propuesta comercial.
- Catálogo Butter inicialmente vacío: fue un estado de carga; luego mostró productos y precios.
- Rediseño responsive: el menú móvil, las secciones y los CTA funcionaron en 390 × 844.

## Cómo usar estos resultados para prospectar

- Punto de entrada 1: mostrar la comparación breve entre el PDF y la carta vigente para Ensalada Panicafé y Baguettín de guacamole.
- Punto de entrada 2: mencionar el `www` como corrección técnica concreta y verificable.
- Punto de entrada 3: preguntar si carta y precios son iguales en las siete sucursales antes de proponer cambios.
- Intervención inicial razonable: corregir contenido y dominio, revisar todos los handoffs y dejar una prueba de regresión pequeña para futuras campañas.
- Lo que la evidencia todavía no justifica: rediseño completo, ecommerce, automatización grande, reemplazo de Butter o promesa de mayor facturación.
- Preguntas antes de cotizar: quién administra DNS y landing; quién actualiza Butter y el PDF; si las sucursales comparten menú; con qué frecuencia cambian ingredientes y promociones.
- Medida de resultado y línea de base requerida: errores de contenido detectados antes de publicar, CTA que llegan al contexto correcto y consultas recurrentes sobre carta, horarios o sucursal.

## Próxima prueba

Pedir al negocio una confirmación simple de recetas y diferencias por sucursal. Con esa información se puede acotar una corrección puntual y decidir si hay base para mantenimiento editorial.
