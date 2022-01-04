# International Classification of Diseases API
> This is an API for ICD-10 diseases built with Django and Django Rest Framework using Postresql as the database.


## **Installation**

_Below is the instructions on how to get this app running_


1. Clone the repo
   ```sh
   $ git clone https://github.com/quamejnr/icd-project.git
   ```


2. Create `.env` file in root and set your environment variables
   ```sh
   SECRET_KEY = DJANGO_SECRET_KEY
   
   EMAIL_HOST_USER = EMAIL HOST USER 
   EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
   
   DATABASE_USER = DATABASE_USER
   DATABASE_PASSWORD = DATABASE_PASSWORD
   
   ```


3. Build images and start services
   ```sh
   $ docker-compose up -d --build
   ```
   

4. Create Migrations
   ```sh
   $ docker-compose exec web python manage.py migrate
   ```


5. Open `http://localhost:8000` to view it in the browser


## Usage
You can view the various endpoints of the API at `http://localhost:8000/swagger`
