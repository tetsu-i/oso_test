from myapp.database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER as Integer


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False, unique=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
