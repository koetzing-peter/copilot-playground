:: Copilot instructions:
:: Create a windows batch file that will
:: - remove any exiting .venv folder
:: - create a new virtual environment in .venv
:: - activate that environment
:: - pip install all requirements from the txt file

REM Close your IDE before running this script from the cmd-shell
:: Remove existing venv
rmdir /s /q .venv
:: Make sure to run the desired Python version
python -m venv .venv
:: Activate venv
call .venv\Scripts\activate
:: Upgrade pip installer
python -m pip install --upgrade pip
:: Install project requirements
pip install --prefer-binary -r requirements.txt
