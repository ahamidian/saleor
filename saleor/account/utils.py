import os
import os.path
import random

from django.conf import settings
from django.core.files import File

from ..checkout import AddressType

AVATARS_PATH = os.path.join(
    settings.PROJECT_ROOT, "saleor", "static", "images", "avatars"
)


def store_user_address(user, address, address_type):
    """Add address to user address book and set as default one."""
    address, _ = user.addresses.get_or_create(**address.as_data())
    set_user_default_address(user, address)


def set_user_default_address(user, address):
    user.default_address = address
    user.save(update_fields=["default_address"])


def change_user_default_address(user, address, address_type):
    set_user_default_address(user, address)


def get_user_first_name(user):
    """Return user first name if not exist return None."""
    if user.first_name:
        return user.first_name
    return None


def get_user_last_name(user):
    """Return user last name if not exist return None."""
    if user.last_name:
        return user.last_name
    return None


def get_random_avatar():
    """Return random avatar picked from a pool of static avatars."""
    avatar_name = random.choice(os.listdir(AVATARS_PATH))
    avatar_path = os.path.join(AVATARS_PATH, avatar_name)
    return File(open(avatar_path, "rb"), name=avatar_name)
