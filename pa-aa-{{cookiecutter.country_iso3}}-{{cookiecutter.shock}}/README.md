# {{cookiecutter.country_name}} Anticipatory Action: {{cookiecutter.shock}}

{%- if cookiecutter.status.lower() == "under development" %}

[![Generic badge](https://img.shields.io/badge/STATUS-UNDER%20DEVELOPMENT-%23007CE0)](https://shields.io/)

{%- elif cookiecutter.status.lower() == "under revision" %}

[![Generic badge](https://img.shields.io/badge/STATUS-UNDER%20REVISION-%23CCCCCC)](https://shields.io/)

{%- elif cookiecutter.status.lower() == "endorsed" %}

[![Generic badge](https://img.shields.io/badge/STATUS-ENDORSED-%231EBFB3)](https://shields.io/)

{%- elif cookiecutter.status.lower() == "on hold" %}

[![Generic badge](https://img.shields.io/badge/STATUS-ON%20HOLD-%23F2645A)](https://shields.io/) 

{%- endif %}

## Background information

Provide a basic overview of the context of anticipatory action in this country. Link to the GDrive Trigger Card document for greater context and details.  

## Overview of analysis

What is the basic process of the analysis contained within this repository? 

## Data description

- Where does the data come from? Are there any licensing or usage restrictions?
- How can the data be accessed?
- Why were these datasets selected?
- Are there any limitations with these datasets that one should be aware of when running the analysis and interpreting results?

## Directory structure 

The code in this repository is organized as follows: 

```

├── analysis      # Main repository of analytical work for the AA pilot, likely mostly .md files 
├── docs          # .Rmd files or other relevant documentation
├── exploration   # Experimental work not intended to be replicated 
├── src           # Code to run any relevant data acquisition/processing pipelines
|
├── .gitignore
├── README.md
└── requirements.txt

```

## Reproducing this analysis

Create a new virtual environment and install the requirements with 

```
pip install -r requirements.txt
```

All code is formatted according to black and flake8 guidelines. The repo is set-up to use pre-commit. Before you start developing in this repository, you will need to run 

```
pre-commit install
```

For baseline datasets, you might also need to sync [this](https://drive.google.com/drive/u/3/folders/1RVpnCUpxHQ-jokV_27xLRqOs6qR_8mqQ) directory from Google drive to your local machine. Create an environment variable called `AA_DATA_DIR` that points to this directory.