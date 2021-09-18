# data-anaylsis-template
Template repo for data analysis projects

Includes typical settings for VScode


Based on Kedro and Cookie Cutter Data Science

*   Kedro/cookie cutter based
*   fsspec for IO
*   config.yml
*   testing
*   mkdocs

## Install
Conda:
```
conda env create -f src/environment.yml
```

Pip + venv:
```
python -m venv project_env
source project_env/bin/activate
pip install -r src/requirements_dev.txt
pip install -r src/requirements_test.txt
pip install -e src/
```

Docker via devcontainers in vscode.

## Testing
```
pytest
```

## Docs
`mkdocs build` or `mkdocs serve`

## Data layers
Taken directly from `Kedro`.

## Todo
Replace `config.yml` with base/local config files.
Local to be added to the gitignore.
Load-config function will load both and local takes precedence.
