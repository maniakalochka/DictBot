"""Removed primary key tg_id1

Revision ID: 9a218234a75a
Revises: 
Create Date: 2025-01-13 10:12:07.867121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a218234a75a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tg_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('words',
    sa.Column('word', sa.String(), nullable=False),
    sa.Column('level', sa.String(), nullable=False),
    sa.Column('pos', sa.String(), nullable=False),
    sa.Column('definition_url', sa.String(), nullable=True),
    sa.Column('voice_url', sa.String(), nullable=True),
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('is_skipped', sa.Boolean(), nullable=False),
    sa.Column('is_repeatable', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['tg_id'], ['users.tg_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('word')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    op.drop_table('users')
    # ### end Alembic commands ###