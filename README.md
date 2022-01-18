# Inventory Management System
This application manages an inventory of items.

## Setup
First, set up a virtual environment for the application.
```bash
python3 -m venv venv
. venv/bin/activate
```
Then install the required packages.
```bash
pip install -r requirements.txt
```
Next, create a config file in `instance/config.py`  to store the secret key, database URL, and database URL for unit tests. An example config file is provided already in the `instance/example_config.py`. Rename this file to `config.py` and replace the placeholders with the actual values.

Finally, export the Flask environment variables and run the app.
```bash
export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```

## Testing
To run unit tests, in your virtual environment, run the test file.
```bash
python tests.py
```
