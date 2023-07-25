import os

import yaml
from dotenv import load_dotenv

from utils.paths import get_subdirectory_path

# Configuration instance
_config = None


class ConfigLoadError(Exception):
    pass


def get_config():
    """
    Get the configuration object.

    Load the configuration from the `config/config.yaml`, if not yet loaded.

    :return: Configuration loaded from YAML file.
    """
    global _config
    if _config is None:
        cfg_path = os.path.join(get_subdirectory_path("config"), "config.yaml")
        try:
            with open(cfg_path, "r") as file:
                _config = yaml.safe_load(file)
        except FileNotFoundError:
            raise ConfigLoadError(f'Configuration file not found at "{cfg_path}".')
        except yaml.YAMLError as e:
            raise ConfigLoadError(f"Error loading the configuration file: {e}")
        if _config is None:
            raise ConfigLoadError(f'Configuration is empty in "{cfg_path}".')
    return _config


def get_bot_token() -> str:
    """
    Get the application token.

    Load the BOT_TOKEN environment variable from the `.env` file.

    :return: Token string.
    """
    if not load_dotenv():
        raise ConfigLoadError(f"No environment variables loaded. Check the .env file.")
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ConfigLoadError(f"Missing BOT_TOKEN variable. Check the .env file.")
    return token
