from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class City(Base):
    __tablename__ = "city"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    country: Mapped[str] = mapped_column(String(255), nullable=False)
    additional_info: Mapped[str] = mapped_column(String(), nullable=True)
