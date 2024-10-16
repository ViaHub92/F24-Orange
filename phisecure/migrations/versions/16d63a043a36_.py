"""empty message

Revision ID: 16d63a043a36
Revises: 
Create Date: 2024-10-09 18:58:09.611584

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '16d63a043a36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('templates', schema=None) as batch_op:
        batch_op.drop_index('ix_templates_name')

    op.drop_table('templates')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('templates',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('subject', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('body', mysql.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('templates', schema=None) as batch_op:
        batch_op.create_index('ix_templates_name', ['name'], unique=True)

    # ### end Alembic commands ###