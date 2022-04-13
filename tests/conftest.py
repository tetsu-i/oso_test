import pytest
from myapp.authorizer import build_oso
from myapp.database import SessionForOso, UnauthSession
from sqlalchemy.orm import Session


@pytest.fixture
def get_unauth_db():
    session: Session = UnauthSession()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def get_read_db():
    session: Session = SessionForOso()
    yield session
    session.close()


@pytest.fixture
def get_oso(get_read_db: Session):
    _oso = build_oso()(get_read_db)
    return _oso
