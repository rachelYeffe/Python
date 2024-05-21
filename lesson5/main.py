import logging
def logger(mesag):
    def y(func):
        def wrapper():
            logging.basicConfig(level=logging.DEBUG)
            file_handler=logging.FileHandler('text.txt')
            func()
            logger = logging.getLogger()
            logger.addHandler(file_handler)
            logger.debug(mesag)
        return wrapper
    return y
@logger("hello")
def f():
    print("func")
f()
