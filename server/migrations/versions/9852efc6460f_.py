"""empty message

Revision ID: 9852efc6460f
Revises: 7c79e17e2f42
Create Date: 2023-08-04 22:10:27.100720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9852efc6460f'
down_revision = '7c79e17e2f42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_uploads'))
    )
    op.drop_table('upload')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_upload')
    )
    op.drop_table('uploads')
    # ### end Alembic commands ###
