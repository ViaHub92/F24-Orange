"""fifth try

Revision ID: cf7d42bcba11
Revises: 
Create Date: 2024-10-28 21:24:32.107777

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cf7d42bcba11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_interaction', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'phishing_emails', ['phishing_email_id'], ['id'])
        batch_op.drop_column('template_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_interaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('template_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###