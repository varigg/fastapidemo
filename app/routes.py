from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db

# from app.models import Todo
from app.schemas import TodoCreate, TodoItem

router = APIRouter()


@router.post("/todos/", response_model=TodoItem, status_code=201)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo_item(db=db, todo_item=todo)


@router.get("/todos/", response_model=List[TodoItem])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    return crud.get_todo_items(db=db, skip=skip, limit=limit)


@router.get("/todos/{todo_id}", response_model=TodoItem)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.get_todo_item(db=db, todo_item_id=todo_id)
