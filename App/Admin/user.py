from flask import Blueprint


user = Blueprint('user', __name__)

@user.route('/user')
def users():
    return "Essa é minha página de usuários!"