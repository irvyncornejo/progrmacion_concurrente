import threading

def executor_a(id=0):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteración {x}')

def executor_b(id=0):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteración {x}')

def executor_c(id=0):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteración {x}')

thread_a = threading.Thread(target=executor_a, args=['a'])
thread_b = threading.Thread(target=executor_b, args=('b',))
thread_c = threading.Thread(target=executor_c, kwargs={'id':'c'})

thread_a.start()
thread_b.start()
thread_c.start()