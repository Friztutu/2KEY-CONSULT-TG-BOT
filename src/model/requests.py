from typing import Any

from .model import async_session, User, RegisteredUsers
from sqlalchemy import select, update


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_registered_user(tg_id: int, name: str, data: dict[str, Any]) -> None:
    async with async_session() as session:
        user = await session.scalar(select(RegisteredUsers).where(RegisteredUsers.tg_id == tg_id))

        if not user:
             session.add(RegisteredUsers(tg_id=tg_id,
                             marketplace=data["marketplace"],
                             service=data["service"],
                             payment_method=data["payment_method"],
                             problem_type=data["problem_type"],
                             is_have_market=data["is_have_market"],
                             market_duration=data["market_duration"],
                             market_turnover=data["market_turnover"],
                             market_category=data["market_category"],
                             market_url=data["market_url"],
                             name=name
                             ))
        else:
            await session.execute(
                update(RegisteredUsers).values(
                    tg_id=tg_id,
                    name=name,
                    marketplace=data["marketplace"],
                    service=data["service"],
                    payment_method=data["payment_method"],
                    problem_type=data["problem_type"],
                    is_have_market=data["is_have_market"],
                    market_duration=data["market_duration"],
                    market_turnover=data["market_turnover"],
                    market_category=data["market_category"],
                    market_url=data["market_url"]
                ).where(RegisteredUsers.tg_id == tg_id)
            )


        await session.commit()


async def get_full_registered_users():
    async with async_session() as session:
        return await session.execute(select(RegisteredUsers))