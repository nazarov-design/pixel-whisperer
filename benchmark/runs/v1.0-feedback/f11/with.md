**TL;DR** — ronda 1 de 3
1. Fotos reales de comida: héroe del plato, miniaturas y banner · 2. Color más vivo, iconos de categoría y jerarquía de tipografía más marcada · 3. Programa de puntos = petición nueva: mostrar solo un punto de entrada discreto y tratarlo como ampliación de alcance
Respuesta: "¡Gracias! Esta ronda ponemos la comida en primer plano y damos un aire más actual. Los puntos son una funcionalidad nueva que no estaba en el briefing; te propongo un pequeño avance y lo valoramos aparte."

## Decode: delivery-app

| # | Cliente dijo | Significado probable (confianza) | Cambio |
|---|---|---|---|
| 1 | "le falta vida" | a) sin imágenes reales ni personalidad (60%) | Todo es placeholder: círculo naranja, 2 miniaturas beige lisas. Poner fotos reales (ver #2) |
|   |  | b) paleta apagada y plana (25%) | Fondo beige del héroe y tarjetas de categoría en melocotón pálido → un acento cálido (~#FF6B35) con ≤10% de superficie |
|   |  | c) falta de microdetalles y calidez en el tono "fresco y cercano" (15%) | Copy más cercano ("¿Qué te apetece hoy?" en vez de "Deliver to"); es una pregunta, ver P1 |
| 2 | "que destaque más la comida" | a) las fotos no existen o son mínimas (65%) | Héroe del plato: círculo ~200px → foto a sangre ~340×240 con plato cenital; miniaturas ~70px → ~110px o tarjetas con foto grande; banner verde con plato recortado |
|   |  | b) la comida compite con elementos de UI (25%) | Banner verde ~300×120 vacío → reducir o integrarlo con foto; categorías: iconos/fotos de comida en vez de cuadrados lisos |
|   |  | c) descripción y precios con poco peso (10%) | Descripción gris ~13px → más contraste. Solo si la foto no basta |
| 3 | "más moderno" | a) estilo plano y genérico (50%) | Tarjetas con radio ~20–24px, sombra suave, fotos con esquinas redondeadas, títulos más grandes (H1 ~28 → ~34px) |
|   |  | b) paleta verde saturado + beige "de plantilla" (30%) | Verde #22C55E (~2.3:1 con texto blanco, no cumple 4.5:1) → verde más oscuro (~#15803D, ~5:1) o acento cálido; el verde ya dice "fresco", no hace falta quitarlo |
|   |  | c) falta de movimiento/transiciones (20%) | Mostrar estados: héroe con parallax, chips seleccionables. Es entrega, no estático |
| 4 | "¿podemos añadir un programa de puntos?" | a) funcionalidad nueva completa (70%) | Fuera del briefing (2 pantallas, inicio y plato). Mostrar solo un punto de entrada (chip "120 pts" en cabecera, marcador 5) y una línea en el plato ("Ganas 12 pts") |
|   |  | b) solo quiere ver la idea reflejada en el diseño (30%) | Mismo chip + línea, sin pantallas nuevas |

**Datos usados:** cabecera "Home" ~16px negrita · buscador ~40px alto, gris · categorías 5 tarjetas ~52px, melocotón pálido · banner verde #22C55E ~300×120, mitad vacío · miniaturas ~70px beige, sin foto · héroe del plato círculo naranja sobre beige ~340×240 · CTA verde 300×52 con texto blanco · tipografía sans (tipo Inter) · todos los valores son estimados (`~`).

### Keep as is
- A: título "Margherita" y jerarquía clara de la pantalla del plato: no tocarla al ampliar la foto (#1, #2).
- B: barra CTA "Add to order" con precio: se queda abajo, ancho completo (cambiar solo el tono de verde si se oscurece, #3).
- Base limpia y aireada (márgenes ~20px, lista de extras ordenada): no recargar al añadir fotos.

### Conflictos
- "Más vida" y "más moderno" pueden chocar con "fresco y cercano" si se vuelve frío o sobrecargado → priorizar fotos y color cálido, estética moderna por forma (radios, tipografía), no por efectos.
- #4 (puntos) vs. "destaque la comida": un chip más en cabecera compite con el foco → mantenerlo pequeño y neutro.
- Verde actual vs. accesibilidad: el texto blanco sobre #22C55E (~2.3:1) no llega a 4.5:1; hay que oscurecerlo aunque el cliente no lo haya pedido.

### Preguntas al cliente (máx. 3)
1. ¿Tenéis fotos de platos propias o usamos un banco de imágenes de referencia para la ronda?
2. "Más moderno": ¿A) formas más redondeadas y tipografía grande, o B) color más atrevido (acento cálido junto al verde)? Puedo enseñar ambas variantes.
3. Puntos: ¿lo vemos solo como idea visual en estas pantallas (chip + línea) o queréis diseñarlo completo (pantalla de puntos, canje, historial) como ampliación?

### Respuesta (idioma del cliente)
**Amable:** ¡Gracias por el feedback! Para esta ronda vamos a poner la comida en el centro: fotos reales en el plato, las miniaturas y el banner, con un toque de color y formas más actuales para que tenga más vida sin perder el tono fresco y cercano. Lo del programa de puntos nos encanta como idea. Como no estaba en el briefing inicial (inicio y plato), te propongo incluir solo un pequeño detalle visual como avance y, si quieres desarrollarlo entero (pantalla de puntos, canje…), lo presupuestamos aparte. ¿Tenéis fotos de platos o usamos referencias?

**Firme:** Gracias. En esta ronda trabajamos las fotos, el color y el estilo más actual de las dos pantallas acordadas. El programa de puntos es una funcionalidad nueva que queda fuera del alcance inicial; podemos incluir un indicador visual como muestra, y su diseño completo lo tratamos como ampliación con su propia estimación.

### Alcance
Ronda 1 de 3 · 3 peticiones dentro de alcance (#1–#3), 1 nueva (#4 programa de puntos, no está en el briefing) → mensaje de ampliación incluido en las respuestas. El ledger no registra importes ni nombres.

Overlay: `./benchmark/runs/v1.0-feedback/f11/with/.feedback-decoder/work/overlay.png`
Ledger: `./benchmark/runs/v1.0-feedback/f11/with/.feedback-decoder/delivery-app.md`

Nota: el overlay muestra el marcador 5 sobre un espacio vacío de la cabecera, que es donde propongo el chip de puntos. Esta carpeta no es un repo git, así que no he tocado ningún `.gitignore`.
