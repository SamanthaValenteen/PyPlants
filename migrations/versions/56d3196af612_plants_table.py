"""plants table

Revision ID: 56d3196af612
Revises: d5763cea9435
Create Date: 2020-05-21 19:11:19.532012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d3196af612'
down_revision = 'd5763cea9435'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=140), nullable=True),
    sa.Column('pot', sa.String(length=140), nullable=True),
    sa.Column('watering_frequency', sa.Integer(), nullable=True),
    sa.Column('last_watered', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_plants_last_watered'), 'plants', ['last_watered'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.drop_index('ix_posts_timestamp', table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_plants_last_watered'), table_name='plants')
    op.drop_table('plants')
    # ### end Alembic commands ###
