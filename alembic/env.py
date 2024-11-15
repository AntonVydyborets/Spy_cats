from app.models import Base
import os
from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine

fileConfig(context.config.config_file_name)

target_metadata = Base.metadata

# Оновлення DATABASE_URL для SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./spy_agency.db")


def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
