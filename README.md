# Daily News Web App

![Screenshot from 2022-08-04 22-59-41](https://user-images.githubusercontent.com/73170886/182913909-805c9c2a-840a-4393-8b51-ccd58e9ba13d.png)

![Screenshot from 2022-08-04 23-01-00](https://user-images.githubusercontent.com/73170886/182914096-98b24207-79aa-46af-8c60-76ea96f674b2.png)

- It is a news web app like Times Of India. 
- It displays news of categories like sports, technology, health, science, business, entertainment, etc.
- Used Bootstrap to enhance front end features.

## How to install in local environment

- Get News API key from this website: https://newsapi.org/
- Create a new file called: `.env` in `myproject` folder (outer)
- Write this content in .env file- `API_KEY='<your-api-key>'`
- Be in the same directory and run the following command: 

### Build Docker image

```
docker build -t <image_name> .
```

### Run the container

```
docker run --network host -d <image_name>
```
