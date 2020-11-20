import random

listas_tarjetas_debito = {}
listas_tarjetas_credito = {}

# En este modulo se efectua todas las transacciones bancarias (Las tarjetas)

def metodoPagoDebito(nif):
    print()

    if nif not in listas_tarjetas_debito:
        nombre_tarjeta = input('Por favor indique el nombre de su tarjeta de débito: ')
        numero_tarjeta = int(input('Por favor indique su numero de su tarjeta de débito: '))
        monto_tarjeta = round(random.uniform(5000, 10000), 2)

        lista_tarjeta = {'nombreTarjeta': nombre_tarjeta, 'numeroTarjeta': numero_tarjeta, 'montoTarjeta': monto_tarjeta}
        listas_tarjetas_debito[nif] = lista_tarjeta

        return lista_tarjeta

    else:
        print('Usted ya posee una tarjeta de débito registrada en el sistema')
        lista_tarjeta = listas_tarjetas_debito[nif]

        return lista_tarjeta

def metodoPagoCredito(nif):
    print()

    if nif not in listas_tarjetas_credito:
        nombre_tarjeta = input('Por favor indique el nombre de su tarjeta de crédito: ')
        numero_tarjeta = int(input('Por favor indique su numero de su tarjeta de crédito: '))
        monto_tarjeta = round(random.uniform(5000, 10000), 2)
    
        lista_tarjeta = {'nombreTarjeta': nombre_tarjeta, 'numeroTarjeta': numero_tarjeta, 'montoTarjeta': monto_tarjeta}
        listas_tarjetas_credito[nif] = lista_tarjeta

        return lista_tarjeta

    else:
        print('Usted ya posee una tarjeta de crédito registrada en el sistema')
        lista_tarjeta = listas_tarjetas_credito[nif]

        return lista_tarjeta

def descontarDebito(precio_total, nif):
    print()

    lista =  listas_tarjetas_debito[nif]
    monto = lista.get('montoTarjeta')
    monto_nuevo = monto - precio_total
    lista['montoTarjeta'] = monto_nuevo 

def descontarCredito(precio_total, nif):
    print()

    lista =  listas_tarjetas_credito[nif]
    monto = lista.get('montoTarjeta')
    monto_nuevo = monto - precio_total
    lista['montoTarjeta'] = monto_nuevo 

def encontrarDebito(nif):
    print()

    if nif in listas_tarjetas_debito:
        print()
        print('NIF:', nif)
        for key, value in listas_tarjetas_debito[nif].items():
            print(key.title() + ':', value)
    else:
        print('No se encuentra la tarjeta de débito en el sistema')

def encontrarCredito(nif):
    print()

    if nif in listas_tarjetas_credito:
        print()
        print('NIF:', nif)
        for key, value in listas_tarjetas_credito[nif].items():
            print(key.title() + ':', value)
    else:
        print('No se encuentra la tarjeta de crédito en el sistema')