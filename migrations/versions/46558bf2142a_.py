"""empty message

Revision ID: 46558bf2142a
Revises: None
Create Date: 2014-07-28 14:46:40.600937

"""

# revision identifiers, used by Alembic.
revision = '46558bf2142a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('companion_key', sa.Binary(), nullable=True),
    sa.Column('user_key_salt', sa.Binary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=8), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('meta', sa.Text(), nullable=True),
    sa.Column('content', sa.LargeBinary(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.Column('modified_timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    ### end Alembic commands ###
