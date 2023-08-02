"""created upload

Revision ID: 834b85ae0c2b
Revises: 16725967aa1c
Create Date: 2023-08-02 17:21:23.285035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '834b85ae0c2b'
down_revision = '16725967aa1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_upload'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('upload')
    # ### end Alembic commands ###
