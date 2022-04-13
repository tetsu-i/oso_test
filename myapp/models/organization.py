from myapp.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.orm import backref, relationship


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False, unique=False)

    companies = relationship(
        "Company", lazy="bulk", backref=backref("organization", lazy="bulk")
    )
