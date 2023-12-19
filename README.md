# Airplane Python Task

This Django project implements a RESTful API for managing information about 10 different cars. Each car is characterized by its engine capacity, fuel efficiency, and passenger capacity.

## Requirements

To run this project, you will need the following:

- Python 3.x

## Setup Instructions

1. Clone the repository
```shell
git clone https://github.com/galisufyan-327/airplane-python-task.git
```

2. Create a virtual environment (recommended but optional):
```shell
python -m venv venv
```

3. Install the required Python packages:
```shell
pip install -r requirements.txt
```

4. Run the Django migrations:
```shell
python manage.py migrate
```


## Usage

To start the Django development server, run the following command:
```shell
python manage.py runserver
```

The API will be accessible at http://127.0.0.1:8000/api/airplanes/.

You can use any API endpoint testing tool, such as Postman, by sending a POST request to the above endpoint with the request body format as follows:

```
[    {"id": 1, "passengers": 4},    {"id": 2, "passengers": 5},    {"id": 3, "passengers": 6},]
```

## Running Tests

- To run tests and check coverage, use the following commands:

```shell
python3 -m coverage run manage.py test
coverage report
```


