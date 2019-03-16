"""empty message

Revision ID: 91be9169a69f
Revises: 
Create Date: 2019-03-03 18:52:56.655940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91be9169a69f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date_required', sa.DateTime(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('meet_person_email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post', sa.Column('meet_person_email', sa.String(length=100), nullable=True))
    op.add_column('post', sa.Column('time', sa.String(), nullable=False))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.INTEGER(), nullable=False))
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.drop_column('post', 'time')
    op.drop_column('post', 'meet_person_email')
    op.drop_table('meetings')
    # ### end Alembic commands ###