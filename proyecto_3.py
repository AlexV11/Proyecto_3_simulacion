import numpy as np

## Esto te simula una cola con su propio server
def unaCola(ini,fin, tllega_min, tllega_max, tsale_min, tsale_max, ingreso_cliente):
    t = ini
    tllega = t + np.random.uniform(tllega_min, tllega_max)
    tsale = 1000
    nAtendidos = 0
    nClientes = 0
    while t <= fin:
        if tllega < tsale:
            t = tllega
            nClientes += 1
            if nClientes == 1:
                tsale = t + np.random.randint(tsale_min, tsale_max)
        else:
            t = tsale
            nClientes -= 1
            nAtendidos += 1
            if nClientes == 0:
                tsale = 1000
            else:
                tsale = t + np.random.randint(tsale_min, tsale_max)
        tllega = t + np.random.uniform(tllega_min, tllega_max)
    return nAtendidos, nClientes, ingreso_cliente * nAtendidos

## Esta es la funcion principal
def ppal(ini,fin):
    print('Simulando tres colas cada una con su propio server...')
    n1, nc1, i1 = unaCola(ini,fin, 5, 10, 4, 6, 550)
    n2, nc2, i2 = unaCola(ini,fin, 5, 10, 9, 10, 400)
    n3, nc3, i3 = unaCola(ini,fin, 8, 12, 10, 12, 560)
    print('El server 1 atendió a '+str(n1)+', el server 2 atendió a '+str(n2)+' clientes y el server 3 atendió a '+str(n3)+' clientes.')
    print('El server 1 generó $'+str(i1)+', el server 2 generó $'+str(i2)+' y el server 3 generó $'+str(i3)+'.')

## El punto de entrada al programa
if __name__ == '__main__':
    ppal(0,180)
