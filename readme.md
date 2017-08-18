This is api-server project.

### Start
```
mkdir api-server
mkdir api-server/app
mkdir api-server/app/templates
mkdir api-server/app/static
touch api-server/app/__init__.py
touch api-server/run.py
touch api-server/config.py
cd api-server
virtualenv -p python3 env
```

Current Structure
```
~/flask-startkit
  |_ run.py     # to start the flask server, launch app
  |_ config.py  # contains the configuration variables for app 
  |_ /env  # virtual environment
  |_ /app  # my project folder
      |_ __init.__.py  # initialize a python module
      |_ /templates
      |_ /static
      |_ views.py    # contains routes for app
      |_ models.py  # database table define file
```

installing Flask, app dependencies
```
cd ~/flask-startkit
source env/bin/activate
(deactivate) # just deactivate
env/bin/pip install flask
env/bin/pip install ...
pip freeze > requirements.txt # installed pip packages list
((env) $ pip install -r requerements.txt) # after, install all package in another env 
```

start
```
(env) $ cd ~/flask-startkit
(env) $ python3 run.py
``