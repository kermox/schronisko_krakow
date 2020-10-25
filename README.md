# [schronisko-krakow](http://schroniskokrakow.herokuapp.com/)

## About project
The idea behind  [schronisko-krakow](https://schroniskokrakow.herokuapp.com/) website is to prove  my programming skills by doing a kind of *commercial* project from scretch.
At the same time I am willing to support a non-profit organizations such as [Krakowskie Schronisko dla Bezdomnych Zwierzat](http://www.schronisko.krakow.pl/). Im sure that better presentation in the web  will help them to better achieve their mission.

## Technology stack
#####Backend:
For the backend I used **python3** together with its framework **Django**.
**Celery** and **Redis** handle the asynchronous tasks such as sending an email. Python's **requests** library is used to make calls to **Facebook Grapgh API**.
Database - **PostgreSQL** 

#####Frond-end:
The front-end part of application was written with **HTML5** for django templates, **SASS** and **Bootstrap4** for stylesheets and mixed
**Jquery** library with **Vanilla Javascript**.

#####Tests:
Some simple unit tests are made with **django.test.TestCase** class.
Functional tests are made with **Selenium**.


#####Deployment:
The project was deployed on **Heroku** using hobby-dev subscription.
Mediafiles are loaded and served up via an  **AWS S3** buckets. Staticfiles are server with fantastic **Whitenoise**.

## Instalation
* Clone the repo:<br> 
```
git clone https://github.com/kermox/schronisko_krakow.git
```
* Go to project directory where `manage.py` is located:
```
cd schronisko_krakow
```
* Create a virtual environment:
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;On macOS and Linux:
```
python3 -m venv env
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On Windows:
```
py -m venv env
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;And activate it:
```
source env/bin/activate
```
* Install python dependencies:
```
pip install -r requirements.txt
```
* Install node dependencies: 
```
npm install
```
* run server:
```
python manage.py runserver
```
* activate css compiler:
```
cd staticfiles

npm run compile:css:watch
```
* activate celery worker:
```
celery -A schronisko_krakow worker -l INFO
```
## Contributing
Any contributions you make are *greatly appreciated*.
1. Fork the project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature`')
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

## License
Distributed under the *MIT* License.

## Contact 
Maksym Garus - [Facebook](https://www.facebook.com/kermox) - [Email](garusmaks@gmail.com)