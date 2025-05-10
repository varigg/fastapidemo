from loguru import logger
from sqlalchemy.orm import Session

from . import models, schemas


# Create a TodoItem
def create_todo_item(db: Session, todo_item: schemas.TodoItemBase):
    logger.debug(f"Creating TodoItem with title: {todo_item.title}")
    db_todo_item = models.TodoItem(**todo_item.model_dump())
    db.add(db_todo_item)
    db.commit()
    db.refresh(db_todo_item)
    return db_todo_item


# Read all TodoItems
def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()


# Read a TodoItem by ID
def get_todo_item(db: Session, todo_item_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.id == todo_item_id).first()
