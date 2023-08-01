#!/usr/bin/env python3
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from database import SessionLocal, engine
import models
import schemas
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db, user)

@app.get('/users/', response_model=list[schemas.User])
def read_users(
        *,
        skip: int = 0,
        limit: int = 100,
        db: Annotated[Session, Depends(get_db)]):
    users = crud.get_users(db, skip=skip, limit=limit)
    print(type(users[0]))
    return users

