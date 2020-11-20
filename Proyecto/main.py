import pedidos
import banco

# Proyecto #1
# Integrantes:
# Emanuel Di Cristofaro Esposito
# Aaron Perez Pereira
# Boris Torrado Hernandez

# En este módulo presenta el menú principal del sistema
# Registro de nuevos clientes, mostrar los mismos, ver info de la tarjeta, iniciar sesión y cerrar el sistema.

clients = {}
option = ''
while option != '5':
    if option == '1':
        #Registro de nuevos clientes.
        nif = input('Por favor indique su cédula: ')
        name = input('Por favor indique su nombre completo: ')
        address = input('Indique su dirección: ')
        phone = input('Indique su número telefónico: ')
        email = input('Indique su correo electrónico: ')
        client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email}
        clients[nif] = client

    if option == '2':
        #Buscar los clientes registrados.
        nif = input('Por favor indique su cédula: ')
        if nif in clients:
            print()
            print('NIF:', nif)
            for key, value in clients[nif].items():
                print(key.title() + ':', value)
        else:
            print('No se encuentra registrado en el sistema')

    if option == '3':
        # Mostrar información de una tarjeta del cliente registrado.
        nif = input('Por favor indique su cédula: ')
        eleccion = input('Indique el tipo de tarjeta (Débito (deb) o Crédito (cre)): ')
        eleccion = eleccion.lower()
        
        if eleccion == 'deb':
            banco.encontrarDebito(nif)
        elif eleccion == 'cre':
            banco.encontrarCredito(nif)
        else:
            print('Por favor indicar lo solicitado')

    if option == '4':
        #Para poder acceder al sistema de pedidos.
        nif = input('Por favor indique su cédula: ')

        if nif in clients:
            nombre = clients[nif].get('nombre')
            pedidos.pedidoSandwiches(nombre)
            option = '5'
        else:
            print('La cedula introducida no se encuentra en el sistema')

    print()
    print('Bienvenidos a la tienda de Sandwiches rockeros GUNS N ROSES, desde acá podrá pedir los sandwiches más')
    print('suculentos. Antes de continuar es necesario que se registe en el sistema o inicie sesión:')

    print()
    print('Sandwiches...')
    print('╔═╦╦╦═╦═╗╔═╗╔═╦═╦═╦═╦═╗')
    print('║║║║║║║╚╣║║║║═║║║╚╣═╣╚╣')
    print('╠╗║║║║╠╗║║║║║╚╣║╠╗║═╬╗║')
    print('╚═╩═╩╩╩═╝╚╩╝╚╩╩═╩═╩═╩═╝')
    print('"Los mejores sandwiches que podrás comer"')

    print()

    option = input('\nMenú de opciones\n(1) Registrarse\n(2) Información del cliente\n(3) Ver información de la tarjeta\n(4) Iniciar sesión\n(5) Terminar\nElige una opción:')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
