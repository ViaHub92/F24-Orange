"""changed fk template_id in phishing_emails table to be nullable

Revision ID: 687933f763d7
Revises: c824cdca3e7e
Create Date: 2024-12-06 19:09:34.185448

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '687933f763d7'
down_revision = 'c824cdca3e7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('phishing_emails', schema=None) as batch_op:
        batch_op.alter_column('template_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('phishing_emails', schema=None) as batch_op:
        batch_op.alter_column('template_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
