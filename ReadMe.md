# how to run the Django App: 


## 1- install python3
- <a href="https://www.python.org/downloads/"> Download Python </a>
- make sure the version is the correct version by issuing the below command in the terminal - FYI - doesnt matter which folder you are on: <br>
<code> python3 --version </code>
<br>
it should be as follow:<br>
<code> Python 3.9.5 </code>
 

## 2- install the virtual environment - FYI - doesnt matter which folder you are on
* <code> pip3 install pipenv </code>

## 3- Install Django
* After Cloning the Repo, Navigate to the GroceryList Folder, and type: <br>
<code> pipenv install django </code>

## 4- Activate the Virtual Environment (venv)
* to activate the virtual environment, follow the below steps: <br>
<code>
cd Desktop <br>
cd GroceryList <br>
source venv/bin/activate <br>
</code>
(venv) will apear behind the terminal prompt if the virtual environment is activated properly

## 5- Run the Django Server
* while on the project directory, issue the following command: <br>
<code> python manage.py runserver </code>

## Opening the app on the browser
* open your browser and enter <br>
<code>http://localhost:8000 </code>

<hr> </hr>

# Pushing the changes to GitHub and Heroku 
* on the project directory issue the below commands: <br>

<code>
git add . <br>
git commit -m "[msg]" <br>
git push origin main <br>
git push heroku main <br>
</code>


