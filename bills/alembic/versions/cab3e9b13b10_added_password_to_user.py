"""added password to User

Revision ID: cab3e9b13b10
Revises: 53f837963885
Create Date: 2025-02-26 10:52:12.528933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'cab3e9b13b10'
down_revision: Union[str, None] = '53f837963885'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bills')
    op.drop_index('email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('username', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'users', ['username'], unique=True)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('email', 'users', ['email'], unique=True)
    op.create_table('bills',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('bill_type', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('amount', mysql.FLOAT(), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('paid', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='bills_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
