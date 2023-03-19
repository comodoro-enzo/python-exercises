import string, random, sys, subprocess

# clear screen function
def clear_screen():
    operating_system = sys.platform

    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif (operating_system == 'linux') or (operating_system == 'darwin'):
        subprocess.run('clear', shell=True)

def guess(x = 1, y = 10):
    # x -> ínfimo
    # y -> supremo
    print(f"Adivina el número entre {x} y {y}")
    random_number = random.randint(x, y)

    user_guess = random_number + 1

    while user_guess != random_number:
        try:
            user_guess = int(input("Ingresa un número: "))

            if user_guess < x or user_guess > y:
                raise ValueError

            clear_screen()

            # a esta altura ya es un entero perteneciente al [x, y]
            if user_guess < random_number:
                print(f"Incorrecto. Debe ser mayor que {user_guess}")
            elif user_guess > random_number:
                print(f"Incorrecto. Debe ser menor que {user_guess}")
            else:
                print(f"Correcto! El número es {random_number}")

        except ValueError:
            clear_screen()

            print(f"Debes ingresar un número entero entre {x} y {y}")


guess(1, 100)

# Resumen:
# La función guess recibe dos enteros 'x' e 'y', siendo x < y
# define 2 variables:
    # la primera variable es random_number y guarda un número entero aleatorio perteneciente al intervalo [x, y]
    # la segunda variable es user_guess y sirve para registrar las elecciones del usuario al intentar adivinar el número 
# el bucle while se ejecuta hasta que el usuario acierte, si el número es incorrecto muestra el feedback al usuario indicando si el número debe ser mayor o menor
# NOTA: la variable user_guess se inicializa con el valor de <número a adivinar> + 1 para que sea distinta al valor de random_number y entre en el bucle la primera vez

