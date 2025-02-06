from src.model.model import RegisteredUsers


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
