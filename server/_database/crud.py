from datetime import datetime, date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import update
from . import models, schemas, utils
import json


async def create_enterprise(db: sessionmaker, content: schemas.Enterprise):
    db_enterprise = models.Enterprises(**content.dict())
    db.add(db_enterprise)
    db.commit()
    db.refresh(db_enterprise)
    return db_enterprise
async def create_accredited_person(db: sessionmaker, content: schemas.AccreditedPerson):
    db_accredited_person = models.AccreditedPersons(**content.dict())
    db.add(db_accredited_person)
    db.commit()
    db.refresh(db_accredited_person)
    return db_accredited_person
async def create_purchase_request(db: sessionmaker, content: schemas.PurchaseRequestBase):
    db_purchase = models.PurchaseRequests(**content.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase
async def create_budget(db: sessionmaker, content: schemas.BudgetBase):
    db_budget = models.Budgets(**content.dict())
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

# ################################################################################
# # READ
# async def read_user(db: Session, by: str, parameter: str|int|float|date):
#     match by:
#         case 'id':
#             return db.query(models.Users).filter(models.Users.id==parameter).all()
#         case 'email':
#             return db.query(models.Users).filter(models.Users.email==parameter).all()
#         case 'name':
#             return db.query(models.Users).filter(models.Users.name==parameter).all()
#         case 'tag':
#             return db.query(models.Users).filter(models.Users.tag==parameter).all()
#         case 'status':
#             return db.query(models.Users).filter(models.Users.status==parameter).all()
#         case _:
#             return []
#

def get_enterprise_by_id(db: sessionmaker, id: str):
    return db.query(models.Enterprises).filter(models.Enterprises.id==id).first()
def get_purchase_request_by_id(db: sessionmaker, id: int):
    return db.query(models.PurchaseRequests).filter(models.PurchaseRequests.id==id).first()
def get_accredited_person_by_id(db: sessionmaker, id: str):
    return db.query(models.AccreditedPersons).filter(models.AccreditedPersons.id==id).first()

#
# ################################################################################
# # UPSERT
# async def update_user(db: Session, content: schemas.UserUpdate):
#     content_dict = content.dict()
#     if content_dict['password']:
#         content_dict['hashed_password'] = tools.encrypt_pass(content_dict['password'])
#     del content_dict['confirming_password'], content_dict['id'], content_dict['password']
#     content_dict['updated_at'] = datetime.now()
#     content_dict = dict((k, v) for k, v in content_dict.items() if v is not None)
#     db_user = db.query(models.Users).filter(models.Users.id==content.id).update(content_dict, synchronize_session=False)
#     db.commit()
#     return db_user
#
# ################################################################################
# # DELETE
# async def delete_address(db: Session, content: schemas.AddressDelete):
#     db_address = db.query(models.Addressess).filter(models.Addressess.id==content.id).first()
#     db.delete(db_address)
#     db.commit()
#     return []
