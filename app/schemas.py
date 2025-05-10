from typing import Optional

from pydantic import BaseModel


class TodoItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoItemBase):
    pass


class TodoItem(TodoItemBase):
    id: int
