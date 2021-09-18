from pathlib import Path
from typing import Dict

import yaml


def load_config() -> Dict:
    """Loads config file from `conf` directory.

    Returns:
        Dict: config dict
    """
    config_path = Path(__file__).parents[2] / "conf" / "config.yml"
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config
