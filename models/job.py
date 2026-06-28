from sqlalchemy import Column,Integer,String,Enum,ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer,primary_key = True,index = True)
    title = Column(String,nullable = False)
    description = Column(Integer)
    salary = Column(Integer)
    company_id = Column(Integer,ForeignKey("companies:id"))
    companies = relationship("Company",back_populates ="jobs")