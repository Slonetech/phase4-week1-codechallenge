"""best pizza 

Revision ID: 0fd7cf13afcd
Revises: 7f153a679823
Create Date: 2023-09-27 15:58:33.103221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd7cf13afcd'
down_revision = '7f153a679823'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'restaurants', ['restaurant_id'], ['id'])

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.create_unique_constraint('unique_name_constraint', ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.drop_constraint('unique_name_constraint', type_='unique')

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
