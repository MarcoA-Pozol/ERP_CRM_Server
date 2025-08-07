from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Company(Base):
    __tablename__ = 'Companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    industry = Column(String, nullable=False)
    size = Column(String, nullable=True, default='medium')
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False, default='MX')
    address = Column(String, nullable=False)
    employees_count = Column(Integer, nullable=True, default=1)
    is_client = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    contacts = relationship("Contact", back_populates="Companies", cascade="all, delete")

class Contact(Base):
    __tablename__ = 'Contacts'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('Companies.id'), nullable=False, default=1)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False, default='MX')
    address = Column(String, nullable=False)
    age = Column(Integer, nullable=True, default=18)
    gender = Column(String, nullable=False, default='I prefer not to say')  
    is_client = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
