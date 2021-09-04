# how to run the Django App: 


## 1- install python3
- <a href="https://www.python.org/downloads/"> Download Python </a>
- make sure the version is the correct version by issuing the below command in the terminal - FYI - doesnt matter which folder you are on: <br>
`python3 --version`
<br>
it should be as follow:<br>
`Python 3.9.5`
 

## 2- install the virtual environment - FYI - doesnt matter which folder you are on
* ` pip3 install pipenv `

## 3- Install Django
* After Cloning the Repo, Navigate to the GroceryList Folder, and type: <br>
`pipenv install django`

## 4- Activate the Virtual Environment (venv)
* to activate the virtual environment, follow the below steps: <br>
```
cd Desktop 
cd GroceryList
source venv/bin/activate 
```
`(venv)` will apear behind the terminal prompt if the virtual environment is activated properly

## 5- Run the Django Server
* while on the project directory, issue the following command: <br>
` python manage.py runserver`

## Opening the app on the browser
* open your browser and enter <br>
`http://localhost:8000 `

<hr> </hr>

# Pushing the changes to GitHub and Heroku 
* on the project directory issue the below commands: <br>

```
git add . 
git commit -m "[msg]"
git push origin main 
git push heroku main 
```


