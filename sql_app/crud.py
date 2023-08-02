#!/usr/bin/env python3
#Enable type definition of the `db` parameters
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Item, User
from schemas import ItemCreate, UserCreate


def get_user(db: Session, user_id: int):
    return db.get(User, user_id)

def get_user_by_email(db: Session, email: str):
    return db.execute(select(User).filter_by(email=email)).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.execute(select(User).offset(skip).limit(limit)).scalars().all()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = f'{user.password}notreallyhashed'
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.execute(select(Item).offset(skip).limit(limit)).scalars().all()

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

