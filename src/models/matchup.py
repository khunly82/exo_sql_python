from __future__ import annotations
from typing import TYPE_CHECKING
from models.database import Base
from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as EnumSQL, ForeignKey
if TYPE_CHECKING:
    from models import Player, Tournament

class MatchupResult(Enum):
    NOT_SET = 'NOT_SET'
    WHITE_WIN = 'WHITE_WIN' 
    BLACK_WIN = 'BLACK_WIN'
    DRAW  = 'DRAW'

class Matchup(Base):
    __tablename__ = 'matchups'
    id: Mapped[int] = mapped_column(primary_key=True)
    tournament_id: Mapped[int] = mapped_column(ForeignKey('tournaments.id'))
    white_id: Mapped[int] = mapped_column(ForeignKey('players.id'))
    black_id: Mapped[int] = mapped_column(ForeignKey('players.id'))
    result: Mapped[MatchupResult] = mapped_column(
        EnumSQL(MatchupResult, name='matchup_result'), 
        default=MatchupResult.NOT_SET
    )
    tournament: Mapped[Tournament] = relationship(back_populates='matchups', init=False)
    white: Mapped[Player] = relationship(
        foreign_keys=['white_id'], 
        back_populates='matchups_as_white', 
        init=False
    )
    black: Mapped[Player] = relationship(
        foreign_keys=['black_id'], 
        back_populates='matchups_as_black', 
        init=False
    )
