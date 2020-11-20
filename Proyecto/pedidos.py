import banco

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
            print('Tamaños: Triple ( t ) Precio: 580 BsS, Doble ( d ) Precio: 430 BsS, Individual ( i ) Precio: 280 BsS:')

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

                print('Jamón indique (ja) Precio: 40 BsS')
                print('Champiñiones indique (ch) Precio: 35 BsS')
                print('Pimentón indique (pi) Precio: 30 BsS')
                print('Doble Queso indique (dq) Precio: 40 BsS')
                print('Aceitunas indique (ac) Precio: 57.5 BsS')
                print('Pepperoni indique (pp) Precio: 38.5 BsS')
                print('Salchichón indique (sa) Precio: 62.5 BsS')
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
                        if lista_ingredientes_escogidos:
                            print('Usted seleccionó un sandwich ' + eleccion_escogida , end=' '),
                            print('con ', end='')
                            for ingerdiente in lista_ingredientes_escogidos:
                                print(ingerdiente, end=", ")
                        else: 
                            print('Usted seleccionó un sandwich ' + eleccion_escogida + ' con Queso', end=' '),
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

                print('Jamón indique (ja) Precio: 40 BsS')
                print('Champiñiones indique (ch) Precio: 35 BsS')
                print('Pimentón indique (pi) Precio: 30 BsS')
                print('Doble Queso indique (dq) Precio: 40 BsS')
                print('Aceitunas indique (ac) Precio: 57.5 BsS')
                print('Pepperoni indique (pp) Precio: 38.5 BsS')
                print('Salchichón indique (sa) Precio: 62.5 BsS')
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
                        if lista_ingredientes_escogidos:
                            print('Usted seleccionó un sandwich ' + eleccion_escogida , end=' '),
                            print('con ', end='')
                            for ingerdiente in lista_ingredientes_escogidos:
                                print(ingerdiente, end=", ")
                        else: 
                            print('Usted seleccionó un sandwich ' + eleccion_escogida + ' con Queso', end=' '),
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

                print('Jamón indique (ja) Precio: 40 BsS')
                print('Champiñiones indique (ch) Precio: 35 BsS')
                print('Pimentón indique (pi) Precio: 30 BsS')
                print('Doble Queso indique (dq) Precio: 40 BsS')
                print('Aceitunas indique (ac) Precio: 57.5 BsS')
                print('Pepperoni indique (pp) Precio: 38.5 BsS')
                print('Salchichón indique (sa) Precio: 62.5 BsS')
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
                        if lista_ingredientes_escogidos:
                            print('Usted seleccionó un sandwich ' + eleccion_escogida , end=' '),
                            print('con ', end='')
                            for ingerdiente in lista_ingredientes_escogidos:
                                print(ingerdiente, end=", ")
                        else: 
                            print('Usted seleccionó un sandwich ' + eleccion_escogida + ' con Queso', end=' '),
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
            print('Escoja una opción')
            print('Bebidas: Pepsi (pe) Precio: 15 BsS, Coca Cola (co) Precio: 17 BsS, Frescolita (fres) Precio: 14 BsS, Chinotto (chi) Precio: 15 BsS')

            eleccion_b = input('Introduzca su eleccion: ')
            eleccion_b = eleccion_b.lower()

            if eleccion_b == 'pe':
                print('Usted a escogido Pepsi')
                precio_total = precio_total + precios_bebidas.get('Pepsi')
                lista_bebidas_escogidas.append(lista_bebidas[0])

            elif eleccion_b == 'co':
                print('Usted a escogido Coca Cola')
                precio_total = precio_total + precios_bebidas.get('Coca Cola')
                lista_bebidas_escogidas.append(lista_bebidas[1])

            elif eleccion_b == 'fres':
                print('Usted a escogido Frescolita')
                precio_total = precio_total + precios_bebidas.get('Frescolita')
                lista_bebidas_escogidas.append(lista_bebidas[2])

            elif eleccion_b == 'chi':
                print('Usted a escogido Chinotto')
                precio_total = precio_total + precios_bebidas.get('Chinotto')
                lista_bebidas_escogidas.append(lista_bebidas[3])

            else:
                print('Por favor debe escoger una de las bebidas indicadas') 

        if option == '3':

            print()
            print(f'Precio total a pagar {precio_total}')
            print()
            metodo_de_pago = input('Por favor seleccione el método de pago (Débito (deb) o Crédito (cre)): ')
            metodo_de_pago = metodo_de_pago.lower()

            if metodo_de_pago == 'deb':

                nif = input('Por favor indique su cédula: ')
                tarjeta = banco.metodoPagoDebito(nif)
                monto = tarjeta.get('montoTarjeta')

                print()
                print(f'El monto de la tarjeta de débito es de: {monto}')

                if monto < precio_total:
                    print('Lo siento no cuenta con suficiente saldo')
                else:
                    si_no_pp = input('¿Desea efectuar el pago? si/no: ')
                    si_no_pp = si_no_pp.lower()

                    if si_no_pp == 'si':
                        print('Gracias por su compra, regrese pronto')
                        banco.descontarDebito(precio_total, nif)
                        eleccion_escogida = ''
                        precio_total = 0
                        lista_ingredientes_escogidos.clear()
                        lista_bebidas_escogidas.clear()
                        
                    elif si_no_pp == 'no':
                        print('Lamentamos que su pedido no haya sido de su agrado, puede volver a intentarlo')
                        eleccion_escogida = ''
                        precio_total = 0
                        lista_ingredientes_escogidos.clear()
                        lista_bebidas_escogidas.clear()

                    else:
                        print('Por favor indicar si/no')

            elif metodo_de_pago == 'cre':

                nif = input('Por favor indique su cédula: ')
                tarjeta = banco.metodoPagoCredito(nif)
                monto = tarjeta.get('montoTarjeta')

                print()
                print(f'El monto de la tarjeta de crédito es de: {monto}')

                if monto < precio_total:
                    print('Lo siento no cuenta con suficiente saldo')
                else:
                    si_no_pp = input('¿Desea efectuar el pago? si/no: ')
                    si_no_pp = si_no_pp.lower()

                    if si_no_pp == 'si':
                        print('Gracias por su compra, regrese pronto')
                        banco.descontarCredito(precio_total, nif)
                        eleccion_escogida = ''
                        precio_total = 0
                        lista_ingredientes_escogidos.clear()
                        lista_bebidas_escogidas.clear()
                        
                    elif si_no_pp == 'no':
                        print('Lamentamos que su pedido no haya sido de su agrado, puede volver a intentarlo')
                        eleccion_escogida = ''
                        precio_total = 0
                        lista_ingredientes_escogidos.clear()
                        lista_bebidas_escogidas.clear()

                    else:
                        print('Por favor indicar si/no')
            
            else:
                print('Por favor indicar lo solicitado')

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