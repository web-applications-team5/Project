# Web Applications - Project [Team5]

1) Sri Akhila Kathari
2) Swetha Busireddy
3) Yashwanth Chegireddy
4) Rakesh Matta

### Basic steps
Install virtualenv if missing

> ```pip install virtualenv``` 

Run the below command inside the project to crete virtualEnv inside project

> ```virtualenv venv```

For Mac or Linux
```source venv/bin/activate```

For Windows
```venv\Scripts\activate.bat```

----

## Swagger 

Use https://editor.swagger.io to view api.

On the page paste the swagger.yaml from the project.


### Create requirements file 

(needed only while development)

> ```pip freeze > requirements.txt```

This file needs to be committed.

----

### Install required dependencies

> ```pip install -r requirements.txt```

----

## Create DB and seed test data

Run the migrations.py file 
> ```python migrations.py```

----

## Running the application

1. Run without docker

    Run the run.py file
    > ```python run.py```
    
2. Run using docker

    Build image from the Dockerfile
    > ```docker build -t restaurant-food-order:latest . ```
    
    Create container from the above image and run the container
    > ```docker run -d -p 5000:5000 restaurant-food-order```
    
> App can be accessed under URL : http://localhost:5000


## DB Operations

(useful when testing and using python console)

Create DB tables from entity models

(Run this in the python console inside the project)
```
 from yourapplication import db
 db.create_all()
```

Create records and save to DB

(Run this in the python console inside the project)
```
 from yourapplication import User
 admin = User(username='admin', email='admin@example.com')
 guest = User(username='guest', email='guest@example.com')

 db.session.add(admin)
 db.session.add(guest)
 db.session.commit()
```