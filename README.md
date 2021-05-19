# abg_assignment
#assignment to upload .xlsx file to backend db with validations

## Installation

## Usage

cd abg_assignment
cd assignment


## Create a virtual environment

virtualenv venv



## Activate the virtual environment

venv\Scripts\activate.bat

## Install all the packages from requirements.txt

pip install requirements.txt


## Migrate

python manage.py migrate


## Start the app

python manage.py runserver


## URL's

127.0.0.1:8000 - To upload files
127.0.0.1:8000/admin - to access Admin
127.0.0.1:8000/export - to export file as .xlsx
