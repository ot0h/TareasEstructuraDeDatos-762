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


def is_empty_pila(pila: list[int]) -> bool:
    return len(pila) == 0


def is_full_array_numeric(numeric_array: list[int], size_limit_array: int) -> bool:

    return len(numeric_array) == size_limit_array


def show_pila_seq_with_tope(numeric_array: list[int]):
    if len(numeric_array) == 0:
        print("ERROR: No se puede realizar esta función, se encuentra vacia la Pila")
        return

    numeric_array.reverse()

    for index, num in enumerate(numeric_array):
        simbol_arrow = "=" * 5 if index == 0 else " " * 11
        print(f"{simbol_arrow} {'[TOPE]' if index == 0 else ''} {num}")


def delete_quantity_in_array(array: list[int]):
    print("=== QUITANDO ITEMS SEGUN CANTIDAD ===")

    if is_empty_pila(array) == True:
        print("ERROR: No se puede realizar esta función, se encuentra vacia la Pila")
        return

    while True:
        try:
            cantidad_quitar: int = int(
                input("Ingresa la cantidad de elementos a eliminar: ")
            )
            quantity_message: int = cantidad_quitar

            if cantidad_quitar <= 0:
                print("Por favor, ingresa una cantidad mayor a 0.")
                continue

            if len(array) < cantidad_quitar:
                print(
                    "No se puede quitar esa cantidad de numeros, es muy pequeña la PILA"
                )
                return

            while cantidad_quitar != 0:
                array.pop()
                cantidad_quitar -= 1  # Reduces the counter by 1 each time

            break

        except ValueError:
            print("ERROR: Se debe ingresar la cantidad en un numero entero")

    print(f"Se quitaron los {quantity_message} elementos correctamente!")
    return array


def clear_screen():
    cmd = "cls" if os.name == "nt" else "clear"
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

    print("Ingresando al programa .....")
    print("Antes de continuar, debe establecer el tamaño del Arreglo Numerico.")

    while True:
        try:
            size_numeric_array: int = int(
                input("Ingresa el tamaño del Arreglo numero: ")
            )
            break
        except ValueError:
            print("Debe ser un numero entero")

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
                if is_full_array_numeric(numeric_array, size_numeric_array) == False:
                    add_number(numeric_array)
                else:
                    print(
                        f"Ya el tamño del arreglo llego al maximo {size_numeric_array}/{size_numeric_array}"
                    )

            case 2:
                print(
                    "La pila esta vacia"
                    if is_empty_pila(numeric_array)
                    else "La pila contiene elementos"
                )
            case 3:
                delete_quantity_in_array(numeric_array)
            case 4:
                print(f"ULTIMO NUMERO AGREGADO A LA PILA ES: {numeric_array[-1]}")
            case 5:
                show_pila_seq_with_tope(numeric_array)
            case 6:
                print("Simular")
            case 0:
                print("Saliendo del programa...")
                exit = True


if __name__ == "__main__":
    main()
