from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, SQLModel

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=120, index=True)
    description: Optional[str] = None
    completed: bool = False

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    created_at: datetime

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = None
    completed: Optional[bool] = None
