from logger_base import logger


class Person:

    def __init__(self, id_person=None, name=None, lastName=None, email=None):
        self.__id_person = id_person
        self.__name = name
        self.__lastName = lastName
        self.__email = email

    def __str__(self):
        return (
            f' Id Person: {self.__id_person},'
            f' Name: {self.__name},'
            f' Last Name: {self.__lastName},'
            f' Email: {self.__email}'
        )

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_id_person(self):
        return self.__id_person

    def set_id_person(self, id_person):
        self.__id_person = id_person


if __name__ == '__main__':
    # person = Person(1, 'Dilan', 'Atondo', 'DilanAtondo@gmail.com')
    # logger.debug(person)
    persona2 = Person(name='Karla', lastName='Gomez',email= 'kgomez@mail.com')
    logger.debug(persona2)
