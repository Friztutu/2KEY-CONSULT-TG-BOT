import csv
from sqlalchemy import BigInteger, Sequence
from aiogram import types
from io import StringIO

from src.model.model import RegisteredUsers, ManagerUser
from src import strings


def registered_user_to_string(registered_user: RegisteredUsers) -> str:
    magazine_info_string = ""
    base_info_string = ""

    if registered_user.is_have_market:
        magazine_info_string += (f"Ваш магазин существует: {registered_user.market_duration}\n"
                                 f"Оборот вашего магазина: {registered_user.market_turnover}\n"
                                 f"Категория в который вы работаете: {registered_user.market_category}\n"
                                 f"Ссылка на ваш магазин: {registered_user.market_url}")

    if registered_user.service != "Разовая консультация":
        base_info_string += (f"Маркетплейс: {registered_user.marketplace}\n"
                             f"Услуга: {registered_user.service}\n"
                             f"Способ оплаты: {registered_user.payment_method}\n"
                             f"Проблема с который вы обратились: {registered_user.problem_type}\n")
    else:
        base_info_string += (f"Маркетплейс: {registered_user.marketplace}\n"
                             f"Проблема с который вы обратились: {registered_user.problem_type}\n")

    return base_info_string + magazine_info_string


def get_managers_id(managers: tuple[ManagerUser]) -> list[str]:
    result = []

    for manager in managers:
        result.append(str(manager.tg_id))

    return result


def get_csv_file(users: tuple[RegisteredUsers]) -> types.BufferedInputFile:
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(strings.TABLE_COLUMN_NAMES)

    for user in users:
        writer.writerow([
            user.tg_id, user.username, user.name, user.marketplace, user.service, user.payment_method,
            user.problem_type, user.is_have_market, user.market_duration, user.market_turnover,
            user.market_category, user.market_url, user.date
        ])

    # Подготавливаем файл для отправки
    csv_buffer.seek(0)
    csv_file = types.BufferedInputFile(
        csv_buffer.getvalue().encode(),
        filename="users_table.csv"
    )

    return csv_file
