"""auto-vote

Revision ID: 20214f3d9f49
Revises: fed5b1ab950b
Create Date: 2024-07-27 22:11:58.389852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20214f3d9f49'
down_revision: Union[str, None] = 'fed5b1ab950b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id',sa.Integer(),nullable=False),
    sa.Column('post_id', sa.Integer(),nullable=False),
    sa.ForeignKeyConstraint(['post_id'],['posts.id'],ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id','post_id'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   op.drop_table('votes')
    # ### end Alembic commands ###
