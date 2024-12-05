"""Added a target list for peer phishing feature

Revision ID: 4bed06b83fe9
Revises: f3336ef53c0f
Create Date: 2024-12-05 16:38:39.251040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bed06b83fe9'
down_revision = 'f3336ef53c0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('target_lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_profile_id'], ['student_profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('target_lists')
    # ### end Alembic commands ###
