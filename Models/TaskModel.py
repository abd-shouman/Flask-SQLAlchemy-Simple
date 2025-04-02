from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class TaskModel(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(30))
    done: Mapped[Optional[bool]] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, text={self.text!r}, done={self.done!r})"


