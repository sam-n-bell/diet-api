"""empty message

Revision ID: 6fb81b7a615b
Revises: e520b8b6427e
Create Date: 2020-07-02 13:00:18.238675

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import citext

# revision identifiers, used by Alembic.
revision = '6fb81b7a615b'
down_revision = 'e520b8b6427e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('recipe_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', citext.CIText(), nullable=False),
    sa.Column('ingredients', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('instructions', citext.CIText(), nullable=False),
    sa.Column('est_completion_time_hrs', sa.NUMERIC(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('recipe_id'),
    sa.UniqueConstraint('recipe_id')
    )
    op.create_unique_constraint(None, 'users', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'user_jwts', type_='unique')
    op.drop_table('recipes')
    # ### end Alembic commands ###
