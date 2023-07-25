import logging
import os

from utils.config_loader import get_config, ConfigLoadError
from utils.paths import get_root_dir_path


def logger_init(name: str) -> logging.Logger:
    """
    Set up a logger instance.

    Suppresses existing logging instances at the root level.
    :param name: Name of the logger.
    :return: Named Logger instance.
    """
    config = get_config()
    try:
        log_path = os.path.join(get_root_dir_path(), config["Logging"]["path"])
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        logging.basicConfig(
            filename=log_path,
            format=config["Logging"]["format"],
            datefmt=config["Logging"]["date_format"],
            force=True,
        )

        # Suppress the root logger messages (logging may be used by external modules)
        logging.getLogger().setLevel(logging.CRITICAL)

        # Create an unsuppressed logger instance
        _logger = logging.getLogger(name)
        _logger.setLevel(logging.getLevelName(config["Logging"]["level"]))
    except KeyError as e:
        raise ConfigLoadError(f"Key not found in the configuration file: {e}")
    except ValueError as e:
        raise ConfigLoadError(f"Invalid logging level in the configuration file: {e}")
    return _logger


logger = logger_init("tulpa")
