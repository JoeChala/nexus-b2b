from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PG_UUID,primary_key=True,nullable=False,unique=True,default=uuid4)

    password_hash: Mapped[str] = mapped_column(String(255),nullable=False,unique=False)

    email: Mapped[str] = mapped_column(String(80),nullable=False,unique=False)

    display_name: Mapped[str] = mapped_column(String(20),nullable=False,unique=False)

    is_active: Mapped[bool] = mapped_column(Boolean,default=True,nullable=False,unique=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False,unique=False)

    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),onupdate=True,nullable=False,unique=False)
