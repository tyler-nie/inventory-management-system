# Inventory Management System
This application manages an inventory of items.

## Setup
First, set up a virtual environment for the application.
```
python 3 -m venv venv
. venv/bin/activate
```
Then install the required packages.
```
pip install -r requirements.txt
```
Finally, export the Flask environment variables and run the app.
```
export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```

## Testing
To unit testing, in your virtual environment, run the test file.
```
python tests.py
```
