import logging


class TwitterLogger:
    def __init__(self):
        self.logger = logging.getLogger('twitter_logger')
        file_handler = logging.FileHandler(r'C:\Users\MainLaptop\Desktop\a.txt')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)
