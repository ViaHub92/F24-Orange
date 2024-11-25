"""added major column to student profile table

Revision ID: 02eb8708bef2
Revises: 
Create Date: 2024-11-24 17:46:47.178743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02eb8708bef2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('major', sa.String(length=120), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_profiles', schema=None) as batch_op:
        batch_op.drop_column('major')

    # ### end Alembic commands ###
