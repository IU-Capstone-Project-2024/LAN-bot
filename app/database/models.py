from os import getenv
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import BigInteger, String, ForeignKey, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

load_dotenv()
engine = create_async_engine(url=getenv('SQLALCHEMY_URL'))

session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    User_ID: Mapped[int] = mapped_column(primary_key=True, index=True)
    Profile_ID: Mapped[int] = mapped_column(ForeignKey('profiles.Profile_id'), nullable=True)
    Participant_ID: Mapped[int] = mapped_column(ForeignKey('participants.Participant_id'), nullable=True)
    Tg_id = mapped_column(BigInteger)
    User_name: Mapped[str] = mapped_column(String(30))
    # name: Mapped[str] = mapped_column(String(30))
    # age: Mapped[int] = mapped_column()
    # sex: Mapped[bool] = mapped_column()
    # religion: Mapped[str] = mapped_column(String(25))
    # room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    # roomss = relationship('Room', back_populates='userss')

    user_profile = relationship('Profile', back_populates='profile_user')
    user_participant = relationship('Participant', back_populates='participant_user')


class Metric(Base):
    __tablename__ = 'metrics'

    Metric_ID: Mapped[int] = mapped_column(primary_key=True, index=True)
    Profile_id: Mapped[int] = mapped_column(ForeignKey('profiles.Profile_id'))
    Name: Mapped[str] = mapped_column(String(30))
    Value: Mapped[float] = mapped_column()

    metric_profile = relationship('Profile', back_populates='profile_metric')


class Profile(Base):
    __tablename__ = 'profiles'

    Profile_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    Name: Mapped[str] = mapped_column(String(100))
    Age: Mapped[int] = mapped_column()
    Photo: Mapped[str] = mapped_column(String(40))
    Date_birth: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    Sex: Mapped[int] = mapped_column()
    Religion: Mapped[str] = mapped_column(String(40))
    About: Mapped[str] = mapped_column(String(1000))

    profile_user = relationship('User', back_populates='user_profile')
    profile_metric = relationship('Metric', back_populates='metric_profile')


class Match(Base):
    __tablename__ = 'matches'

    Match_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    Profile_id1: Mapped[int] = mapped_column(ForeignKey())
    Profile_id2: Mapped[int] = mapped_column(ForeignKey())

    match_profile = relationship('Profile', back_populates='')


class Participant(Base):
    __tablename__ = 'participants'

    Participant_ID: Mapped[int] = mapped_column(primary_key=True, index=True)
    Room_id: Mapped[int] = mapped_column(ForeignKey())

    participant_user = relationship('User', back_populates='user_participant')

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
