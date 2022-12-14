"""Added the role (user or admin) to the user table picture

Revision ID: 8a25b30a6ca2
Revises: ef39bbcbb16f
Create Date: 2022-11-07 23:02:28.169347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a25b30a6ca2'
down_revision = 'ef39bbcbb16f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    op.add_column('product', sa.Column('img', sa.Text(), nullable=True))
    op.add_column('product', sa.Column('img_name', sa.Text(), nullable=False))
    op.add_column('product', sa.Column('mimetype', sa.Text(), nullable=False))
    op.create_unique_constraint(None, 'product', ['img'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='unique')
    op.drop_column('product', 'mimetype')
    op.drop_column('product', 'img_name')
    op.drop_column('product', 'img')
    op.create_table('image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('img', sa.TEXT(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('mimetype', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img')
    )
    # ### end Alembic commands ###
