"""initial migration

Revision ID: 1daf868c99d7
Revises: 1af75bf36d1a
Create Date: 2025-06-23 10:02:43.722194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1daf868c99d7'
down_revision = '1af75bf36d1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appearances')
    op.drop_table('episodes')
    op.drop_table('users')
    op.drop_table('guests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guests',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('guests_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('occupation', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='guests_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('username', name='users_username_key', postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('episodes',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('episodes_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='episodes_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('appearances',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('guest_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('episode_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], name='appearances_episode_id_fkey'),
    sa.ForeignKeyConstraint(['guest_id'], ['guests.id'], name='appearances_guest_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='appearances_pkey')
    )
    # ### end Alembic commands ###
