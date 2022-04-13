from myapp.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER as Integer


class UsersCompany(Base):
    __tablename__ = "users_companies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
