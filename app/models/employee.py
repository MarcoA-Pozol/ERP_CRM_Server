from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
from . occupation import Occupation 
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    age = Column(Integer, nullable=True, default=18)
    gender = Column(String, nullable=False, default="Other")  
    occupation_id = Column(Integer, ForeignKey("occupations.id"), nullable=False)
    occupation = relationship("Occupation", back_populates="employees") # For ORM
    salary_per_month = Column(Numeric(10, 2), nullable=False, default=800.00)  
    is_admin = Column(Boolean, nullable=False, default=False)  
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
