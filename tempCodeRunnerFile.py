personaDao = PersonDao.select()
    for person in personaDao:
        print(person)
        logger.debug(person)