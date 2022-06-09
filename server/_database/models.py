from datetime import datetime, date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Date, PickleType, LargeBinary, SmallInteger
from sqlalchemy.types import JSON
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from .database import Base


class Enterprises(Base):
    __tablename__ = 'enterprises'
    id = Column(String, primary_key=True, index=True)
    formal_name = Column(String)
    informal_name = Column(String)#
    address = Column(String)
    number = Column(String)
    complement = Column(String)
    district = Column(String)
    city = Column(String)
    county = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    site = Column(String)
    main_email = Column(String)
    purchase_email = Column(PickleType)
    bill_receiver_email = Column(String)
    bill_sender_email = Column(PickleType)
    financial_email = Column(PickleType)
    additional_content = Column(JSON)
    logo = Column(String) #LARGE BINARY


class AccreditedPersons(Base):
    __tablename__ = 'accreditedpersons'
    id = Column(String, primary_key=True)
    informal_name = Column(String)
    formal_name = Column(String)
    address = Column(String)
    number = Column(String)
    complement = Column(String)
    district = Column(String)
    city = Column(String)
    county = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    site = Column(String)
    main_email = Column(String)
    budget_email_receivers = Column(String)
    purchase_request_email_receivers = Column(String)
    bill_email_receivers = Column(String)
    additional_content = Column(JSON)

    budgets = relationship('Budgets', backref='accreditedpersons')
    purchase_requests = relationship('PurchaseRequests', backref='accreditedpersons')

class Budgets(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('accreditedpersons.id'))
    estimator = Column(String)
    cetegory = Column(Integer)
    description = Column(String)
    manpower = Column(Boolean)
    items = Column(PickleType)
    validity = Column(Date)
    payment_terms = Column(String)
    bdi = Column(Float)
    created_at = Column(Date, default=date.today())
    

class PurchaseRequests(Base):
    __tablename__='purchaserequests'
    id = Column(Integer, primary_key=True, index=True)
    enterprise_id = Column(Integer, ForeignKey('enterprises.id'))
    requester = Column(String(200))
    budget_id = Column(Integer, ForeignKey('budgets.id'))
    provider_id = Column(Integer, ForeignKey('accreditedpersons.id'))
    _type = Column(String(200))
    payment_terms = Column(String(200))
    items = Column(PickleType)
    created_at = Column(Date, default=date.today())




