from person import Person
from pool_cursor import PoolCursor
from logger_base import logger


class PersonDao:

    '''DAO (Data Access Object) CRUD'''

    __SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERT = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    __UPDATE = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    __DELETE = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT))
            cursor.execute(cls.__SELECT)
            data = cursor.fetchall()
            persons = []
            for item in data:
                person = Person(item[0], item[1], item[2], item[3])
                persons.append(person)
            return persons

    @classmethod
    def insert(cls, person):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            logger.debug(f'Peronsa a insertar => {person}')
            values = (person.get_name(), person.get_lastName(),
                      person.get_email())
            cursor.execute(cls.__INSERT, values)
            return cursor.rowcount

    @classmethod
    def update(cls, person):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.debug(f'Peronsa a actualizar => {person}')
            values = (person.get_name(), person.get_lastName(),
                      person.get_email(), person.get_id_person())
            cursor.execute(cls.__UPDATE, values)
            return cursor.rowcount

    @classmethod
    def delete(cls, person):
        with PoolCursor() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.debug(f'Persona a eliminar => {person}')
            values = (person.get_id_person(),)
            cursor.execute(cls.__DELETE, values)
            return cursor.rowcount


if __name__ == '__main__':
    # select all
    personaDao = PersonDao.select()
    for person in personaDao:
        print(person)
        logger.debug(person)

    # insert
    # person = Person(name='Antonio', lastName='Najera', email='pnajera@mail.com')
    # data_insert = PersonDao.insert(person)
    # logger.debug(f'registros insertados => {data_insert}')

    # Actualizar un registro existente
    # persona = Person(1,'Juan','Perez', 'jperez@mail.com')
    # personas_actualizadas = PersonDao.update(persona)
    # logger.debug(f'Personas actualizadas: {personas_actualizadas}')

    # eliminar un registro existente
    # persona = Person(id_person=1)
    # personas_eliminadas = PersonDao.delete(persona)
    # logger.debug(f'Personas eliminadas: {personas_eliminadas}')
