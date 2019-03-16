# Deloitte_Hackathon
Repo to win Deloitte Hackathon 2019

Steps to install:

1. This project uses quite a lot of python packages, and thus it is important to install them first to avoid problems later.

2. We have used python 3.7 here.

3. Install the following libraries: <br>
    -PyPDF2 <br>
    -ZipFile <br>
    -csv <br>
    -os <br>
    -requests <br>
    -flask <br>
    -werkzeug <br>
    -json <br>
4. Once you have installed these libraries, open a terminal and headover to the project directory (inside pyfiles)

5. Here we need to set up the flask environment variables.

6. Type, export FLASK_APP = flask_control.py. This is because the flask_control.py is the main app/server for this project.

7. Next type, export FLASK_DEBUG=1, so that when you refresh the page with changes in the code, we don't have to instantiate the server repeatedly.

8. Write "flask run" to start the server.

9. By default, flask opens in port: 5000. In a web browser, preferably Chrome, write "localhost:5000".

10. The home page should load up a form.

11. Enter the skills required for the particular job, separated by commas. 

12. The resumes should be encapsulated in a zip file, and then uploaded.

13. The output should be the scores for each resume.


