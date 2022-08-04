# Daily News Web App

![Screenshot from 2022-08-04 22-59-41](https://user-images.githubusercontent.com/73170886/182913909-805c9c2a-840a-4393-8b51-ccd58e9ba13d.png)

![Screenshot from 2022-08-04 23-01-00](https://user-images.githubusercontent.com/73170886/182914096-98b24207-79aa-46af-8c60-76ea96f674b2.png)

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

