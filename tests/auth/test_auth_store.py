"""Tests for the auth store."""
from homeassistant.auth import auth_store


async def test_loading_old_data_format(hass, hass_storage):
    """Test we correctly load an old data format."""
    hass_storage[auth_store.STORAGE_KEY] = {
        'version': 1,
        'data': {
            'credentials': [],
            'users': [
                {
                    "id": "user-id",
                    "is_active": True,
                    "is_owner": True,
                    "name": "Paulus",
                    "system_generated": False,
                },
                {
                    "id": "system-id",
                    "is_active": True,
                    "is_owner": True,
                    "name": "Hass.io",
                    "system_generated": True,
                }
            ],
            "refresh_tokens": [
                {
                    "access_token_expiration": 1800.0,
                    "client_id": "http://localhost:8123/",
                    "created_at": "2018-10-03T13:43:19.774637+00:00",
                    "id": "a95025b7b555486587ad8336f5653e20",
                    "jwt_key": "some-key",
                    "last_used_at": "2018-10-03T13:43:19.774712+00:00",
                    "token": "some-token",
                    "user_id": "user-id"
                },
                {
                    "access_token_expiration": 1800.0,
                    "client_id": None,
                    "created_at": "2018-10-03T13:43:19.774637+00:00",
                    "id": "a95025b7b555486587ad8336f5653e20",
                    "jwt_key": "some-key",
                    "last_used_at": "2018-10-03T13:43:19.774712+00:00",
                    "token": "some-token",
                    "user_id": "system-id"
                },
            ]
        }
    }

    store = auth_store.AuthStore(hass)
    groups = await store.async_get_groups()
    assert len(groups) == 1
    users = await store.async_get_users()
    assert len(users) == 2
    assert False, 'test all attributes'
