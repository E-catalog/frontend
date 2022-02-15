# Frontend

## About

![Conceptual schema of E-catalog](https://github.com/daria-veselkova/frontend/raw/main/frontend/app_schema.drawio.png)

This repository contains files of E-catalog frontend application. Two main parts of the app - the user web interface and the API client which connects to the backend app and DB. You can get or push data from/to the database with simple CRUD operations of the API. They are similar for two basic instanses - Places and Individuals:

```
# get all places
GET http://{backend_address}:5000/api/v1/places/

# get a particular place
GET http://{backend_address}:5000/api/v1/places/<uid>

# create a place
POST http://{backend_address}:5000/api/v1/places/

# update a particular place
PUT http://{backend_address}:5000/api/v1/places/<uid>

# delete a particular place
DELETE http://{backend_address}:5000/api/v1/places/<uid>

# get all individuals
GET http://{backend_address}:5000/api/v1/individuals

# get a particular individual
GET http://{backend_address}:5000/api/v1/individuals/<uid>

# create an individual
POST http://{backend_address}:5000/api/v1/individuals/

# update a particular individual
PUT http://{backend_address}:5000/api/v1/individuals/<uid>

# delete a particular individual
DELETE http://{backend_address}:5000/api/v1/individuals/<uid>
```

