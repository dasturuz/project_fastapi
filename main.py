from db import SessionLocal
from fastapi import FastAPI
# from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session
from models.users import Users
from routes.auth import get_password_hash

from routes import auth, orders, users, customers, product_type, products
from db import Base, engine
import datetime



Base.metadata.create_all(bind=engine)

app=FastAPI(
	title="💻OLX with (SeniorDev)💻",
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get('/')
def home():
	return {"message": "OLX API"}


app.include_router(
	auth.login_router,
	prefix='/auth',
	tags=['User auth section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	users.router_user,
	prefix='/user',
	tags=['User section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	orders.router_order,
	prefix='/orders',
	tags=['Orders Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)
app.include_router(
	customers.router_customer,
	prefix='/customers',
	tags=['Customers Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)
app.include_router(
	product_type.router_productType,
	prefix='/product_types',
	tags=['Product Types Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	products.router_product,
	prefix='/products',
	tags=['Products Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

try:
	db=SessionLocal()
	new_user_db = Users(
		name='Mominjon',
		username='www',
		number='form.number',
		password=get_password_hash('816'),
		roll='www',
		status=True,
	)
	db.add(new_user_db)
	db.commit()
	db.refresh(new_user_db)
except Exception :
	print(Exception)