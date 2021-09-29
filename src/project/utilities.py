from pathlib import Path
from typing import Dict

import yaml


def load_config() -> Dict:
    """Loads config file from `conf` directory.

    Overwrites base with local config.

    Returns:
        Dict: config dict
    """
    config_path = Path(__file__).parents[2] / "conf" / "base.yml"
    if config_path.exists():
        with open(config_path, "r") as f:
            base_config = yaml.safe_load(f)
    else:
        base_config = {}

    config_path = Path(__file__).parents[2] / "conf" / "local.yml"
    if config_path.exists():
        with open(config_path, "r") as f:
            local_config = yaml.safe_load(f)
    else:
        local_config = {}

    # replace base with local overwrites
    return merge_dict(base_config, local_config)


def merge_dict(dict1, dict2):
    """Merge two dicts together into single Dict."""
    for key, val in dict1.items():
        if type(val) == dict:
            if key in dict2 and type(dict2[key] == dict):
                merge_dict(dict1[key], dict2[key])
        else:
            if key in dict2:
                dict1[key] = dict2[key]

    for key, val in dict2.items():
        if not key in dict1:
            dict1[key] = val

    return dict1
