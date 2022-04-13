from oso import Oso
from sqlalchemy.orm import Session

from myapp.models.user import User


def read_user(id: int, session: Session) -> User:
    user = session.query(User).filter(User.id == id).first()
    return user


def read_all_users(actor: User, oso: Oso):
    return oso.authorized_resources(actor=actor, action="read", resource_cls=User)
