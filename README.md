# Online-Doctor-Appointment-System
Final Year Group project - Grp 10

## Steps to setup virtual environment (Windows):
1. Ensure that python 3 is installed in the system
2. In command prompt type:

`pip install virtualenvwrapper`

3. Let’s create a new virtual environment named ‘test’
Run the following command:

`mkvirtualenv test`

4. To activate the virtual environment, run the command:

`workon test`

5. To leave the environment
Run:

`deactivate`

## Steps to compile and execute the project:

1. Download and Install python in the system (must be python 3 | preferably python version 3.9.6)
2. Ensure python is properly installed by running the following command from command prompt.

`python --version`

3. Download and install git in the system from the git official website
4. Ensure that git is properly installed by running the following command

`git --version`

5. Now inside any folder run the following command through command prompt / terminal:

`git clone https://github.com/adaksritiman24/Online-Doctor-Appointment-System.git`

This should clone the remote repository with necessary project files into the current folder

6. Now, open the cloned repository and move into the ‘odas’ folder. Open command prompt / terminal here and run the following command: 

`pip install -r ../requirements.txt`

This will install all the dependencies to run the project

7. Now the project is ready to be run. Type the following command to runs the server in local machine.

`python manage.py runserver`

8. The server is now running. Open any browser and type the URL – http://localhost:8000
to open the website of Online doctor appointment System 

9.  Following are the two main URLs:
A. http://localhost:8000   Index page for patients 
B. http://localhost:8000/doc  Index page for doctors

10. To stop the server, type Ctrl+c in the command prompt / terminal.


