[![Build Status](https://travis-ci.org/minatah/MyDiaryUI.svg?branch=challenge_2)](https://travis-ci.org/minatah/MyDiaryUI)
[![Coverage Status](https://coveralls.io/repos/github/minatah/MyDiaryUI/badge.svg?branch=challenge_2)](https://coveralls.io/github/minatah/MyDiaryUI?branch=challenge_2)
[![Maintainability](https://api.codeclimate.com/v1/badges/1588592243e0dc1d87bb/maintainability)](https://codeclimate.com/github/minatah/MyDiaryUI/maintainability)

MyDiary is an online journal where users can pen down their thoughts and feelings.

To access this API online visit [API Link ](https://challengetwo.herokuapp.com)

### Requirements Building blocks.
- ```Python3``` - A programming language that lets us work more quickly (The universe loves speed!).

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment

### Installation on WIndows

First clone this repository
```
 git clone @https://github.com/minatah/MyDiaryUI/tree/challenge_2
 cd challenge_2
 ```

Create virtual environment and install it on Windows

 ```
 virtualenv --python=python3 venv
 .\venv\bin\activate.bat
 ```

Then install all the necessary dependencies by
 ```
pip install -r requirements.txt
 ```

Then run the application
 ```
 python run.py
 ```
 Testing and knowing coverage run
 ```
nosetests or python manage.py test
 ```
