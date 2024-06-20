from app.database.models import session, User, Room, Metric
from sqlalchemy import select, update


async def set_user(t_id: int, alias: str, fn: str, ln: str) -> None:
    async with session() as s:
        user = await s.scalar(select(User).where(User.tg_id == t_id))

        if not user:
            s.add(User(tg_id=t_id, user_name=alias, name=f'{fn} {ln}'))
            await s.commit()
