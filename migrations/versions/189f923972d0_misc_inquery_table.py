"""misc inquery table 

Revision ID: 189f923972d0
Revises: 2bedc992f416
Create Date: 2020-06-25 11:46:14.828242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '189f923972d0'
down_revision = '2bedc992f416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.create_table('misc_enquiry',
    #sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    #sa.Column('description', sa.Text(), nullable=False),
    #sa.Column('customer_id', sa.Integer(), nullable=False),
    #sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    #sa.PrimaryKeyConstraint('id')
    #)
    op.alter_column('customer', 'first_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('customer', 'last_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customer', 'last_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('customer', 'first_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    #op.drop_table('misc_enquiry')
    # ### end Alembic commands ###
