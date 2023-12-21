#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

# uso de tuberias para comunicacion
from multiprocessing import Process, Pipe

# manda vector
def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()

# recibe vector y le suma 100 a cada componente
def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)
    extremo.close()

# PROGRAMA PRINCIPAL

if __name__=="__main__":

    # tuberia con sus extremos
    extremo1,extremo2 = Pipe()

    # instanciar procesos (tanget es la funcion)
    # (args son los argumentos de la funcion)
    proceso1 = Process(target=f, args=(extremo1,))
    proceso2 = Process(target=g, args=(extremo2,))

    # comenzar procesos
    proceso2.start()
    proceso1.start()

    # esperar a que terminen los procesos
    proceso2.join()
    proceso1.join()
