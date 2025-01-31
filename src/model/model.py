from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, foreign
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger, String, ForeignKey, Integer
from sqlalchemy.sql.sqltypes import NullType

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger)


class RegisteredUsers(Base):
    __tablename__ = "registered_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(String(120), nullable=True)
    marketplace: Mapped[str] = mapped_column(String(120), nullable=True)
    service: Mapped[str] = mapped_column(String(120), nullable=True)
    payment_method: Mapped[str] = mapped_column(String(120), nullable=True)
    problem_type: Mapped[str] = mapped_column(String(120), nullable=True)
    is_have_market: Mapped[str] = mapped_column(String(120), nullable=True)
    market_duration: Mapped[str] = mapped_column(String(120), nullable=True)
    market_turnover: Mapped[str] = mapped_column(String(120), nullable=True)
    market_category: Mapped[str] = mapped_column(String(120), nullable=True)
    market_url: Mapped[str] = mapped_column(String(120), nullable=True)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)