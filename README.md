# Daily News Web App

- This is a news web app like Times Of India. 
- It displays news of categories like sports, technology, health, science, business, entertainment, etc.
- I have not used database tables in this project.
- I have used mainly bootstrap to enhance front end features of this mini project.

## How to install in local environment

- Create virtual environment in the root directory using the following command:
```
python3 -m venv venv
```
- Activate Virtual environment by running the following:
```
source ./venv/bin/activate
```
- Go inside `myproject` (outer) folder and run the following command:
```
pip install -r requirements.txt
```
- Get News API key from this website: https://newsapi.org/
- Create new file called: `.env` in `myproject` folder (outer)
- Write this content in .env file- `API_KEY='<your-api-key>'`
- Be in the same folder and run the following command: 
```
python3 manage.py runserver
```
- Make sure to run the command where `manage.py` file is present.

