from app.database.models import session, User, Room, Metric
from sqlalchemy import select, update


async def set_user(t_id: int, username: str) -> None:
    async with session() as s:
        user = await s.scalar(select(User).where(User.Tg_id == t_id))

        if not user:
            s.add(User(Tg_id=t_id, User_name=username))
            await s.commit()
