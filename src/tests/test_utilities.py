from pathlib import Path

import yaml

from project import utilities


class SideEffect:
    def __init__(self, *fns):
        self.iter = iter(fns)

    def __call__(self, *args, **kwargs):
        return next(self.iter)


def test_load_config1(monkeypatch):
    config = utilities.load_config()
    assert config == {
        "test_var1": "test",
        "test_var2": "test",
        "test_obj": {"test_var": "local"},
    }


def test_load_config(monkeypatch):
    side_effect = SideEffect(
        {"test_var1": "test", "test_obj": {"test_var": "base"}},
        {"test_var2": "test", "test_obj": {"test_var": "local"}},
    )
    monkeypatch.setattr(yaml, "safe_load", side_effect)
    exist_return = SideEffect(True, True)
    monkeypatch.setattr(Path, "exists", exist_return)

    config = utilities.load_config()
    assert config == {
        "test_var1": "test",
        "test_var2": "test",
        "test_obj": {"test_var": "local"},
    }


def test_load_config_exist(monkeypatch):
    # test for if base.yml is missing
    yaml_return = SideEffect({"test_var2": "test", "test_obj": {"test_var": "local"}})
    monkeypatch.setattr(yaml, "safe_load", yaml_return)
    exist_return = SideEffect(False, True)
    monkeypatch.setattr(Path, "exists", exist_return)

    config = utilities.load_config()
    assert config == {"test_var2": "test", "test_obj": {"test_var": "local"}}


def test_load_config_non_exist(monkeypatch):
    # test for if base.yml is missing
    yaml_return = SideEffect({"test_var2": "test", "test_obj": {"test_var": "local"}})
    monkeypatch.setattr(yaml, "safe_load", yaml_return)
    exist_return = SideEffect(False, False)
    monkeypatch.setattr(Path, "exists", exist_return)

    config = utilities.load_config()
    assert config == {}
