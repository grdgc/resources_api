"""empty message

Revision ID: 514a36eb1161
Revises: 59a6f6552b5a
Create Date: 2018-08-08 22:13:09.695012

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = '514a36eb1161'
down_revision = '59a6f6552b5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('languages_id', sa.Integer(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('upvotes', sa.INTEGER(), nullable=True),
    sa.Column('downvotes', sa.INTEGER(), nullable=True),
    sa.Column('times_clicked', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['languages_id'], ['language.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resource')
    op.drop_table('language')
    op.drop_table('category')
    # ### end Alembic commands ###
