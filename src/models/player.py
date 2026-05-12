from __future__ import annotations

from models.database import Base, registrations
from sqlalchemy import Enum as EnumSQL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from enum import Enum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import Tournament, Matchup

class Gender(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(unique=True)
    address: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    birth_date: Mapped[date] = mapped_column()
    elo: Mapped[int] = mapped_column(default=1200)
    gender: Mapped[Gender] = mapped_column(EnumSQL(Gender, name='gender'), nullable=True, default=None)
    
    tournaments: Mapped[list[Tournament]] = relationship(
        secondary=registrations,
        init=False,
        default_factory=list
    )

    matchups_as_white: Mapped[list[Matchup]] = relationship(
        back_populates='white',
        init=False,
        default_factory=list
    )

    matchups_as_black: Mapped[list[Matchup]] = relationship(
        back_populates='black',
        init=False,
        default_factory=list
    )
