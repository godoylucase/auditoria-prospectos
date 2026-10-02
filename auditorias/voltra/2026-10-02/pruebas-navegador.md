# Registro de pruebas interactivas

Fecha: 2026-10-02. Horas aproximadas entre 09:42 y 09:52 ART. Navegador integrado; escritorio por defecto, vista móvil temporal 390 × 844. Las capturas se visualizaron durante la sesión; no se guardaron archivos de imagen. Este documento es un registro sintetizado de observaciones, no un volcado automático del navegador.

| Prueba | Resultado observado | Evidencia y alcance |
|---|---|---|
| Portada → botón de afeitadora | Abre mochila | URL final `/products/mochila-voltra%C2%AE-core-45l`; título y ficha de mochila visibles |
| Mochila → envíos | Panel no aparece | Excepción `querySelector` en carga y clic; texto de envíos ausente del contenido renderizado |
| Mochila → garantía en móvil | Panel no aparece | Misma área vacía en captura 390 × 844 |
| Menú → preguntas frecuentes → venta mayorista | Página no encontrada | Ruta `/pages/venta-mayorista`, 404 y captura móvil |
| Página `/pages/mayoristas` | Carga catálogo y controles | Mínimo diez unidades, avance deshabilitado con cero; no se agregaron cantidades ni datos |
| Ayuda mayorista | Video visible | La extracción de texto parecía vacía; la captura mostró un video. Se descartó como bug |
| Contacto | Campos y WhatsApp visibles | Sin enviar formulario ni abrir conversación |
| Buscador → mochila | Tres resultados | Mochila, mosquetón y parches; búsqueda resuelta por la UI |
| Mosquetón rosa → carrito | Un artículo, ARS 5.990 | Primera interacción coincidió con popup; se confirmó carrito vacío antes de reintentar. Segundo intento exitoso |
| Carrito bajo mínimo | Faltan ARS 64.010 para envío gratis | Total del artículo ARS 5.990; umbral inferido ARS 70.000 |
| Carrito → pago con tarjeta | Checkout de invitado disponible | Artículo y subtotal correctos; envío pendiente de dirección; ningún dato personal ingresado |
| Limpieza del carrito | Cero artículos | Se retiró solo la línea de mosquetón creada en esta auditoría; respuesta confirmó `item_count: 0` |
| Acceso de clientes | Pantalla de Shopify | Campo email, continuar, términos y marketing preseleccionado; no se continuó |

## Excepción reproducida en mochila

```text
SyntaxError: Failed to execute 'querySelector' on 'Document':
'showTabContent('${tabId}')' is not a valid selector.
at showTabContent
at HTMLDivElement.onclick
```

Lectura del DOM confirmó tres controles `DIV` con manejadores:

```text
Descripción -> showTabContent('when-to-take')
Envíos      -> showTabContent('description')
Garantía    -> showTabContent('ingredients')
```

No se ejecutó JavaScript para modificar la página. La reproducción consistió en pulsar los controles visibles y leer el estado y la consola. El mismo selector inválido apareció al cargar la página y al pulsar envíos.

## Checkout observado

Se visitó la primera pantalla, sin completar campos ni pulsar el botón final. Se vieron correo, entrega o retiro, datos de domicilio, documento, teléfono, métodos de pago, cupón y resumen. Dos opciones se presentaron con el mismo nombre de tarjeta; se dejó como hipótesis de claridad. La opción de marketing apareció marcada por defecto. La promoción de transferencia no fue seleccionada ni verificada.

Se omiten deliberadamente tokens y URLs de sesión del checkout y autenticación. No se creó cuenta, pedido ni suscripción. El viewport temporal se restableció.

## Observaciones descartadas o pendientes

- El HTML incluye cadenas de agotado y error de disponibilidad que pueden estar ocultas. No se declararon fallos de stock o retiro solo por encontrarlas.
- El primer clic del carrito no produjo incorporación, pero el reintento sin el popup funcionó: no se declaró una falla general de agregar al carrito.
- Algunos videos mostraron mensajes de reproducción en el árbol de accesibilidad. No se concluyó que estén rotos sin comprobar compatibilidad multimedia.
- El texto estático del mayorista menciona un descuento que no aparece igual en la UI móvil cargada. No se declaró discrepancia de precio sin confirmar la promesa visible aplicable.
- No se midieron Core Web Vitals. El tiempo y tamaño de una respuesta HTML del CSV no equivalen al rendimiento real de la página.
