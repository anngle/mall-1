"""empty message

Revision ID: 9c69db5b89eb
Revises: df01e17e73e1
Create Date: 2017-02-20 13:42:19.161000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c69db5b89eb'
down_revision = 'df01e17e73e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'user_id')
    # ### end Alembic commands ###
