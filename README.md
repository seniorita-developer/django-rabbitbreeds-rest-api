Rabbit Breeds Api created with Django Rest Framework.
Data loaded from JSON file rabbit_breeds.json (scrapped from Wikipedia page)
Documentation created with Swagger UI.

Link to API:  https://rabbit-breed-api.herokuapp.com/

Documentation: https://rabbit-breed-api.herokuapp.com/docs/

To run the project on Windows:
- venv\Scripts\activate

Install Django and Django REST framework into the virtual environment
- pip install django
- pip install djangorestframework

Run server:
- cd rabbitbreedapi
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata rabbit_breeds.json
- python manage.py runserver

Endpoints:

GET /breeds​/

GET /breeds​/{breed_id}​/

GET /breeds-with-images​/

GET /random​/



