# Registro de pruebas interactivas

Fecha: 2 de octubre de 2026, aproximadamente 10:25–10:40 ART. Navegador Chrome; escritorio y emulación móvil de 390 × 844. Revisión externa sin autenticación.

| Prueba | Resultado observado | Evidencia y alcance | Estado |
|---|---|---|---|
| Portada en escritorio | Carga propuesta, secciones, cartas y siete sucursales | Navegación visible y sin bloqueo | confirmado |
| Navegación interna | `Sabores` y `Contacto` cambian el fragmento y llevan a la sección | Probado en escritorio y móvil | confirmado |
| Menú móvil | El botón abre y cierra; `Sabores` y `Contacto` funcionan | Emulación 390 × 844 | confirmado |
| Selector de país | Abre Argentina y Estados Unidos; Argentina cierra el selector | El enlace de Estados Unidos respondió HTTP 200; no se auditó ese sitio | confirmado |
| CTA `Ver carta` | Abre Butter en `PaniCafe - Cerro de las Rosas` | El menú carga categorías, productos y precios | confirmado |
| Contexto de la carta | Las tres CTA de la landing llevan a Cerro de las Rosas | El panel de Butter muestra dirección Av. Rafael Núñez 4385 y no mostró selector de sucursal | confirmado |
| Carta saludable PDF | Abre un PDF legible de ocho páginas | Creado el 3 de agosto de 2026; se extrajo texto y se renderizaron las páginas relevantes | confirmado |
| PDF → Ensalada Panicafé | El PDF dice “Mini pan brioche hojaldrado, palta, salmón y queso crema” | Butter describe “Mix de hojas verdes, salmón curado, palta, queso brie y semillas de lino” | confirmado |
| PDF → Baguettín de guacamole | El PDF repite la descripción del brioche de salmón | Butter describe pan de masa madre, guacamole, huevo poché, tomates, limón y nachos | confirmado |
| PDF → Brioche de salmón | La frase repetida corresponde a este producto | Butter muestra la misma base y agrega acompañamiento de nachos | confirmado |
| Dominio HTTP | Redirige en un salto a `https://panicafe.com/` | Consulta HTTP pasiva | confirmado |
| Variante `www` | `www.panicafe.com` no resolvió DNS | Repetido mediante consulta HTTP; el dominio apex sí funciona | confirmado |
| WhatsApp | El enlace público apunta a `wa.me/5493515489701` | No se abrió conversación ni se envió mensaje | pendiente |
| Mapas de sucursales | Hay siete enlaces con nombre de sucursal | No se validó la ficha, horario ni exactitud de cada resultado en Google | pendiente |

## Observaciones descartadas

- El HTML contiene dos `h1`, pero uno pertenece al selector de país oculto. En el estado normal solo hay un título principal visible; no se declaró un problema de jerarquía por el conteo bruto.
- `robots.txt` y `sitemap.xml` devuelven 404. En una landing de una sola URL esto no interrumpe al visitante y no se presenta como argumento comercial principal.
- La carta de Butter pareció vacía durante su carga inicial; después de esperar, mostró el catálogo completo. Se descartó como falla.
- La landing no muestra horarios. Se conserva como hipótesis para validar con consultas reales del negocio, no como bug.

## Límites

No se enviaron mensajes, formularios ni datos. No se probaron reservas, pedidos, pagos, cuentas ni disponibilidad física. No se verificó si todas las sucursales comparten carta, precios y horarios. No se hicieron pruebas activas de seguridad.
