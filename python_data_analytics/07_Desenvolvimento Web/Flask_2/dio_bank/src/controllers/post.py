# Controllers ou orquestradores das rotas, conduzindo a aplicação para determinados métodos
# Os posts de usuários no blog

from http import HTTPStatus

# Blueprints no Flask
from flask import Blueprint, request
from sqlalchemy import inspect

from src.app import Post, db

app = Blueprint('post', __name__, url_prefix='/posts')


def _create_post():
    data = request.json
    # Campos id e created são adicionados automaticamente pelo db
    post = Post(title=data['title'], body=data['body'], author_id=data['author_id'])
    db.session.add(post)
    db.session.commit()


def _list_posts():
    posts = db.session.execute(db.select(Post)).scalars()
    return [
        {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created': post.created,
            'author_id': post.author_id,
        }
        for post in posts
    ]


# Rota de listagem e criação de blogs
@app.route('/', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'GET':
        return {'Posts': _list_posts()}
    # POST
    else:
        _create_post()
        return {'message': 'Post created'}, HTTPStatus.CREATED


# Rota de requisição de blog
@app.route('/<int:post_id>')
def get_post(post_id):
    post = db.get_or_404(Post, post_id)
    return {
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'created': post.created,
        'author_id': post.author_id,
    }


# Rota de atualização de blog
@app.route('/<int:post_id>', methods=['PATCH'])
def update_post(post_id):
    post = db.get_or_404(Post, post_id)
    data = request.json

    mapper = inspect(Post)
    for column in mapper.attrs:
        if column.key in data:
            setattr(post, column.key, data[column.key])
    db.session.commit()

    return {'message': 'Post patched'}


# Rota de exclusão de blog
@app.route('/<int:post_id>', methods=['DELETE'])
def remove_post(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    return {}, HTTPStatus.NO_CONTENT
