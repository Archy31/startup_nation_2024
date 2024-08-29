from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    email = Column(String(100), nullable=True)
    t_number = Column(String(100), nullable=True)
    password = Column(String(100), unique=True)
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
