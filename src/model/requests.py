from typing import Any

from .model import async_session, User, RegisteredUsers, ManagerUser
from sqlalchemy import select, update, BigInteger


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


async def get_all_managers():
    async with async_session() as session:
        result = await session.execute(select(ManagerUser))
        managers = result.scalars().all()
        return managers

async def set_new_manager(data: dict[str, Any]) -> None:
    async with async_session() as session:
        session.add(ManagerUser(tg_id = int(data["tg_id"]), first_name = data["first_name"]))
        await session.commit()


async def get_full_user():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users


async def delete_manager(tg_id: int) -> None:
    pass

async def get_full_registered_users():
    async with async_session() as session:
        result =  await session.execute(select(RegisteredUsers))
        user = result.scalars().all()
        return user


async def get_registered_user_by_id(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(RegisteredUsers).where(RegisteredUsers.tg_id == tg_id))