"""empty message

Revision ID: 224ed08eabcd
Revises: 6fb81b7a615b
Create Date: 2020-07-03 11:15:32.273671

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '224ed08eabcd'
down_revision = '6fb81b7a615b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('utilities', postgresql.ARRAY(sa.TEXT()), nullable=True))
    op.create_unique_constraint(None, 'recipes', ['recipe_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='unique')
    op.drop_column('recipes', 'utilities')
    # ### end Alembic commands ###
