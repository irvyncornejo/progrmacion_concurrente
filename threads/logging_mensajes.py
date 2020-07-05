import logging

#Los cinco tipos de mensajes --> Debug(10), Info(20), Warning(30), Error(40) y Critical(50)
#configuración del modulo logging para poder definir que niveles de mesanjes queremos observar
#Podemos colocar desde el mensaje contenido en el logging, nombre de la función, linea de ejecución hasta el thread
logging.basicConfig(
    level=10,
    format='%(asctime)s - %(threadName)s',
    datefmt='%H:%M:%S',
    #filename='message.txt' podemos almacenar los mensajes
)

def mensajes():
    logging.debug('Este es un mensaje de tipo Debug')
    logging.info('Mensaje para info')
    logging.warning('Mensaje de alerta')
    logging.error('Mensaje de Error')
    logging.critical('Mensaje critico')

if __name__ == '__main__':
    mensajes()
