"""empty message

Revision ID: 5094383eaf2f
Revises: 26977f2132f6
Create Date: 2020-05-22 14:41:49.791205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5094383eaf2f'
down_revision = '26977f2132f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('next_water_date', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_plant_next_water_date'), 'plant', ['next_water_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_plant_next_water_date'), table_name='plant')
    op.drop_column('plant', 'next_water_date')
    # ### end Alembic commands ###
