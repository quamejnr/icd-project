# International Classification of Diseases API
> This is an API for ICD-10 diseases built with Django and Django Rest Framework using Postgresql as the database.


## **Installation**

_Below are instructions on how to get this app running_


1. Clone the repo
   ```sh
   git clone https://github.com/quamejnr/icd-project.git
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
   

4. Apply Migrations
   ```sh
   $ docker-compose exec web python manage.py migrate
   ```


5. Open `http://localhost:8000` to view it in the browser


## Usage
You can view the various endpoints of the API at `http://localhost:8000/swagger`


## Data

_Below are instructions to add data to your database_

1. Navigate to file upload endpoint `http://localhost:8000/icd-10/upload-file/`

2. Upload file `icd-codes.csv` in project directory.

3. Database will be populated now if upload was successful
