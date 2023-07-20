#!/usr/bin/env python3
import sys

from utils.config_loader import get_config, ConfigLoadError

try:
    print(get_config())
except ConfigLoadError as e:
    print(e)
    sys.exit(1)
