from logger_base import logger
from psycopg2 import pool
import sys


class Connection:

    __DATABASE = "test"
    __USERNAME = "postgres"
    __PASSWORD = "admin123"
    __DB_PORT = "5432"
    __HOST = "127.0.0.1"
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def getPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON,
                                                       cls.__MAX_CON,
                                                       host=cls.__HOST,
                                                       port=cls.__DB_PORT,
                                                       user=cls.__USERNAME,
                                                       password=cls.__PASSWORD,
                                                       database=cls.__DATABASE)
                logger.debug(f'Creacion de pool exitosa')
                return cls.__pool
            except Exception as e:
                logger.error(f'Error al crear el pool de conexiones => {e}')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def getConnection(cls):
        # get pool connection 
        connection = cls.getPool().getconn()
        logger.debug(f'Conexion obtenida de pool => {connection}')
        return connection

    @classmethod
    def liberateConnection(cls, connection):
        # return obj pool connection
        cls.getPool().putconn(connection)
        logger.debug(f'Regresamos la coneccion al pool')
        logger.debug(f'Estado del pool => {cls.__pool}')
        

    @classmethod
    def closeConnections(cls):
        # Close pool and connecctions 
        cls.getPool().closeall()
        logger.debug(f'Cerramos todas las conecciones')
        


if __name__ == '__main__':
    # get pool connection
    connection = Connection.getConnection()
    Connection.liberateConnection(connection)
    Connection.closeConnections()