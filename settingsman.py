import json
import os
from typing import Any, Dict

PATH_TO_JSON = os.path.join(os.curdir, "settings.json")
SETTINGS: Dict[str, Any]


# === DO NOT USE THESE OUTSIDE OF THIS FILE ====================================================
class SettingsNotFoundError(Exception):
    """
    Custom exception for when settings fail to initialize.

    TODO: Move to exceptions file.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"SettingsNotFoundError: {self.message}"


def _dump_settings() -> None:
    """
    Dumps the current `SETTINGS` to the JSON file specified by `PATH_TO_JSON`.

    Raises:
        `SettingsNotFoundError`: If `SETTINGS` is None.
    """
    if not SETTINGS:
        raise SettingsNotFoundError("'SETTINGS' is empty or not initialized.")

    try:
        with open(PATH_TO_JSON, "w") as file:
            json.dump(SETTINGS, file, indent=4)

            print("Settings saved.")  # Update these to use logging library
    except IOError as e:
        print(f"IO Error while saving settings: {e}")


# === PUBLIC METHODS =============================================================================
def init_settings() -> None:
    """
    Loads in settings from `PATH_TO_JSON`. Call during setup to have settings.
    """
    global SETTINGS

    try:
        with open(PATH_TO_JSON, "r") as file:
            contents = json.load(file)
            SETTINGS = contents

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")  # Update these to use logging library
    except FileNotFoundError:
        print(
            f"File '{PATH_TO_JSON}' not found."
        )  # Update these to use logging library
    except TypeError as e:
        print(f"Invalid file type: {e}")  # Update these to use logging library
    except IOError as e:
        print(f"IO Error: {e}")  # Update these to use logging library


def update_setting(key: str, value: Any) -> None:
    """
    Update settings to `value` at `key`.
    """
    if not SETTINGS:
        raise SettingsNotFoundError("'SETTINGS' is empty or not initialized.")

    SETTINGS[key] = value
    _dump_settings()


def read_setting(key: str) -> Any:
    """
    Read value in settings at `key`.
    """
    if not SETTINGS:
        raise SettingsNotFoundError("'SETTINGS' is empty or not initialized.")

    return SETTINGS.get(key, None)