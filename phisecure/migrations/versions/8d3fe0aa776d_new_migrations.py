"""new migrations

Revision ID: 8d3fe0aa776d
Revises: 
Create Date: 2024-11-16 17:08:55.129507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d3fe0aa776d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.drop_column('boolean_response')
        batch_op.drop_column('question_id')
        batch_op.drop_column('response_text')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('response_text', mysql.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('question_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('boolean_response', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))

    # ### end Alembic commands ###