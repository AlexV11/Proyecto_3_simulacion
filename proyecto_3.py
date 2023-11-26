import numpy as np

## Esto te simula una cola con su propio server
def unaCola(ini,fin):
    t = ini
    tllega = t + np.random.uniform(5,10)
    tsale = 1000
    nAtendidos = 0
    nClientes = 0
    ingresos = 0
    while t <= fin:
        if tllega < tsale:
            t = tllega
            nClientes += 1
            if nClientes == 1:
                tsale = t + 6
            ingresos += 550
        else:
            t = tsale
            nClientes -= 1
            nAtendidos += 1
            if nClientes == 0:
                tsale = 1000
            else:
                tsale = t + 9
        tllega = t + np.random.uniform(5,10)
    return nAtendidos, ingresos

## Esta es la funcion principal
def ppal(ini,fin):
    print('Simulando tres colas cada una con su propio server...')
    n1, i1 = unaCola(ini,fin)
    n2, i2 = unaCola(ini,fin)
    n3, i3 = unaCola(ini,fin)
    print('El server 1 atendió a '+str(n1)+', generó $'+str(i1)+', el server 2 atendió a '+str(n2)+', generó $'+str(i2)+' clientes y el server 3 atendió a '+str(n3)+', generó $'+str(i3)+' clientes.')
    
## El punto de entrada al programa
if __name__ == '__main__':
    ppal(0,180)