"""updated db 08/08

Revision ID: b2ffa1c0ce86
Revises: 897bd4216882
Create Date: 2023-08-08 21:54:03.023372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ffa1c0ce86'
down_revision = '897bd4216882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_companies'))
    )
    op.drop_table('upload')
    with op.batch_alter_table('buses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_buses_company_id_companies'), 'companies', ['company_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password')

    with op.batch_alter_table('buses', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_buses_company_id_companies'), type_='foreignkey')
        batch_op.drop_column('company_id')

    op.create_table('upload',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_upload')
    )
    op.drop_table('companies')
    # ### end Alembic commands ###
