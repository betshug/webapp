"""Added the role (user or admin) to the user table

Revision ID: ef39bbcbb16f
Revises: b3329a5f5a6c
Create Date: 2022-11-03 22:38:22.154366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef39bbcbb16f'
down_revision = 'b3329a5f5a6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
