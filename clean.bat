@echo off

rem This batch file will run flake8 and black on all Python files in the current directory.

rem update dependencies
pip freeze > ./requirements.txt

rem Run flake8.
flake8 .

rem Run black.
black .

rem Exit the batch file.
exit