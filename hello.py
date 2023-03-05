import logging


logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', datefmt='%d.%m.%Y %H:%M:%S',
                    filename='example.log', encoding='utf-8', level=logging.INFO)

logging.info('We are running')
print("Hello, world!")
logging.warning("That's all, kids. We are done")
