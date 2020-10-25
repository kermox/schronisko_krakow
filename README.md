# [schronisko-krakow](http://schroniskokrakow.herokuapp.com/)

## About project
The idea behind  [schronisko-krakow](https://schroniskokrakow.herokuapp.com/) website is to prove my programming skills by doing a kind of *commercial* project from scratch.
At the same time I am willing to support a non-profit organizations such as [Krakowskie Schronisko dla Bezdomnych Zwierzat](http://www.schronisko.krakow.pl/). I am sure that modern website will improve the adoption rate for this shelter and provide a better user experience throughout the process. <br>

![Alt Text](https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.gif)

## Technology stack
### Back-end:
For the back-end I used **python3** together with its framework **Django**.
**Celery** and **Redis** handle the asynchronous tasks such as sending an email. Python's **requests** library is used to make calls to **Facebook Grapgh API**.
Database - **PostgreSQL** 

### Front-end:
The front-end part of application is written with **HTML5** using **django-templates** syntax, **SASS** preprocessor and **Bootstrap4** css framework,
**Jquery** and **Vanilla Javascript**. 

### Tests:
Some simple unit tests are made with **django.test.TestCase** class and
functional tests are made with **Selenium**.


### Deployment:
The project is deployed on **Heroku** using hobby-dev subscription.
Mediafiles are loaded and served up via an  **AWS S3** buckets. Staticfiles are server with fantastic **Whitenoise**.

## Instalation
**Clone the repo:**
```
git clone https://github.com/kermox/schronisko_krakow.git
```
**Go to project directory where `manage.py` is located:**
```
cd schronisko_krakow
```
**Create a virtual environment:**
* On macOS and Linux:
```
python3 -m venv env
```
* On Windows:
```
py -m venv env
```
**activate virtual env:**
```
source env/bin/activate
```
**Install python dependencies:**
```
pip install -r requirements.txt
```
**Install node dependencies:**
```
npm install
```
**Run server:**
```
python manage.py runserver
```
**Activate css compiler:**
```
cd staticfiles
```
```
npm run compile:css:watch
```
**Activate celery worker:**
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
Distributed under the **MIT** License.

## Contact 
Maksym Garus - [Facebook](https://www.facebook.com/kermox) <br>
garusmaks@gmail.com