from curses.ascii import HT
from ._database import schemas, crud, utils
from sqlalchemy.orm import sessionmaker
from datetime import date
from . import tools
from fastapi import FastAPI, Depends, HTTPException

#uvicorn server.__main__:app --relaod
app = FastAPI()
utils._create_database()


##############################################################
@app.post('/api/v1/enterprise/create', response_model=schemas.Enterprise)
async def create_enterprise(payload: schemas.Enterprise, db: sessionmaker=Depends(utils.get_db_write)):
    db_enterprise = crud.get_enterprise_by_id(db=db, id=payload.id)
    if db_enterprise:
        raise HTTPException(status_code=404, detail=f'Enterprise with id "{payload.id} already exists!"')
    db_enterprise = await crud.create_enterprise(db=db, content=payload)
    return db_enterprise
@app.post('/api/v1/accredited_person/create', response_model=schemas.AccreditedPerson)
async def create_accredited_person(payload: schemas.AccreditedPerson, db: sessionmaker=Depends(utils.get_db_write)):
    db_accredited_person = crud.get_accredited_person_by_id(db=db, id=payload.id)
    if db_accredited_person:
        raise HTTPException(status_code=404, detail=f'Accredited Person with id "{payload.id} already exists!"')
    db_accredited_person = await crud.create_accredited_person(db=db, content=payload)
    return db_accredited_person
##############################################################
@app.post("/api/v1/budget/create", response_model=schemas.Budget)
async def create_budget(payload: schemas.BudgetBase, db: sessionmaker=Depends(utils.get_db_write)):
    ### VALIDATION BLOCK ###
    db_client = crud.get_accredited_person_by_id(db=db, id=payload.client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail=f"Client with ID {payload.client_id} not found")
    ### VALIDATION APPROVED ###
    db_budget = await crud.create_budget(db=db, content=payload)
    return db_budget
@app.post("/api/v1/budget/send")
async def send_budget(payload: schemas.Budget):
    return
##############################################################

@app.post("/api/v1/purchase_request/create", response_model=schemas.PurchaseRequest)
async def create_purchase_request(purchaserequest: schemas.PurchaseRequestBase, db: sessionmaker=Depends(utils.get_db_write)):
    db_provider = crud.get_provider_by_id(purchaserequest.provider_id)
    if not db_provider:
        raise HTTPException(status_code=404, detail='provider not found')
    db_purchase_request = await crud.create_purchase_request(db=db, content=purchaserequest)
    if not db_purchase_request:
        raise HTTPException(status_code=404, detail='purchase request not found')
    ## APPROVED VALIDATION!
    return db_purchase_request
@app.post("/api/v1/purchase_request/send")
async def send_purchase_request(purchase_request_id: int, db: sessionmaker=Depends(utils.get_db_read)):
    db_pedido_compra = crud.get_purchase_request_by_id(db, purchase_request_id)
    if not db_pedido_compra:
        print('Nº de pedido de compra inválido!')
        return None
    fornecedor_data = tools.get_fornecedor(db_pedido_compra.cnpj_cpf_fornecedor)
    if not fornecedor_data:
        print('Fornecedor não cadastrado')
        return None
    tools.enviar_email_pedido_compra(email_conn, empresa, db_pedido_compra, fornecedor_data, obs)
    print('E-mail enviado!')
    return {'none':'none'}
@app.post("/api/v1/purchase/save_invoice")
async def save_invoice(invoice_xml):
    return {'none':'none'}

##############################################################
@app.post("/api/v1/operational/service/create_order")
async def create_service_order():
    return {'none':'none'}
@app.post("/api/v1/operational/service/execute")
async def execute_service():
    return {'none':'none'}
@app.post("/api/v1/operational/service/report")
async def report_service():
    return {'none':'none'}
###############################################################
@app.post("/api/v1/bill/create")
async def create_bill():
    return {'none':'none'}
@app.post("/api/v1/bill/send")
async def send_bill():
    return {'none':'none'}
###############################################################        


