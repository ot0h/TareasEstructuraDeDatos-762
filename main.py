import os
import subprocess


def add_number(array: list[int]) -> list[int]:
    print("=== AGREGAR UN NUMERO ===")

    while True:
        try:
            number: int = int(input("Escribe el numero a ingresar: "))
            print(f"Se agrego correctamente el numero: {number}")
            break
        except ValueError:
            print("ERROR: Solo se puede ingresar numeros :P")

    array.append(number)
    return array


def is_full_array_numeric(numeric_array: list[int], size_limit_array) -> bool:
    return True if len(numeric_array) == size_limit_array else False


def show_last_number_in_array(numeric_array: list[int]):
    numeric_array.reverse()

    for index, num in enumerate(numeric_array):
        simbol_arrow = "=" * 5 if index == 0 else " " * 11
        print(f"{simbol_arrow} {'[TOPE]' if index == 0 else ''} {num}")
def clear_screen():
    cmd = "cls" if os.name == "name" else "clear"
    subprocess.run(cmd, shell=True)


def print_menu():
    menu = """
               MENU PILAS
    ----------------------------------
    1. Agregar número a la pila
    2. Verificar si la pila está vacía
    3. Sacar varios números de la pila
    4. Ver el último número agregado
    5. Mostrar cuántos números hay
    6. Simular una secuencia de caracteres
    0. Salir
    ----------------------------------
    """
    print(menu)


def main() -> None:
    numeric_array: list[int] = []
    characters_array: list[str] = []

    exit: bool = False

    while not exit:
        print_menu()

        while True:
            try:
                option: int = int(input("Ingresa una opción: "))
                if 0 <= option <= 6:
                    clear_screen()
                    print(
                        f"Se selecciono la opción {option}.",
                    )
                    break
                else:
                    print("Opción inválida. El número debe estar entre 0 y 6.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        match option:
            case 1:
                add_number(numeric_array)
            case 2:
                print("Verificar")
            case 3:
                print("Sacar")
            case 4:
                print("Ver el ultimo")
            case 5:
                print("Mostrar")
            case 6:
                print("Simular")
            case 0:
                print("Saliendo del programa...")
                exit = True


if __name__ == "__main__":
    main()
