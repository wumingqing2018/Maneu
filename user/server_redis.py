from django.core.cache import cache


def set_user_login(session_key, value):
    return cache.set(session_key, value, 720)


def get_user_login(session_key):
    return cache.get(session_key)


def del_user_login(session_key):
    return cache.delete(session_key)


def verify_user_login(session_key):
    return cache.get_or_set(session_key, {'user': False}, 720)
