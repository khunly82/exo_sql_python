from __future__ import annotations
from models.database import Base, registrations
from enum import Flag, Enum, auto
from sqlalchemy import Enum as EnumSQL, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Player, Matchup

class TournamentStatus(Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    FINISHED = 'FINISHED'

class TournamentCategory(Flag):
    JUNIOR = auto() # 1
    SENIOR = auto() # 2
    VETERAN = auto() # 4

class Tournament(Base):
    __tablename__ = 'tournaments'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column()
    location: Mapped[str] = mapped_column()
    min_players: Mapped[int] = mapped_column()
    max_players: Mapped[int] = mapped_column()
    min_elo: Mapped[int] = mapped_column()
    max_elo: Mapped[int] = mapped_column()
    start_date: Mapped[date] = mapped_column()
    categories: Mapped[int] = mapped_column()
    status: Mapped[TournamentStatus] = mapped_column(EnumSQL(TournamentStatus, name='tournament_status'), default=TournamentStatus.PENDING)
    woman_only: Mapped[bool] = mapped_column(default=False)
    current_round: Mapped[int] = mapped_column(default=0)
    
    players: Mapped[list[Player]] = relationship(
        secondary=registrations, 
        init=False, # remove this property from the initialyser
        default_factory=list
    )

    matchups: Mapped[list[Matchup]] = relationship(
        back_populates='tournament',
        init=False,
        default_factory=list
    )

    __table_args__ = (
        CheckConstraint('min_elo <= max_elo'),
        CheckConstraint('min_players <= max_players'),
    )

