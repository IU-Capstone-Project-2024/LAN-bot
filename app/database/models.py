from os import getenv

from dotenv import load_dotenv
from sqlalchemy import BigInteger, String
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()
engine = create_async_engine(url=getenv('SQLALCHEMY_URL'))

session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tg_id = mapped_column(BigInteger)
    user_name: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(30))
    # age: Mapped[int] = mapped_column()
    # # dob: Mapped[date] = mapped_column()
    # sex: Mapped[bool] = mapped_column()
    # religion: Mapped[str] = mapped_column(String(25))
    # room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    # roomss = relationship('Room', back_populates='userss')


class Metric(Base):
    __tablename__ = 'metrics'

    id: Mapped[int] = mapped_column(primary_key=True)


class Room(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(70))
    description: Mapped[str] = mapped_column(String(200))
    capacity: Mapped[int] = mapped_column()
    occupancy: Mapped[int] = mapped_column()
    number: Mapped[str] = mapped_column(String(20))
    # update_time: Mapped[]
    # create_time: Mapped[]
    # userss = relationship('User', back_populates='roomss')


async def async_main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
