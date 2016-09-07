from Objects.TwitterLogger import TwitterLogger
from Objects.TwitterPost import TwitterPost
from Consts import Consts
from flask import Flask, request
from Dals.PostDAL import PostDAL
import os, datetime

app = Flask(__name__, static_url_path='/static')

"""def main():
    logger = TwitterLogger().logger
    logger.info('Twitter is running')
    if not os.path.isdir(Consts.FOLDER_NAME):
        os.mkdir(Consts.FOLDER_NAME)"""

@app.route('/')
def get_posts():
    post = PostDAL()
    results = post.get_posts()
    return str(results)
    #return app.send_static_file('/html/index.html')


@app.route("/add_post", methods=['POST', 'GET'])
def add_post():
    return app.send_static_file('add_post.html')


@app.route("/post", methods=['POST'])
def post():
    new_post = TwitterPost(datetime.datetime.now(), request.form["post"])
    post_dal = PostDAL().upload_post(new_post.upload_time, new_post.post_content)
    return app.send_static_file('post_uploaded_successfully.html')
    

if __name__ == '__main__':
    app.run(debug=True)

















