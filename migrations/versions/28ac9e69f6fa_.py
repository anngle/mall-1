"""empty message

Revision ID: 28ac9e69f6fa
Revises: 61d5475f17b7
Create Date: 2017-02-21 22:51:53.038000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '28ac9e69f6fa'
down_revision = '61d5475f17b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'Original_price')
    op.drop_column('products', 'Special_price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('Special_price', mysql.DECIMAL(precision=15, scale=2), nullable=True))
    op.add_column('products', sa.Column('Original_price', mysql.DECIMAL(precision=15, scale=2), nullable=True))
    # ### end Alembic commands ###
