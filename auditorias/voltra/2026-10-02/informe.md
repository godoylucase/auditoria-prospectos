# Voltra — auditoría pública para prospección

Fecha: 2 de octubre de 2026. Sitio: https://voltra.com.ar/. Revisión externa, sin acceso administrativo.

## Evaluación comercial

Hay problemas reproducibles suficientes para una conversación comercial sobre mantenimiento y calidad del recorrido de compra en Shopify. Los mejores puntos de entrada son las pestañas rotas de una ficha, un enlace mayorista que termina en 404 y un botón de afeitadora que lleva a una mochila.

El impacto directo observado es la interrupción o confusión del recorrido. Que esto cause abandono, ventas perdidas o consultas adicionales es una hipótesis razonable, todavía sin medir. No conocemos tráfico, conversión, volumen de consultas, presupuesto, proveedor actual ni disposición a contratar. Encontrar errores demuestra una oportunidad técnica; no demuestra demanda comercial.

La skill CRO se usó para priorizar información necesaria para decidir, navegación, condiciones de compra y fricción. La conversión principal es comprar; mayoristas y contacto son caminos secundarios. No se conoce el origen del tráfico.

## Cobertura y límites

Se recorrieron las 63 URLs publicadas en los sitemaps de contenido y los enlaces internos descubiertos en su HTML. El inventario final contiene **78 URLs**: 41 de productos —incluye 3 alias—, 18 de colecciones —incluye 4 variantes de paginación—, 13 de páginas —incluye la ruta inexistente—, 4 de políticas, 1 blog y la portada. Hubo **77 respuestas finales HTTP 200 y 1 HTTP 404**. Dos de los 200 corresponden a enlaces de productos que terminan en la portada.

Esto cubre las hojas públicas descubiertas por sitemap y enlaces, no todas las rutas posibles del servidor. Se normalizaron variantes, seguimiento, filtros y ordenamientos para evitar combinaciones infinitas. El sitemap técnico de descubrimiento de agentes quedó fuera del inventario de contenido. No se enumeraron rutas privadas.

En las 78 URLs se comprobó respuesta, destino final, título, metadatos, enlaces y contenido HTML. La verificación interactiva fue una muestra dirigida: portada, mochila, mosquetón, ayuda de envíos, navegación mayorista, página mayorista vigente, contacto, búsqueda, entrada al checkout y acceso de clientes. Se verificaron la navegación y las pestañas de mochila en vista móvil de 390 × 844; no equivale a una certificación en dispositivos físicos ni a probar todas las variantes de todos los productos.

Archivos de evidencia:

- `rutas.csv`: URL, respuesta, destino, título y páginas que la enlazan.
- `pages.jsonl`: contenido público extraído y hora UTC de cada consulta. Puede contener textos ocultos de plantillas; no toda cadena equivale a un elemento visible.
- `sitemaps.json`: sitemaps y URLs de origen.
- `crawl-summary.json`: resumen del recorrido, sin URLs pendientes en la cola.
- `pruebas-navegador.md`: registro de reproducción y límites de las pruebas interactivas.

## Hallazgos priorizados

### V01 — Pestañas de información que no muestran contenido

**Prioridad alta · confirmado en navegador, escritorio y vista móvil.**

Página: [Mochila Voltra 45L](https://voltra.com.ar/products/mochila-voltra%C2%AE-core-45l).

Al pulsar las pestañas de envíos o garantía, el panel continúa vacío. La descripción tampoco aparece inicialmente en ese componente. La consola registra un `SyntaxError` dentro de `showTabContent`, disparado tanto en la carga como al hacer clic. El selector rechazado es `showTabContent('${tabId}')`.

Reproducción: abrir la ficha, bajar hasta el bloque de tres pestañas situado debajo de la compra y pulsar envíos o garantía. Esperado: información correspondiente visible. Obtenido: área vacía y excepción JavaScript.

Oportunidad: reparar el componente y verificar los tres paneles, teclado, móvil y las demás plantillas que reutilicen ese código. Hace falta acceso al tema para determinar el alcance compartido y aplicar el cambio. No se afirma que todas las fichas tengan la misma falla.

### V02 — La promoción de una afeitadora lleva a una mochila

**Prioridad alta · confirmado siguiendo el botón.**

Página: [portada](https://voltra.com.ar/), sección de afeitado identificada por el título «Al ras, sin miedo». El botón de esa sección abre `/products/mochila-voltra%C2%AE-core-45l`.

Oportunidad: corregir el destino y revisar la correspondencia entre cada promoción y su producto. Criterio de cierre: el usuario llega a la afeitadora anunciada y conserva su contexto de compra. El SKU correcto debe confirmarse con el catálogo del negocio; no conviene elegirlo solo por semejanza de nombre.

### V03 — El enlace de venta mayorista de preguntas frecuentes da 404

**Prioridad alta · confirmado por HTTP y navegación móvil.**

Recorrido: menú → preguntas frecuentes → venta mayorista → [`/pages/venta-mayorista`](https://voltra.com.ar/pages/venta-mayorista). Se muestra una página no encontrada.

Existe otra [página mayorista vigente](https://voltra.com.ar/pages/mayoristas), accesible desde la entrada principal de mayoristas. Su catálogo carga y anuncia un mínimo de diez unidades combinadas. Por lo tanto, la falla está en uno de los accesos, no en la inexistencia de una oferta mayorista.

Oportunidad: actualizar el enlace compartido del menú y considerar una redirección de la ruta antigua a la vigente. Verificar ambos accesos. El rastreo encontró el enlace defectuoso en las 78 respuestas HTML inspeccionadas, incluidas las respuestas que redirigen a otras páginas.

### V04 — Dos enlaces promocionales de producto terminan en la portada

**Prioridad media · confirmado por enlaces HTML y destino HTTP final.**

| Origen | Destino enlazado | Resultado |
|---|---|---|
| [Sellador](https://voltra.com.ar/products/sellador-al-vacio-voltra) | `/products/sellador-al-vacio-voltra-portatil-recargable-para-bolsas-reutilizables-con-valvula-kit-bolsas` | Portada |
| [Afeitadora](https://voltra.com.ar/products/afeitadora-anti-cortes-100-sumergible-voltra%C2%AE) | `/products/afeitadora-corporal-anti-cortes-voltra-ipx7` | Portada |

Los enlaces corresponden a franjas promocionales presentes en el HTML de las fichas. Su exposición visual puede variar según plantilla y tamaño. No se contabilizan como 404: el problema es el destino semánticamente incorrecto después de la redirección.

Oportunidad: actualizar enlaces y redirecciones a las fichas correctas. Verificar clics desde los tamaños donde se muestran esas franjas.

### V05 — Condición de envío gratis comunicada tarde

**Prioridad media · confirmado en anuncio, carrito y ayuda.**

La franja general presenta el envío gratuito a todo el país sin aclarar un mínimo. En una prueba con un mosquetón de ARS 5.990, el carrito indicó que faltaban ARS 64.010 para obtenerlo. La suma corresponde a un umbral de ARS 70.000. La [ayuda de envíos](https://voltra.com.ar/pages/como-son-los-envios) indica que los costos se calculan al finalizar según dirección y paquete.

No se ingresó una dirección, por lo que no se verificó el costo de envío definitivo ni la aplicación real de la promoción en checkout. Lo confirmado es la inconsistencia de los mensajes previos a ese cálculo.

Oportunidad: acordar la regla real y comunicar importe mínimo, cobertura y excepciones de manera consistente en franja, producto, carrito y ayuda. Criterio de cierre: la promesa coincide con el cálculo real para casos por debajo y por encima del umbral.

### V06 — Devoluciones y operación con mensajes contradictorios

**Prioridad media · inconsistencia de contenido confirmada.**

La [ficha del mosquetón](https://voltra.com.ar/products/mosqueton-premium) ofrece un período de prueba y devolución de 30 días. La [página de garantías](https://voltra.com.ar/pages/politica-de-cambios-y-devoluciones) y la [política de reembolso](https://voltra.com.ar/policies/refund-policy) describen 10 días para arrepentimiento, sin uso, y distinguen las fallas de fabricación.

También hay diferencias operativas: la ficha habla de despacho dentro de 24 horas hábiles y atención del showroom de lunes a viernes; la ayuda informa 24–48 horas, hasta 72 en alta demanda, y atención de lunes a sábado con intervalo al mediodía. La ayuda mezcla OCA/ZETA con instrucciones de seguimiento de Andreani.

Oportunidad: definir una fuente única de condiciones operativas y reutilizarla en las plantillas. El negocio debe confirmar su política y obtener revisión jurídica cuando corresponda. Esta auditoría detecta contradicciones; no emite una conclusión de cumplimiento legal.

### V07 — Campaña de verano visible en octubre

**Prioridad baja · confirmado visualmente.**

La ficha de mochila muestra una promoción presentada como exclusiva de verano el 2 de octubre de 2026. La captura de escritorio y la vista móvil la muestran junto al selector de packs.

Oportunidad: revisar vigencia y programación de campañas. No se comprobó si el contador vence, se reinicia o corresponde a una promoción individual: no se afirma que sea falso.

### V08 — Colección vacía y deuda de metadatos

**Prioridad baja · confirmado en HTML, pendiente de valor comercial.**

[`/collections/afeitadoras-voltra`](https://voltra.com.ar/collections/afeitadoras-voltra) está publicada en el sitemap pero muestra cero productos. La [categoría principal de afeitadoras](https://voltra.com.ar/collections/afeitadoras-sumergibles) sí tiene catálogo.

Quince URLs de productos del inventario no tienen meta descripción en el HTML. Esto es una oportunidad editorial a priorizar con tráfico orgánico y Search Console; no demuestra una penalización ni permite prometer posicionamiento. Los conteos de H1 del CSV son del HTML completo y pueden incluir variantes ocultas: requieren revisión visual antes de presentarlos como problemas.

Oportunidad: decidir si la colección vacía debe completarse, retirarse de publicación o redirigirse; trabajar los metadatos de las fichas que realmente atraigan búsquedas.

## Seguridad: resultado y alcance

**No se confirmó ninguna vulnerabilidad de seguridad.** La portada utiliza HTTPS y devuelve HSTS, `X-Frame-Options: DENY`, protección contra interpretaciones erróneas del tipo de contenido y una política CSP que restringe la incrustación en marcos y actualiza solicitudes inseguras. Estas observaciones son de una respuesta pública; no certifican todo el sitio.

No se probaron inyecciones, evasión de autenticación, acceso a pedidos ajenos, fuerza bruta, manipulación de importes, descubrimiento de secretos ni carga. El acceso de clientes está delegado a Shopify. Los errores de navegación y JavaScript descritos son defectos funcionales, no pruebas de exposición de datos.

Si el negocio solicita una evaluación de seguridad activa, esa etapa necesita alcance y autorización propios del titular. No hay base para acercarse al prospecto con una afirmación de que su tienda es insegura.

## Funciones y mejoras que conviene validar antes de proponer

- **Costo y fecha estimada por código postal antes del checkout:** podría resolver dudas si existen consultas o abandono por envío. Confirmar primero reglas logísticas y métricas.
- **Condiciones comerciales centralizadas:** tiene sustento directo en V05 y V06; reduce la posibilidad de que distintas fichas comuniquen reglas diferentes.
- **Pruebas de regresión de recorridos principales:** cubrir promociones, mayoristas, pestañas, variantes y carrito después de cambios del tema o apps. Tiene sustento directo en V01–V04.
- **Depuración del checkout:** revisar textos extensos en campos, dos métodos visibles con el mismo nombre de tarjeta y elección de marketing preseleccionada. Es una hipótesis de claridad y elección informada; no se demostró que impida comprar ni que sea una vulnerabilidad.

El sitio ya ofrece buscador, filtros, variantes, reseñas, recomendaciones, descuentos por volumen, WhatsApp y checkout sin cuenta. No sería razonable vender esas capacidades como ausentes a partir de esta revisión.

## Próxima prueba con Lucas

Ya se llegó al checkout como invitado con un artículo. La cuenta es opcional en ese recorrido. Para la etapa autenticada:

1. Lucas inicia sesión o crea la cuenta personalmente y resuelve el acceso por email. No hace falta compartir contraseña ni códigos en el informe.
2. Revisar una ficha de alto valor y un accesorio, selección de variante disponible/agotada, cantidad, persistencia del carrito y eliminación.
3. Con datos de entrega elegidos por Lucas, comprobar costo/plazo de envío y retiro. Comparar pedidos por debajo y por encima del mínimo comunicado.
4. Revisar aplicación del 10% por transferencia y reglas de acumulación con promociones o packs. Evitar enviar comprobantes o confirmar un pedido manual.
5. Verificar resumen, importe, moneda y condiciones antes del botón final. Detenerse antes de pagar o crear una orden, incluso si el medio es transferencia.

Quedaron sin probar: envío de contacto y newsletter, recepción de emails/WhatsApp, cuenta autenticada, dirección y cotización real, descuentos finales, cobro, pedido, seguimiento y devoluciones. No se enviaron mensajes al negocio.

## Cómo usar estos resultados para prospectar

Recomiendo abrir la conversación con V01–V03 y una demostración breve reproducible. El trabajo inicial razonable sería corregir esos recorridos, comprobarlos en móvil/escritorio y después medir su uso. La evidencia disponible no justifica todavía una reconstrucción completa del sitio, una automatización grande ni una promesa de aumento de ventas.

Antes de cotizar: confirmar quién administra Shopify, qué tema/apps generan esos componentes y qué recorridos concentran tráfico o consultas. Para medir resultado: clics de promoción → ficha correcta, acceso mayorista sin error, apertura efectiva de información y abandono por etapa, con una línea de base del negocio.
