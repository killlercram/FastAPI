"""adding content column to posts table

Revision ID: 273bfe53efd6
Revises: a882619313ec
Create Date: 2024-07-26 23:28:17.339095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '273bfe53efd6'
down_revision: Union[str, None] = 'a882619313ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
