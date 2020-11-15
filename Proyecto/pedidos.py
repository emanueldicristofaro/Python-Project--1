# Toda la lógica principal de los pedidos de sandwiches y bebidas.

def pedidoSandwiches(nombre):

    contador = 1
    precio_total = 0
    precios_tamano = {'Triple': 580, 'Doble': 430, 'Individual': 280}
    precios_ingredientes = {'Jamon': 40, 'Champiñiones': 35, 'Pimentón': 30, 'Doble Queso': 40, 'Aceitunas': 57.5
    , 'Pepperoni': 38.5, 'Salchichón': 62.5}

    precios_bebidas = {'Pepsi': 15, 'Coca Cola': 17, 'Frescolita': 14, 'Chinotto': 15}

    option = ''
    while option != '3':
        if option == '1':
            
            print()
            print('Escoja una opción')
            print('Tamaños: Triple ( t ) Doble ( d ) Individual ( i ):')

            eleccion = input('Introduzca su eleccion: ')
            eleccion = eleccion.lower()

            if eleccion == 't':
                precio_total = precio_total + precios_tamano.get('Triple')          
            elif eleccion == 'd':
                precio_total = precio_total + precios_tamano.get('Doble') 
            elif eleccion == 'i':
                precio_total = precio_total + precios_tamano.get('Individual') 
            else:
                print('Por favor debe escoger uno de los tamaños indicados')

        if option == '2':
            print()

        print()
        print(f'Bienvenido a sandwiches GUNS N ROSES {nombre}')
        print()
        print(f'Sandwich número {contador}')
        print(f'Precio total del pedido {precio_total}')
        print()

        print('Sandwiches...')
        print('╔═╦╦╦═╦═╗╔═╗╔═╦═╦═╦═╦═╗')
        print('║║║║║║║╚╣║║║║═║║║╚╣═╣╚╣')
        print('╠╗║║║║╠╗║║║║║╚╣║╠╗║═╬╗║')
        print('╚═╩═╩╩╩═╝╚╩╝╚╩╩═╩═╩═╩═╝')
        print('"Los mejores sandwiches que podrás comer"')

        print()
        option = input('\nMenú de Alimentos\n(1) Sandwich\n(2) Bebidas\n(3) Terminar\nElige una opción:')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    