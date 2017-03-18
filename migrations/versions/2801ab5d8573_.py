"""empty message

Revision ID: 2801ab5d8573
Revises: 4eed386a154f
Create Date: 2017-03-03 00:26:26.460000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2801ab5d8573'
down_revision = '4eed386a154f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('score_count', sa.Integer(), nullable=True),
    sa.Column('integral', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery')
    # ### end Alembic commands ###