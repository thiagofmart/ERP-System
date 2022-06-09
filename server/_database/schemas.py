from pydantic import BaseModel
from typing import List
from datetime import date


class Email(BaseModel):
    email: str
    password: str
    assign: str

class Enterprise(BaseModel):
    id: str
    formal_name: str
    informal_name: str
    address: str
    number: str
    complement: str
    district: str
    city: str
    county: str
    postal_code: str
    country: str
    phone: str
    site: str
    main_email: str
    purchase_email: Email
    bill_receiver_email: str
    bill_sender_email: Email
    financial_email: Email
    additional_content: dict
    logo: str

    class Config:
        orm_mode = True

class AccreditedPerson(BaseModel):
    id: str
    informal_name: str
    formal_name: str
    address: str
    number: str
    complement: str
    district: str
    city: str
    county: str
    postal_code: str
    country: str
    phone: str
    site: str
    main_email: str
    budget_email_receivers: str
    purchase_request_email_receivers: str
    bill_email_receivers: str
    additional_content: dict

    class Config:
        orm_mode = True

class Item(BaseModel):
    description: str
    quantity: float
    unity: str
    unitary: float
    total: float
### Budgets ####################################
class ItemBudget(Item):
    _type: str

class BudgetBase(BaseModel):
    client_id: str
    estimator: str
    cetegory: str
    description: str
    manpower: bool
    items: List[ItemBudget]
    validity: date
    payment_terms: str
    bdi: float    
    
class Budget(BudgetBase):
    id: int
    created_at: date
    class Config:
        orm_mode = True

### Purchases #################################
class PurchaseRequestBase(BaseModel):
    requester: str
    budget_id: int
    provider_id: int
    _type: str
    items: List[Item]
    payment_terms: str
    
class PurchaseRequest(PurchaseRequestBase):
    id: int

### Bill ######################################