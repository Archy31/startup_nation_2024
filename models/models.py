from sqlalchemy import Column, String, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    address = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
    
    