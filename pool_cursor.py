from connection import Connection
from logger_base import logger


class PoolCursor:

    def __init__(self):
        self.__conn = None
        self.__cursor = None

    # start with
    def __enter__(self):
        self.__conn = Connection.getConnection()
        self.__cursor = self.__conn.cursor()
        logger.debug(f'Inicio del metodo With {self.__conn}')
        return self.__cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug('Se ejecuta el metodo exit()')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrio una Excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit de la trancsaccion')
        self.__cursor.close()
        Connection.liberateConnection(self.__conn)
        
        
if __name__ == '__main__':
    # Get cursor by the pool connection
    with PoolCursor() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug(cursor.fetchall())
