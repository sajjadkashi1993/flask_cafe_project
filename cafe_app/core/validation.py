import json
import re
from datetime import datetime


def is_name_valid(name: str) -> bool:
    """
    This function validates the name. The name must contain only English letters
    Also, its length can be at least 3 letters and at most 50 letters.
    Otherwise, it returns False

    Parameters
    ----------
    name

    Returns
    -------
    boolean
    """
    pattern = '[a-zA-Z\s]{3,50}'
    if re.fullmatch(pattern, name):
        return True
    return False


def is_phone_valid(phone: str) -> bool:
    """
    This function validates the mobile phone number.
    The mobile phone number can have one of the following two modes:
        If it starts with 09, it must be eleven digits.
        If it starts with +989, it must be thirteen digits.
    Otherwise, it returns False
    Parameters
    ----------
    phone

    Returns
    -------
    boolean
    """
    pattern = '(09)([0-9]{9})|(\+989)([0-9]{9})'
    if re.fullmatch(pattern, phone):
        return True
    return False


def is_email_valid(email: str) -> bool:
    """
    This function validates the email.
    The email format should be as follows:
    name@email.com
    Otherwise, it returns False

    Parameters
    ----------
    email

    Returns
    -------
    boolean
    """
    pattern = '^[\w\.\_]+\@([\w\.\_]+)\.[\w]{2,4}$'
    if re.fullmatch(pattern, email):
        return True
    return False


def is_character_valid(character: str) -> bool:
    """
    This function validates the user character.
    The character can have one of the following two modes:
        user.
        admin.
    Otherwise, it returns False
    Parameters
    ----------
    phone

    Returns
    -------
    boolean
    """
    character_list = ['user', 'admin']
    if character in character_list:
        return True
    return False


def is_normal_pas(pas: str) -> bool:
    """
     Takes a string as input and specifies whether it can be a password or not

        :param
            pas:str
        :return:
            True if pas is valid for the password otherwise False!!!
        """
    if len(pas) > 6:
        return True
    return False


def is_date_valid(date) -> bool:
    """
        Takes a datetime as input and specifies whether it can be a date

        :param
            date: datetime
        :return:
            True if date is valid for the input otherwise False!!!
        """
    if isinstance(date, datetime):
        return True
    return False


def is_state_valid(state: str) -> bool:
    """
    This function validates the order state.
    The state can have one of the following three types:
        in_process,
        served,
        delivered;
    Otherwise, it returns False
    Parameters
    ----------
    state: str

    Returns
    -------
    boolean
    """
    state_list = ['New orders', 'Cooking orders', 'Served orders', 'Deleted Orders', 'Paid Orders', 'Archive',
                  'in_process', 'served', 'delivered']
    if state in state_list:
        return True
    return False


def is_order_type_valid(order_type: str) -> bool:
    """
    This function validates the order type.
    The state can have one of the following three types:
        order-in-cafe,
        order_ahead,
        take_away;
    Otherwise, it returns False
    Parameters
    ----------
    order_type: str

    Returns
    -------
    boolean
    """
    order_type_list = ['order_in_cafe', 'order_ahead', 'take_away']
    if order_type in order_type_list:
        return True
    return False


def is_int_valid(number: int) -> bool:
    """
    This function validates the number. The number must be integer.
    Otherwise, it returns False

    Parameters
    ----------
    number

    Returns
    -------
    boolean
    """
    if isinstance(number, int):
        return True
    return False


def is_float_valid(number: float) -> bool:
    """
    This function validates the number. The number must be float.
    Otherwise, it returns False

    Parameters
    ----------
    number

    Returns
    -------
    boolean
    """
    if isinstance(number, float):
        return True
    return False


def is_json_valid(json_as_str: str) -> bool:
    """
    This function validates the input string is JSON.
    Otherwise, it returns False

    Parameters
    ----------
    String of a JSON

    Returns
    -------
    boolean
    """
    try:
        json.loads(json_as_str)
    except ValueError:
        return False
    return True


def is_bool_valid(input: bool) -> bool:
    """
    This function validates the input is boolean.
    Otherwise, it returns False

    Parameters
    ----------
    boolean

    Returns
    -------
    boolean
    """
    if isinstance(input, bool):
        return True
    return False
