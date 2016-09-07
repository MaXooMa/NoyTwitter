
from datetime import datetime
from Consts import Consts
from Queries import Queries
from Objects.TwitterLogger import TwitterLogger
from Objects.TwitterPost import TwitterPost
from SqliteAdapter import SqliteAdapter

class PostDAL():
    def __init__(self):
        self.db_adapter = SqliteAdapter()
        self.cur = self.db_adapter.get_cursor()
        #self.logger = TwitterLogger.logging.getLogger('twitter_logger')

    def get_posts(self):
        posts = []
        try:
            results = self.cur.execute(Queries.GET_POSTS_QUERY)
            #self.logger.INFO("Successfully get all posts from the DB")
        except Exception as exc:
            print 'diddnt get blat' + str(exc)
            #self.logger.ERROR("Didn't succeed to get all posts from the DB, Error occurred:{0}".format(exc))
        else:
            for result in results:
                tup = (str(result[Consts.POST_DB_TIME_INDEX]), str(result[Consts.POST_DB_CONTENT_INDEX]))
                posts.append(tup)
        return posts

    def upload_post(self, upload_time, post_content):
        try:
            print Queries.INSERT_POSTS_QUERY % (str(upload_time), post_content)
            self.cur.execute(Queries.INSERT_POSTS_QUERY) % (str(upload_time), post_content)
            print Queries.INSERT_POSTS_QUERY % upload_time, post_content
            print upload_time, post_content
            #self.logger,INFO("New post had arrived to system:{0}".format(post_content))
        except Exception as exc:
            print exc
            #self.logger.ERROR("Didn't succeed to insert new post, Error occurred:{0}".format(exc))



