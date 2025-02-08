from datetime import datetime, date, timedelta
from typing import Any

from .model import async_session, User, RegisteredUsers, ManagerUser
from sqlalchemy import select, update, BigInteger
from src import keyboards as kb


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_registered_user(tg_id: int, name: str, username: str, data: dict[str, Any]) -> None:
    async with async_session() as session:
        user = await session.scalar(select(RegisteredUsers).where(RegisteredUsers.tg_id == tg_id))

        marketplace = kb.MARKETPLACES[data["marketplace"]]
        service = kb.SERVICES[data["service"]]
        payment_method = kb.PAYMENT_METHODS[data["payment_method"]]

        if len(data["problem_type"]) == 1:
            problem_type = kb.CLIENT_PROBLEMS[data["problem_type"]]
        else:
            problem_type = data["problem_type"]

        is_have_market = kb.IS_HAVE_MARKET[data["is_have_market"]]
        market_duration = kb.MARKET_DURATIONS[data["market_duration"]]
        market_turnover = kb.MARKET_TURNOVERS[data["market_turnover"]]
        market_category = data["market_category"] if data["market_category"] is not None else "-"
        market_url = data["market_url"] if data["market_url"] is not None else "-"

        if not user:
             session.add(RegisteredUsers(
                 tg_id=tg_id,
                 marketplace=marketplace,
                 service=service,
                 payment_method=payment_method,
                 problem_type=problem_type,
                 is_have_market=is_have_market,
                 market_duration=market_duration,
                 market_turnover=market_turnover,
                 market_category=market_category,
                 market_url=market_url,
                 name=name,
                 username=username
             ))
        else:
            await session.execute(
                update(RegisteredUsers).values(
                    tg_id=tg_id,
                    marketplace=marketplace,
                    service=service,
                    payment_method=payment_method,
                    problem_type=problem_type,
                    is_have_market=is_have_market,
                    market_duration=market_duration,
                    market_turnover=market_turnover,
                    market_category=market_category,
                    market_url=market_url,
                    name=name,
                    username=username,
                    date=datetime.now()
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

async def get_full_registered_users():
    async with async_session() as session:
        result =  await session.execute(select(RegisteredUsers))
        user = result.scalars().all()
        return user


async def get_registered_user_by_id(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(RegisteredUsers).where(RegisteredUsers.tg_id == tg_id))


async def delete_manager(tg_id: int) -> None:
    async with async_session() as session:
        result = await session.execute(select(ManagerUser).where(ManagerUser.tg_id == tg_id))
        user = result.scalar_one()

        if user:
            await session.delete(user)
            await session.commit()


async def get_registered_users_by_day(target_date: date):
    async with async_session() as session:
        start_datetime = datetime.combine(target_date, datetime.min.time())
        end_datetime = start_datetime + timedelta(days=1)
        query = select(RegisteredUsers).where(
            RegisteredUsers.date >= start_datetime,
            RegisteredUsers.date < end_datetime
        )

        result = await session.execute(query)
        records = result.scalars().all()

        return records