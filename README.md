# pa-aa-cookiecutter

This cookiecutter can be used to create a new repository for
an OCHA Anticipatory Action pilot. Using this cookiecutter
will help to standardize the structure of an analysis for a
pilot and will take care of generating boilerplate content
such as a basic README and `.Rmd` docs.

## Using this cookiecutter

To use this cookiecutter, first install `cookiecutter`:

```shell
pip install cookiecutter
```

Then, generate a template from this repo:

```shell
cookiecutter https://github.com/OCHA-DAP/pa-aa-cookiecutter
```

You'll be prompted to fill in a number of parameters:

- `country_iso3`: ISO3 code for the pilot's country
- `country_name`: Full name of the pilot's country
- `shock`: The shock event that is the subject of the pilot
    (select from options provided)
- `status`: The current status of the pilot
    (select from options provided)
- `notebooks_in_analysis`: If the analysis work will be done
    within Jupyter Notebooks (y/n)

## Development

To contribute to this cookiecutter, begin by creating a new virtual
environment and installing the project dependencies.

```shell
pip install -r requirements.txt
```

This repository is set up with a number of pre-commit hooks.
Before you start developing in this repository, you will need to run

```shell
pre-commit install
```

The `markdownlint` hook will require
[Ruby](https://www.ruby-lang.org/en/documentation/installation/)
to be installed on your computer.

You can run all hooks against all your files using

```shell
pre-commit run --all-files
```
