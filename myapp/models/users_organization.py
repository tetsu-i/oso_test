from myapp.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER as Integer


class UsersOrganization(Base):
    __tablename__ = "users_organaizations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
