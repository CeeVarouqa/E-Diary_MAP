[![codecov](https://codecov.io/gh/CeeVarouqa/E-Diary_MAP/branch/main/graph/badge.svg?token=X973M7CA6F)](https://codecov.io/gh/CeeVarouqa/E-Diary_MAP)
## E-Diary and Habit Tracker

This project is an electronic diary. The purpose of this application is to serve as a modern diary: it is always with the user and can be accessed from anywhere. The notes should be secure and and accessed only by one's personal account. This e-diary can include several features. It should provide a user ability to create habit trackers and reminders for the users that they need to perform a habit they track. 



### **Module View of the System:**

![img](https://lh6.googleusercontent.com/24hb656SYiz_R0R8xgfOOevALxCZh8O0IAXEinwvb16VIf7KJSy2s3PbIX0nXgtuNhFHKrFMdad5QvFEDe99RVEugtoIiondGTwGLNPW8dCVbtfoR9DL3d-3Ksc-gfd0KlJvI42X)



### **Initial choices for technologies:**

**Frontend:** Node.js, HTML, and CSS

**Backend:** python with Flask, Restful API

**User Interface:** Figma



### Project First Setup
1. Create virtual environment
`python3 -m venv .venv`
2. Activate venv
`. .venv/bin/activate`
3. Install all libraries
`pip install -r requirements.txt`
4. `export FLASK_APP=run`
5. `flask run`


### API documentation
1. Set up the project
2. Go to /api/docs

### Tests
To run tests just run `pytest`
1. We have added unit tests for the backend. tests are written in Python.
2. We also have test coverage, you can see the label on the top of the read me. test coverage was done using codecov.io

### Github Actions checks:
1. Docker Image 
2. runs tests.py (checks tests)
3. PRs



