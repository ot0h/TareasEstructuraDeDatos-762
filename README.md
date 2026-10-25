# Tarea 2: Analisis de problemas de colas

Realizando la tarea de analisis de problemas de colas.

Donde  se eligieron los casos A y C

El informe para esta tarea es [INFORME](informe.pdf)

## Archivos

- main.py -> Donde se realizo las pruebas de las colas
- cola.py -> La clase padre de las colas, con sus metodos principales
- cola_prioridad.py -> Clase de las colas de prioridades donde se se aplico un @dataclass que se puedeconsiderar como un struct en diferentes lenguajes, donde era de un Paciente con sus propiedades de mame y priority, donde ese priority se uso un enum.
- cola_doble_entrada.py -> Clase para las colas de doble entrada, donde se definino los metodoas para ingresar un elemento al principio y final.
- informe.typ -> Donde se estructuro el documento :V

#> [!NOTE]
Los archivos de cola_prioridad y cola_doble_entrada heredaron los metodos de cola.
> 

## Tecnologías

- Python 
- Typst -> Para crear los pdfs de los ejercicios que no son relacionados a codigo.

[← Volver al README principal](../../blob/main/README.md)
