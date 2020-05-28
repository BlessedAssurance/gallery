## Photo Gallery

### Author
- Vincent Kirui

### Description
- This is a django application that a user can use to view photos, description and location of the photos.The user is also able to copy the image location.

### Setup/Installation
### Cloning the repository:

 https://github.com/BlessedAssurance/gallery

#### Navigate into the folder and install requirements
cd gallery pipenv  install -r requirements.txt 

#### Install and activate Virtual
python3 -m venv virtual - source virtual/bin/activate  

#### Install Dependencies
- pipenv install -r requirements.txt 

#### Setup Database
SetUp your database User,Password, Host then make migrate

python manage.py makemigrations gallery

#### Now Migrate

python manage.py migrate 
Run the application
python manage.py runserver 

#### Testing the application
python manage.py test 

Open the application on your browser 127.0.0.1:8000.

### Technologies used
- Python3.6
- Django1.11
- Git

### Contact Information

engineervincblair@gmail.com 

### License

<a href="https://github.com/BlessedAssurance/gallery/blob/master/LICENSE">MIT license</a>

