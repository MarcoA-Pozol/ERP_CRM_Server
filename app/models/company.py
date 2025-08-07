from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Company(Base):
    __tablename__ = "Companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    industry = Column(String, nullable=False)
    size = Column(String, nullable=True, default='medium')
    contact_email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    city = Column(String, index=True)
    employees_count = Column(Integer, nullable=True, default=1)