
# Toda la lógica principal de los pedidos de sandwiches y bebidas.

def pedidoSandwiches(nombre):

    contador = 1
    precio_total = 0
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
            
            print()
            print('Escoja una opción')
            print('Tamaños: Triple ( t ) Doble ( d ) Individual ( i ):')

            eleccion = input('Introduzca su eleccion: ')
            eleccion = eleccion.lower()

            if eleccion == 't':
                precio_total = precio_total + precios_tamano.get('Triple')
                eleccion_escogida = 'Triple'

                print('Haz seleccionado el tamaño triple')

                si_no = 'si'
                while si_no == 'si':
                    print()
                    print('Por favor indique los ingredientes que desee usar')
                    print('Si no desea ninguno solamente presione (q)')
                    print()
                    print('Ingredientes: ')
                    print('Jamón indique (ja)')
                    print('Champiñiones indique (ch)')
                    print('Pimentón indique (pi)')
                    print('Doble Queso indique (dq)')
                    print('Aceitunas indique (ac)')
                    print('Pepperoni indique (pp)')
                    print('Salchichón indique (sa)')

                    eleccion_s = input('Indique su elección: ')
                    eleccion_s = eleccion_s.lower()

                    if eleccion_s == 'ja':
                        lista_ingredientes_escogidos.append(lista_ingredientes[0])
                        precio_total = precio_total + precios_ingredientes.get('Jamon')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'ch':
                        lista_ingredientes_escogidos.append(lista_ingredientes[1])
                        precio_total = precio_total + precios_ingredientes.get('Champiñiones')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'pi':
                        lista_ingredientes_escogidos.append(lista_ingredientes[2])
                        precio_total = precio_total + precios_ingredientes.get('Pimentón')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'dq':
                        lista_ingredientes_escogidos.append(lista_ingredientes[3])
                        precio_total = precio_total + precios_ingredientes.get('Doble Queso')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'ac':
                        lista_ingredientes_escogidos.append(lista_ingredientes[4])
                        precio_total = precio_total + precios_ingredientes.get('Aceitunas')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'pp':
                        lista_ingredientes_escogidos.append(lista_ingredientes[5])
                        precio_total = precio_total + precios_ingredientes.get('Pepperoni')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'sa':
                        lista_ingredientes_escogidos.append(lista_ingredientes[6])
                        precio_total = precio_total + precios_ingredientes.get('Salchichón')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'q':
                        print()
                        print('Sandwich triple con queso')
                        break
                        
                    else:
                        print('Por favor indique el ingrediente como se le solicita')

            elif eleccion == 'd':
                precio_total = precio_total + precios_tamano.get('Doble')
                eleccion_escogida = 'Doble'

                print('Haz seleccionado el tamaño doble')

                si_no = 'si'
                while si_no == 'si':
                    print()
                    print('Por favor indique los ingredientes que desee usar')
                    print('Si no desea ninguno solamente presione (q)')
                    print()
                    print('Ingredientes: ')
                    print('Jamón indique (ja)')
                    print('Champiñiones indique (ch)')
                    print('Pimentón indique (pi)')
                    print('Doble Queso indique (dq)')
                    print('Aceitunas indique (ac)')
                    print('Pepperoni indique (pp)')
                    print('Salchichón indique (sa)')

                    eleccion_s = input('Indique su elección: ')
                    eleccion_s = eleccion_s.lower()

                    if eleccion_s == 'ja':
                        lista_ingredientes_escogidos.append(lista_ingredientes[0])
                        precio_total = precio_total + precios_ingredientes.get('Jamon')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'ch':
                        lista_ingredientes_escogidos.append(lista_ingredientes[1])
                        precio_total = precio_total + precios_ingredientes.get('Champiñiones')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'pi':
                        lista_ingredientes_escogidos.append(lista_ingredientes[2])
                        precio_total = precio_total + precios_ingredientes.get('Pimentón')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'dq':
                        lista_ingredientes_escogidos.append(lista_ingredientes[3])
                        precio_total = precio_total + precios_ingredientes.get('Doble Queso')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'ac':
                        lista_ingredientes_escogidos.append(lista_ingredientes[4])
                        precio_total = precio_total + precios_ingredientes.get('Aceitunas')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'pp':
                        lista_ingredientes_escogidos.append(lista_ingredientes[5])
                        precio_total = precio_total + precios_ingredientes.get('Pepperoni')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'sa':
                        lista_ingredientes_escogidos.append(lista_ingredientes[6])
                        precio_total = precio_total + precios_ingredientes.get('Salchichón')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'q':
                        print()
                        print('Sandwich doble con queso')
                        break
                        
                    else:
                        print('Por favor indique el ingrediente como se le solicita')

            elif eleccion == 'i':
                precio_total = precio_total + precios_tamano.get('Individual')
                eleccion_escogida = 'Individual'

                print('Haz seleccionado el tamaño Individual')

                si_no = 'si'
                while si_no == 'si':
                    print()
                    print('Por favor indique los ingredientes que desee usar')
                    print('Si no desea ninguno solamente presione (q)')
                    print()
                    print('Ingredientes: ')
                    print('Jamón indique (ja)')
                    print('Champiñiones indique (ch)')
                    print('Pimentón indique (pi)')
                    print('Doble Queso indique (dq)')
                    print('Aceitunas indique (ac)')
                    print('Pepperoni indique (pp)')
                    print('Salchichón indique (sa)')

                    eleccion_s = input('Indique su elección: ')
                    eleccion_s = eleccion_s.lower()

                    if eleccion_s == 'ja':
                        lista_ingredientes_escogidos.append(lista_ingredientes[0])
                        precio_total = precio_total + precios_ingredientes.get('Jamon')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'ch':
                        lista_ingredientes_escogidos.append(lista_ingredientes[1])
                        precio_total = precio_total + precios_ingredientes.get('Champiñiones')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'pi':
                        lista_ingredientes_escogidos.append(lista_ingredientes[2])
                        precio_total = precio_total + precios_ingredientes.get('Pimentón')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'dq':
                        lista_ingredientes_escogidos.append(lista_ingredientes[3])
                        precio_total = precio_total + precios_ingredientes.get('Doble Queso')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'ac':
                        lista_ingredientes_escogidos.append(lista_ingredientes[4])
                        precio_total = precio_total + precios_ingredientes.get('Aceitunas')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'pp':
                        lista_ingredientes_escogidos.append(lista_ingredientes[5])
                        precio_total = precio_total + precios_ingredientes.get('Pepperoni')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'sa':
                        lista_ingredientes_escogidos.append(lista_ingredientes[6])
                        precio_total = precio_total + precios_ingredientes.get('Salchichón')

                        si_no = input('¿Desea agregar otro ingrediente si/no: ')

                    elif eleccion_s == 'q':
                        print()
                        print('Sandwich Individual con queso')
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
        print(f'Sandwich número {contador}')
        print(f'Precio total del pedido {precio_total} BsS')
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