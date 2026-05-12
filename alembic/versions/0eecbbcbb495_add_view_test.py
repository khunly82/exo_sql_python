"""add view test

Revision ID: 0eecbbcbb495
Revises: c14cb0e9d375
Create Date: 2026-05-12 16:36:45.747523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0eecbbcbb495'
down_revision: Union[str, Sequence[str], None] = 'c14cb0e9d375'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('CREATE VIEW my_view AS SELECT * FROM players')


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('DROP VIEW my_view')
