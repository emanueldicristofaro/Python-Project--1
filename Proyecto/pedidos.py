
# Toda la lógica principal de los pedidos de sandwiches y bebidas.

def pedidoSandwiches(nombre):

    contador = 1
    precio_total = 0
    precio_subtotal = 0
    precios_tamano = {'Triple': 580, 'Doble': 430, 'Individual': 280}
    precios_ingredientes = {'Jamon': 40, 'Champiñiones': 35, 'Pimentón': 30, 'Doble Queso': 40, 'Aceitunas': 57.5
    , 'Pepperoni': 38.5, 'Salchichón': 62.5}
    lista_ingredientes_escogidos = []
    lista_bebidas_escogidas = []
    eleccion_escogida = ''
    lista_bebidas = ['Pepsi', 'Coca Cola', 'Frescolita', 'Chinotto']
    lista_ingredientes = ['Jamón', 'Champiñiones', 'Pimentón', 'Doble Queso', 'Aceitunas', 'Pepperoni', 'Salchichón']

    precios_bebidas = {'Pepsi': 15, 'Coca Cola': 17, 'Frescolita': 14, 'Chinotto': 15}

    option = ''
    while option != '4':
        if option == '1':
            print(f'\n\nSandwich número {contador}')
            print()
            print('Escoja una opción')
            print('Tamaños: Triple ( t ) Doble ( d ) Individual ( i ):')

            eleccion = input('Introduzca su eleccion: ')
            eleccion = eleccion.lower()

            if eleccion == 't':
                precio_subtotal = precio_subtotal + precios_tamano.get('Triple')
                eleccion_escogida = 'Triple'

                print('Haz seleccionado el tamaño triple')
                si_no = 'si'
                print()
                print('Por favor indique los ingredientes que desee usar')
                print()
                print('Ingredientes: ')
                print('Jamón indique (ja)')
                print('Champiñiones indique (ch)')
                print('Pimentón indique (pi)')
                print('Doble Queso indique (dq)')
                print('Aceitunas indique (ac)')
                print('Pepperoni indique (pp)')
                print('Salchichón indique (sa)')
                print()
                while si_no == 'si':
                    eleccion_s = input('Indique su elección (enter para terminar): ')
                    eleccion_s = eleccion_s.lower()

                    if eleccion_s == 'ja':
                        lista_ingredientes_escogidos.append(lista_ingredientes[0])
                        precio_subtotal = precio_subtotal + precios_ingredientes.get('Jamon')

                    elif eleccion_s == 'ch':
                        lista_ingredientes_escogidos.append(lista_ingredientes[1])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Champiñiones')

                    elif eleccion_s == 'pi':
                        lista_ingredientes_escogidos.append(lista_ingredientes[2])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Pimentón')

                    elif eleccion_s == 'dq':
                        lista_ingredientes_escogidos.append(lista_ingredientes[3])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Doble Queso')

                    elif eleccion_s == 'ac':
                        lista_ingredientes_escogidos.append(lista_ingredientes[4])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Aceitunas')

                    elif eleccion_s == 'pp':
                        lista_ingredientes_escogidos.append(lista_ingredientes[5])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Pepperoni')

                    elif eleccion_s == 'sa':
                        lista_ingredientes_escogidos.append(lista_ingredientes[6])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Salchichón')

                    elif eleccion_s == '':
                        print()
                        print('Usted seleccionó un sandwich ' + eleccion_escogida, end=' '),
                        if lista_ingredientes_escogidos:
                            print('con ', end='')
                            for ingerdiente in lista_ingredientes_escogidos:
                                print(ingerdiente, end=", ")
                        print(f'\nSubtotal a pagar por un sandwich {eleccion_escogida}: {precio_subtotal}')
                        precio_total += precio_subtotal
                        precio_subtotal = 0
                        print()
                        print(f'Precio total del pedido {precio_total} BsS')
                        contador += 1                
                        si_no = 'no'
                        break

                    else:
                        print('Por favor indique el ingrediente como se le solicita')
            elif eleccion == 'd':
                precio_subtotal = precio_subtotal + precios_tamano.get('Doble')
                eleccion_escogida = 'Doble'

                print('Haz seleccionado el tamaño doble')
                si_no = 'si'
                print()
                print('Por favor indique los ingredientes que desee usar')
                print()
                print('Ingredientes: ')
                print('Jamón indique (ja)')
                print('Champiñiones indique (ch)')
                print('Pimentón indique (pi)')
                print('Doble Queso indique (dq)')
                print('Aceitunas indique (ac)')
                print('Pepperoni indique (pp)')
                print('Salchichón indique (sa)')
                print()
                while si_no == 'si':
                    eleccion_s = input('Indique su elección (enter para terminar): ')
                    eleccion_s = eleccion_s.lower()

                    if eleccion_s == 'ja':
                        lista_ingredientes_escogidos.append(lista_ingredientes[0])
                        precio_subtotal = precio_subtotal + precios_ingredientes.get('Jamon')

                    elif eleccion_s == 'ch':
                        lista_ingredientes_escogidos.append(lista_ingredientes[1])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Champiñiones')

                    elif eleccion_s == 'pi':
                        lista_ingredientes_escogidos.append(lista_ingredientes[2])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Pimentón')

                    elif eleccion_s == 'dq':
                        lista_ingredientes_escogidos.append(lista_ingredientes[3])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Doble Queso')

                    elif eleccion_s == 'ac':
                        lista_ingredientes_escogidos.append(lista_ingredientes[4])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Aceitunas')

                    elif eleccion_s == 'pp':
                        lista_ingredientes_escogidos.append(lista_ingredientes[5])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Pepperoni')

                    elif eleccion_s == 'sa':
                        lista_ingredientes_escogidos.append(lista_ingredientes[6])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Salchichón')

                    elif eleccion_s == '':
                        print()
                        print('Usted seleccionó un sandwich ' + eleccion_escogida, end=' '),
                        if lista_ingredientes_escogidos:
                            print('con ', end='')
                            for ingerdiente in lista_ingredientes_escogidos:
                                print(ingerdiente, end=", ")
                        print(f'\nSubtotal a pagar por un sandwich {eleccion_escogida}: {precio_subtotal}')
                        precio_total += precio_subtotal
                        precio_subtotal = 0
                        print()
                        print(f'Precio total del pedido {precio_total} BsS')
                        contador += 1                
                        si_no = 'no'
                        break

                    else:
                        print('Por favor indique el ingrediente como se le solicita')
            elif eleccion == 'i':
                precio_subtotal = precio_subtotal + precios_tamano.get('Individual')
                eleccion_escogida = 'Individual'

                print('Haz seleccionado el tamaño individual')
                si_no = 'si'
                print()
                print('Por favor indique los ingredientes que desee usar')
                print()
                print('Ingredientes: ')
                print('Jamón indique (ja)')
                print('Champiñiones indique (ch)')
                print('Pimentón indique (pi)')
                print('Doble Queso indique (dq)')
                print('Aceitunas indique (ac)')
                print('Pepperoni indique (pp)')
                print('Salchichón indique (sa)')
                print()
                while si_no == 'si':
                    eleccion_s = input('Indique su elección (enter para terminar): ')
                    eleccion_s = eleccion_s.lower()

                    if eleccion_s == 'ja':
                        lista_ingredientes_escogidos.append(lista_ingredientes[0])
                        precio_subtotal = precio_subtotal + precios_ingredientes.get('Jamon')

                    elif eleccion_s == 'ch':
                        lista_ingredientes_escogidos.append(lista_ingredientes[1])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Champiñiones')

                    elif eleccion_s == 'pi':
                        lista_ingredientes_escogidos.append(lista_ingredientes[2])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Pimentón')

                    elif eleccion_s == 'dq':
                        lista_ingredientes_escogidos.append(lista_ingredientes[3])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Doble Queso')

                    elif eleccion_s == 'ac':
                        lista_ingredientes_escogidos.append(lista_ingredientes[4])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Aceitunas')

                    elif eleccion_s == 'pp':
                        lista_ingredientes_escogidos.append(lista_ingredientes[5])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Pepperoni')

                    elif eleccion_s == 'sa':
                        lista_ingredientes_escogidos.append(lista_ingredientes[6])
                        precio_subtotal = precio_subtotal + \
                        precios_ingredientes.get('Salchichón')

                    elif eleccion_s == '':
                        print()
                        print('Usted seleccionó un sandwich ' + eleccion_escogida, end=' '),
                        if lista_ingredientes_escogidos:
                            print('con ', end='')
                            for ingerdiente in lista_ingredientes_escogidos:
                                print(ingerdiente, end=", ")
                        print(f'\nSubtotal a pagar por un sandwich {eleccion_escogida}: {precio_subtotal}')
                        precio_total += precio_subtotal
                        precio_subtotal = 0
                        print()
                        print(f'Precio total del pedido {precio_total} BsS')
                        contador += 1                
                        si_no = 'no'
                        break

                    else:
                        print('Por favor indique el ingrediente como se le solicita')
            else:
                print('Por favor debe escoger uno de los tamaños indicados')

        if option == '2':
            print()

        if option == '3':

            print()
            print(f'Usted seleccionó el sandwich de tamaño {eleccion_escogida}')
            print(f'Los ingredientes escogidos fueron {lista_ingredientes_escogidos}')
            print(f'Precio total a pagar {precio_total}')

            si_no_p = input('¿Desea continuar? si/no: ')
            si_no_p = si_no_p.lower()

            if si_no_p == 'si':
                print()
                print(f'EL pedido tiene un total de un sandwich por un monto de {precio_total}')
                print('Gracias por su compra, regrese pronto')
                contador += 1
                eleccion_escogida = ''
                precio_total = 0
                lista_ingredientes_escogidos.clear()

            elif si_no_p == 'no':
                eleccion_escogida = ''
                precio_total = 0
                lista_ingredientes_escogidos.clear()
            
            else:
                print('Por favor indique si/no')

        print()
        print(f'Bienvenido a sandwiches GUNS N ROSES {nombre}')
        print()

        print('Sandwiches...')
        print('╔═╦╦╦═╦═╗╔═╗╔═╦═╦═╦═╦═╗')
        print('║║║║║║║╚╣║║║║═║║║╚╣═╣╚╣')
        print('╠╗║║║║╠╗║║║║║╚╣║╠╗║═╬╗║')
        print('╚═╩═╩╩╩═╝╚╩╝╚╩╩═╩═╩═╩═╝')
        print('"Los mejores sandwiches que podrás comer"')

        print()
        option = input('\nMenú de Alimentos\n(1) Sandwich\n(2) Bebidas\n(3) Pagar\n(4) Salir\nElige una opción:')
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    