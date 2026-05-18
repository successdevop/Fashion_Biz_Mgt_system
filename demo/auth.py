from demo import auth
from demo.models.user import UserModel
from werkzeug.security import check_password_hash


@auth.verify_password
def verify_password(email, password):
    user = UserModel.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None