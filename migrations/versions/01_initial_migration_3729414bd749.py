"""01_initial_migration

Revision ID: 3729414bd749
Revises: 
Create Date: 2024-08-20 12:27:56.198071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3729414bd749"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "demo_model",
        sa.Column("uid", sa.UUID(), nullable=False),
        sa.Column("type", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("uid"),
    )
    op.create_index(op.f("ix_demo_model_uid"), "demo_model", ["uid"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_demo_model_uid"), table_name="demo_model")
    op.drop_table("demo_model")
    # ### end Alembic commands ###
