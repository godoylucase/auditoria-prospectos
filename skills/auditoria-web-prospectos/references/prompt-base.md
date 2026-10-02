# Prompt base

Reemplaza los campos entre corchetes. Los opcionales pueden omitirse.

```text
Quiero auditar [URL] como posible prospecto para [tipo de servicio o "descubrir oportunidades tecnicas"].

Hace una revision externa, de bajo impacto y basada en evidencia. Recorre todas las rutas publicas que puedas descubrir razonablemente desde la portada, robots.txt, sitemaps y enlaces internos, evitando parametros infinitos y sin enumerar rutas privadas.

Si es una landing de una sola pagina o no publica sitemap, revisa sus secciones, documentos importantes y destinos externos que completan el recorrido —por ejemplo carta digital, agenda, mapas o portal de compra— sin rastrear entero el dominio del proveedor. Compara la informacion entre esas superficies. Comprueba tambien la redireccion HTTP/HTTPS y la variante habitual www/apex.

Primero entende que vende el negocio y cuales son sus recorridos de mayor valor. Despues busca y reproduce:
- bugs funcionales y recorridos rotos;
- enlaces o redirecciones con destino incorrecto;
- contradicciones de contenido, precio, envio, devoluciones, horarios o disponibilidad;
- fricciones cercanas a la conversion;
- capacidades aparentemente ausentes que valga la pena validar;
- indicadores pasivos de seguridad, sin hacer pruebas intrusivas ni afirmar vulnerabilidades no confirmadas.

Proba los recorridos relevantes en escritorio y movil. Podes avanzar por flujos reversibles como busqueda, seleccion, carrito o inicio de registro/checkout, pero no envies formularios, mensajes, reservas, pedidos o pagos. No crees cuentas ni uses datos personales sin pedirme que tome control. Limpia al terminar cualquier estado de prueba que hayas creado.

Para cada hallazgo separa hechos confirmados, inferencias, hipotesis, pendientes y falsos positivos descartados. Documenta pasos de reproduccion, esperado versus obtenido, consecuencia observable, impacto comercial solo como hipotesis, control probable del problema, intervencion minima y criterio de cierre.

Distingue lo que controla el negocio de lo que depende del tema, CMS, app, integracion o plataforma. Si el hallazgo solo justifica una correccion pequena, decilo; no lo conviertas artificialmente en un proyecto grande. No inventes ventas perdidas, ROI, trafico, presupuesto ni voluntad de contratar.

Guarda un informe, el inventario de rutas y una bitacora de pruebas. Termina con los uno a tres mejores puntos de entrada para una conversacion comercial, que propuesta todavia no esta justificada y el siguiente paso minimo.

Contexto opcional:
- Negocio: [nombre]
- Conversion principal esperada: [compra / reserva / demo / contacto / registro / desconocida]
- Mercado: [pais o region]
- Plataforma conocida: [plataforma o desconocida]
- Alcance autenticado autorizado: [ninguno por defecto]
- Limite adicional: [por ejemplo, no agregar productos al carrito]
```

## Version corta

```text
Audita [URL] como prospecto usando la skill auditoria-web-prospectos. Hace primero la etapa publica completa y de bajo impacto. No envies nada ni completes transacciones. Quiero evidencia reproducible, atribucion negocio/plataforma, una evaluacion comercial sin inflar el alcance y artefactos reutilizables.
```
