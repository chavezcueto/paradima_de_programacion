#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   enero 2024
#==============================

# las colas (queues) son memorias compartidas entre procesos
from multiprocessing import Process, Queue
def cubico(x,q):
    # poner en la memoria compartidas entre procesos
    q.put((x,x*x*x))

# CODIGO PRINCIPAL
if __name__== "__main__":
    # q es una cola (memoria compartida)
    q = Queue()

    # instanciar una lista de procesos
    procesos = [Process(target=cubico,args=(i,q)) for i in range(1,10)]

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

    # metodo get (les pido a los procesos que me den su resultado enla cola)
    # no nos da el resultado en orden hay que ponerle identificador
    resultado = [q.get() for p in procesos]

    print(resultado)
