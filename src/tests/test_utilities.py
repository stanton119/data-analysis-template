import pytest
from project import utilities


def test_load_config():
    config = utilities.load_config()
    assert isinstance(config, dict)
