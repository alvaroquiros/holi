# coding=utf-8
from getpass import getpass


def press_enter_to_continue():
    getpass('\nPulsa intro para continuar...')


def op_sum(first_num, second_num):
    print(format('\nLa suma entre {} y {} es {}'.format(first_num, second_num, first_num + second_num)))
    press_enter_to_continue()

def op_sub(first_num, second_num):
    print(format('\nLa resta entre {} y {} es {}'.format(first_num, second_num, first_num - second_num)))
    press_enter_to_continue()

def op_power(first_num, second_num):
    """
    Esta función eleva un número por otro mediante el uso de bucles anidados y sumas.

    :param first_num:   número al que se se aplicara la elevación
    :param second_num:  número por el que se elevará
    :return:            el resultado de la elevación
    """

    # Función de ayuda para realizar multiplicaciones con dos operandos a base de sumas
    def in_op_multiply(in_first_num, in_second_num):
        in_res = in_first_num
        in_second_num -= 1

        # Se suma el primer valor al resultado hasta que el segundo número llegue a 0
        while in_second_num > 0:
            in_res += in_first_num
            in_second_num -= 1

        return in_res

    if second_num == 0:
        # Un número elevado a 0 es 1
        res = 1
    elif second_num == 1:
        # Un número elevado a 1 es el mismo número
        res = first_num
    else:
        # Llegados a este punto podemos estar seguros de que el segundo número (aka elevación) es de 2 o mas, por lo
        # que para empezar multiplicamos el primer número por si mismo y restamos dos al contador (que es el segundo
        # número)
        count = second_num - 2
        res = in_op_multiply(first_num, first_num)

        # Se multiplica el resultado por el primer número hasta que el contador llegue a 0
        while count > 0:
            res = in_op_multiply(res, first_num)
            count -= 1

    print(format('\nLa potencia de {} elevado a {} es {}'.format(first_num, second_num, res)))
    press_enter_to_continue()


def main():
    close_calculator = False

    while not close_calculator:
        print('##########################################################################')
        print('#                      Calculadora simple en Python                      #')
        print('#                                                                        #')
        print('# Todos los cálculos de esta calculadora estan hechos con sumas y restas #')
        print('##########################################################################')

        print('\n( 1) Sumar')
        print('( 2) Restar')
        print('( 3) Multiplicar')
        print('( 4) Dividir')
        print('( 5) Potencia')
        print('( 6) Raiz cuadrada')
        print('(-9) Salir')

        valid_input = False

        first_num = None
        second_num = None

        while not valid_input:
            try:
                operation = int(input('\nSelecciona la operación que deseas realizar: '))
            except ValueError:
                # Si el valor introducido no es un número se marca por defecto como no válido
                operation = 0

            if 1 <= operation <= 6:
                valid_input = True

                # Por sencillez las operaciones se realizaran con números absolutos
                first_num = abs(int(input('\nIntroduce el primer número: ')))
                second_num = abs(int(input('Introduce el segundo número: ')))

            if operation == -9:
                valid_input = True
                close_calculator = True

                print('\nLa calculadora se cerrara')

            if not valid_input:
                print('La operación seleccionada no existe')

            # Suma
            if operation == 1:
                op_sum(first_num, second_num)

            if operation == 2:
                op_sub(first_num, second_num)

            # Elevación
            if operation == 5:
                op_power(first_num, second_num)


if __name__ == '__main__':
    main()
