# data-analysis-template
Template repo for data analysis projects

Includes typical settings for VScode


Based on [Kedro](https://github.com/quantumblacklabs/kedro) and [Cookie Cutter Data Science](https://github.com/drivendata/cookiecutter-data-science/)

*   Kedro/cookie cutter based
*   fsspec for IO
*   config.yml
*   testing
*   mkdocs
*   pre-commit code formatting

## Using the template
Clone the repo.
Replace instances of `Project` and away you go.

## Install dev environment
Conda:
```
conda env create -f environment.yml
```

Docker via devcontainers in vscode.

Pip + venv:
```
python -m venv project_env
source project_env/bin/activate
pip install -r src/requirements_dev.txt
pip install -r src/requirements_test.txt
pip install -e src/
```

Installing pre-commit hooks in each case:
```
pre-commit install
```

## Testing
```
pytest
```

## Docs
`mkdocs build` or `mkdocs serve`

## Data layers
Taken directly from `Kedro`.

## Coding style
*   `black` for general style.
*   `pydocstyle` - doc strings - google style.
*   `isort` - for ordering imports.

## Todo
*   Project specific vscode settings (autoformatter etc.) in the dev container json and vscode folder? How to apply with conda/pip installations?
*   Personal dev settings (shortcuts etc.) not in the dev container.
