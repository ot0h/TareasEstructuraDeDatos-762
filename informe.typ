#set page(
  paper: "a4",
  margin: 2.0cm,
)

#set text(
  font: "Libertinus Serif",
  size: 11pt,
  lang: "es",
)

#set par(justify: true)
#set heading(numbering: "1.")

#align(center)[
  #text(size: 16pt, weight: "bold")[
    Análisis de problemas de colas
  ]

  Estructura de Datos — Semana 2
]

= Introducción

Las colas son estrucutras de datos donde nos permiten almacenar y retirar elementos siguiendo el principio de FIFO(*FIRST IN,FIRST OUT*). Donde se desarrollo la actividad con el lenguage de Python donde se selecciono los escenarios A (Cola de Doble Entrada) y C (Cola de Priodidad)

= Caso A: Cola con doble entrada

Se realizo un sistema para organizar mangas en un estante, donde se pueden agregar mangas por ambos extremos, pero quitarlo solamente por el frente.

La clase `ColaDobleEntrada` utiliza los métodos *`add_at_beginning()`*, *`add_at_end()`*, *`sacation()`*, *`show()`* y *`size_cola()`*.

Para comprobar su funcionamiento se agregaron tres mangas:

+ VAGABOND (final).
+ GIANT KILLING (final).
+ BERSERK (inicio).

El orden resultante fue:

#align(center)[
  *BERSERK → VAGABOND → GIANT KILLING*
]

Al retirar el primer manga, quedan VAGABOND y GIANT KILLING, con un total de dos mangas.

== Evidencia de ejecución

#figure(
  image("imagenes/escenario-a.png", width: 90%),
  caption: [Ejecución de la cola con doble entrada.],
)

= Caso C: Cola con prioridades

Se implementó un sistema de atención hospitalaria donde los pacientes se atienden según su nivel de urgencia: emergencia, urgente o general.

La clase `ColaPrioridad` utiliza objetos *`Paciente`* con los atributos *`name`* y *`priority`*. Sus métodos principales son *`push()`*, *`sacation()`*, *`show()`*, *`size_cola()`* e *`is_empty()`*.

Se registraron los siguientes pacientes:

#table(
  columns: (1fr, 1fr),
  [*Paciente*], [*Prioridad*],
  [Raul], [General],
  [Diego], [Emergencia],
  [Oliver], [Emergencia],
  [Anderly], [Urgente],
)

El orden esperado de atención es:

+ Diego.
+ Oliver.
+ Anderly.
+ Raul.

Los pacientes con mayor urgencia son atendidos primero. Cuando comparten la misma prioridad, se respeta su orden de llegada.

== Evidencia de ejecución

#figure(
  image("imagenes/escenario-c.png", width: 90%),
  caption: [Ejecución de la cola con prioridades.],
)

= Ejecución Completa del Main.py
#figure(
  image("imagenes/completo.png", width: 90%),
  caption: [Ejecución completa del Main],
)
= Conclusión

La actividad permitió aplicar dos variantes del TDA Cola mediante Python. La cola con doble entrada facilita el ingreso de elementos desde ambos extremos, mientras que la cola con prioridades organiza la salida de los elementos según su importancia.
