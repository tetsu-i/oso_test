from myapp.database import Base
from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql import expression


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False, unique=False)
    is_admin = Column(
        Boolean, unique=False, nullable=False, server_default=expression.false()
    )

    companies = relationship(
        "Company",
        secondary="users_companies",
        lazy="bulk",
        backref=backref("users", lazy="bulk"),
    )

    organization = relationship(
        "Organization",
        secondary="users_organaizations",
        lazy="bulk",
        backref=backref("users", lazy="bulk"),
    )
