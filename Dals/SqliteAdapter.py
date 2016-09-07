import sqlite3
from Consts import Consts
from Objects.TwitterLogger import TwitterLogger

class SqliteAdapter():
    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(Consts.TWITTER_DB_LOCATION)
        except Exception as exc:
            print exc
            #self.logger.ERROR("Didn't succeed to connect to DB, Error occurred:{0}".format(exc))
        else:
            print 'connected'

    def get_cursor(self):
        return self.conn.cursor()