from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return {'msg': 'Hello Flask'}


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post ID {post_id}'


@app.route('/post/<float:post_score>')
def show_float(post_score):
    # show the post with the given id, the id is an integer
    return f'Post Score {post_score}'


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath


@app.route('/uuid/<uuid:uuid>')
def show_uuid(uuid):
    # show the uuid after /uuid/
    return f'uuid {uuid}'


if __name__ == '__main__':
    app.run()