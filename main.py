from cola_doble_entrada import ColaDobleEntrada
from cola_prioridad import ColaPrioridad, Paciente, Priority


def test_doble_entradation_colation():
    print("---- ESCENARIO A: MANGAS ----")

    cola = ColaDobleEntrada()

    cola.add_at_end("VAGABOND")
    cola.add_at_end("GIANT KILLING")
    cola.add_at_beginning("BERSERK")

    print("ESTANTE: ", cola.show())
    print("TOTAL DE MANGAS EN EL ESTANTE: ", cola.size_cola())
    print()

    print("SACAR EL ULTIMO MANGA: ", cola.sacation())

    print()

    print("LOS MANGAS RESTANTES: ", cola.show())
    print("EN TOTAL CUANTOS SON: ", cola.size_cola())
    print()


def test_priority_colation():
    print("\n---- ESCENARIO C: HOSPITAL")

    cola = ColaPrioridad()

    cola.push(Paciente("Raul", Priority.GENERAL))
    cola.push(Paciente("Diego", Priority.EMERGENCIA))
    cola.push(Paciente("Oliver", Priority.EMERGENCIA))
    cola.push(Paciente("Anderly", Priority.URGENTE))

    print("PACIENTES: ", cola.show())
    print()
    print("CANTIDAD DE PACIENTES: ", cola.size_cola())
    print()

    while not cola.is_empty():
        paciente = cola.sacation()

        if paciente is not None:
            print(f"Antendiendo: {paciente.name} ({paciente.priority.name})")
            print()


if __name__ == "__main__":
    test_doble_entradation_colation()
    test_priority_colation()
