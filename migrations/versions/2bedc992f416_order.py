"""order

Revision ID: 2bedc992f416
Revises: 0805d4bf4d9d
Create Date: 2020-06-22 13:30:48.545945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bedc992f416'
down_revision = '0805d4bf4d9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device', sa.Column('order_index', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_device_order_index'), 'device', ['order_index'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_device_order_index'), table_name='device')
    op.drop_column('device', 'order_index')
    # ### end Alembic commands ###