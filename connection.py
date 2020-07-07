from logger_base import logger
import psycopg2 as db
import sys


class Connection:

    __DATABASE = "test"
    __USERNAME = "postgres"
    __PASSWORD = "admin123"
    __DB_PORT = "5432"
    __HOST = "127.0.0.1"
    __connection = None
    __cursor = None

    @classmethod
    def getConnection(cls):
        if cls.__connection is None:
            try:
                cls.__connection = db.connect(host=cls.__HOST,
                                              port=cls.__DB_PORT,
                                              user=cls.__USERNAME,
                                              password=cls.__PASSWORD,
                                              database=cls.__DATABASE)

                logger.debug(f'Coneccion Exitosa => {cls.__connection}')
                return cls.__connection
            except Exception as e:
                logger.error(f'Error al conectar a la BD => {e}')
                sys.exit()
        else:
            return cls.__connection

    @classmethod
    def getCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.getConnection().cursor()
                logger.debug(f'Se abrio el cursor con exito => {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al obtener cursor => {e}')
                sys.exit()
        else:
            return cls.__cursor

    @classmethod
    def close(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor.close()
                logger.debug(f'Se cerro el cursor')
            except Exception as e:
                logger.error(f'Error al cerrar cursor => {e}')
        if cls.__connection is None:
            try:
                cls.__connection.close()
                logger.debug(f'Se cerro la conexion')
            except Exception as e:
                logger.error(f'Error al cerrar la conexion')
        logger.debug(f'Se han cerrado los obj de conexion y cursor')


if __name__ == '__main__':
    logger.info(Connetion.getCursor())
    Connetion.close()
