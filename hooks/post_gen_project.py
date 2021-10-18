import os


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)


if "{{cookiecutter.notebooks_in_analysis}}" == "n":
    remove("analysis/01_analysis_step_a.md")
    remove("analysis/02_analysis_step_b.md")
