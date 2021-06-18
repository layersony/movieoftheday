"""user class

Revision ID: 700596f8bf15
Revises: 4a140da4a1c3
Create Date: 2021-06-17 23:40:17.472484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700596f8bf15'
down_revision = '4a140da4a1c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('subscriber', sa.Integer(), nullable=True))
    op.drop_constraint('movies_user_fkey', 'movies', type_='foreignkey')
    op.create_foreign_key(None, 'movies', 'subscribers', ['subscriber'], ['id'])
    op.drop_column('movies', 'user')
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_column('users', 'password_secure')
    op.add_column('movies', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'movies', type_='foreignkey')
    op.create_foreign_key('movies_user_fkey', 'movies', 'subscribers', ['user'], ['id'])
    op.drop_column('movies', 'subscriber')
    # ### end Alembic commands ###