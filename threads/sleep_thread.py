import time
import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)

def task():
    logging.info('Dentro de la una nueva tarea')
    time.sleep(2)
    logging.info('Tarea finalizada')

if __name__ == '__main__':
    thread = threading.Thread(target=task)
    thread.start()