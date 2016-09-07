import Consts


class Queries():
    GET_POSTS_QUERY = """select * from Posts"""
    INSERT_POSTS_QUERY = """INSERT INTO posts (id, creation_time, content) VALUES (NULL, '%s', '%s')"""