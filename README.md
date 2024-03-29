[![codecov](https://codecov.io/gh/CeeVarouqa/E-Diary_MAP/branch/main/graph/badge.svg?token=X973M7CA6F)](https://codecov.io/gh/CeeVarouqa/E-Diary_MAP)
## E-Diary and Habit Tracker

This project is an electronic diary. The purpose of this application is to serve as a modern diary: it is always with the user and can be accessed from anywhere. The notes should be secure and and accessed only by one's personal account. This e-diary can include several features. It should provide a user ability to create habit trackers and reminders for the users that they need to perform a habit they track. 

The purpose of this applications is to replace simple paper based diaries, as they lack couple of very important features and this can be solved very easily using electronic diaries. Let's give more information about features and why they are important:
1) **Ability to access from multiple devices**
    It is impossible to carry your diary with you always. So this feature can create considerable advantage of e-diary over traditional ones.
2)   **Security and privacy**
    It is obvious that traditional diaries does not have any security options except hiding them in someplace, or putting easily breakable locks, which only increases interest to break it. On the other hand, e-diaries can have very high security qualities using only classical ciphering and cryptography methods.
4)   **Editing notes**
    This can be done in traditional diaries if you use pencil and eraser. But it is very uncomfortable and not very effective if you edit multiple times, which can be done very easily in ediary
5)   **Habit tracker**
    Probably possible if you draw tables by hand. But automated habit tracking looks and feels better, probably more motivating too.
7) **Reminders and sharing progress**
    No way you can do this effectively in paper diaries.
8) **UI/UX**
    This is obvious win by e-diary vs multiple lines of paper diary

This arguments helped us to create user stories. And most functional requirements are based on this intentions.

### **Module View of the System:**

![img](https://lh6.googleusercontent.com/24hb656SYiz_R0R8xgfOOevALxCZh8O0IAXEinwvb16VIf7KJSy2s3PbIX0nXgtuNhFHKrFMdad5QvFEDe99RVEugtoIiondGTwGLNPW8dCVbtfoR9DL3d-3Ksc-gfd0KlJvI42X)



### **Initial choices for technologies:**

**Frontend:** Node.js, HTML, and CSS

**Backend:** python with Flask, Restful API

**Tests:** PyTest

**User Interface:** Figma



### Project First Setup
1. Create virtual environment
`python3 -m venv .venv`
2. Activate venv
`. .venv/bin/activate`
3. Install all libraries
`pip install -r requirements.txt`
4. Export Flask application `export FLASK_APP=run`
5. Run it `flask run`


### API documentation
For API documentation we set up Swagger.

Below you can see the documentation for some of our methods:
![image](https://user-images.githubusercontent.com/54363667/145612634-164c4f9b-a3c2-4dd9-af41-43540805ae21.png)
![image](https://user-images.githubusercontent.com/54363667/145612747-85aad773-c0dc-42e3-87f9-c4fa1fe66771.png)
![image](https://user-images.githubusercontent.com/54363667/145612851-ae56963b-61fa-47a4-8683-376a4a5b324d.png)
![image](https://user-images.githubusercontent.com/54363667/145612975-bd313fa2-8d50-4c65-b283-8159847b70a3.png)

To see full api documentation with usage examples do the following:
1. Set up the project
2. Go to /api/docs

### Tests
To run tests just run `pytest`
1. We have added unit tests for the backend. tests are written in Python.
2. We also have test coverage, you can see the label on the top of the read me. test coverage was done using codecov.io

Example of code cov in our tests, and how percentage got smaller when we removed some test:

![image](https://user-images.githubusercontent.com/42468193/145602890-cb4a9988-f28a-45d2-b78d-b58383f13edd.png)


### Github Actions checks:
1. Docker Image 
2. runs tests.py (checks tests)
3. PRs

Example of Action checks: 
![image](https://user-images.githubusercontent.com/42468193/145603390-9914cba2-cd30-4e3e-8d9c-0b97c46379b5.png)


