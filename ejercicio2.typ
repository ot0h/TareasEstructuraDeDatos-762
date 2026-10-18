#set page(paper: "a4", margin: (x: 2.2cm, y: 2cm), fill: white)
#set text(font: "Departure Mono", size: 11pt, fill: rgb("252525"))
#let bg = white
#let surface = rgb("e3e3e3")
#let border = rgb("525252")
#let muted = rgb("999999")
#let bright = rgb("f7f7f7")
#set par(justify: true, leading: 0.72em)

#align(center)[
  #text(size: 16pt, weight: "bold", fill: rgb("101010"))[Estructura de Datos]
  #linebreak()
  #text(
    size: 13pt,
    weight: "bold",
    fill: rgb("464646"),
  )[Ejercicio 2: Conversión de notación infija a postfija]
]

#v(1em)
#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  [*Nombre:* Raul Moncada], [*Número de registro:* 62314465],
)

= Expresión infija elegida

$ (M^(N - O)) / P + Q $

= Pasos

Leo la expresión de izquierda a derecha. Las letras van a la salida y los signos se guardan en la pila. Cuando aparece `)`, saco el signo de la pila y lo agrego a la salida.

#table(
  columns: (0.8fr, 1.7fr, 2fr, 1.25fr),
  inset: 6pt,
  stroke: (x, y) => if y == 0 { border } else { rgb("464646") },
  fill: (x, y) => if y == 0 { rgb("525252") } else if calc.even(y) {
    rgb("e3e3e3")
  } else { white },
  [#text(fill: rgb("f7f7f7"))[*Símbolo leído*]],
  [#text(fill: rgb("f7f7f7"))[*Acción*]],
  [#text(fill: rgb("f7f7f7"))[*Salida postfija*]],
  [#text(fill: rgb("f7f7f7"))[*Pila (base → tope)*]],

  [`(`], [Apilar], [—], [`(`],
  [`M`], [Agregar letra], [`M`], [`(`],
  [`^`], [Apilar], [`M`], [`( ^`],
  [`(`], [Apilar], [`M`], [`( ^ (`],
  [`N`], [Agregar letra], [`M N`], [`( ^ (`],
  [`-`], [Apilar], [`M N`], [`( ^ ( -`],
  [`O`], [Agregar letra], [`M N O`], [`( ^ ( -`],
  [`)`], [Sacar `-`; quitar `(`], [`M N O -`], [`( ^`],
  [`)`], [Sacar `^`; quitar `(`], [`M N O - ^`], [Vacía],
  [`/`], [Apilar], [`M N O - ^`], [`/`],
  [`P`], [Agregar letra], [`M N O - ^ P`], [`/`],
  [`+`], [Sacar `/` y guardar `+`], [`M N O - ^ P /`], [`+`],
  [`Q`], [Agregar letra], [`M N O - ^ P / Q`], [`+`],
  [Fin], [Sacar `+`], [`M N O - ^ P / Q +`], [Vacía],
)

= Resultado final

#align(center)[
  #rect(
    fill: surface,
    stroke: border,
    inset: 10pt,
    radius: 0pt,
  )[
    #text(size: 14pt, weight: "bold", fill: rgb("101010"))[$M N O -^P / Q +$]
  ]
]

= Comprobación

Primero se hace $N - O$. Después se eleva $M$ a ese resultado, se divide entre $P$ y se suma $Q$.
