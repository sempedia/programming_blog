# Build a Blog Using Django, Vue, and GraphQL

Install the project on your machine by following the steps outlined below.

## Setup

### Back End

Create a new terminal window, navigate into `back_end/`, create, activate a virtual environment, and install the necessary dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Then, create the initial Django database by running migrations:

```sh
$ python manage.py migrate
```

Create a Django superuser:

```shell
$ python manage.py createsuperuser
```

Run the Django project:

```sh
$ python manage.py runserver
```

Before continuing, it's a good idea to create some users, profiles, and blog posts in the Django admin interface at `http://localhost:8000/admin`. You must use your superuser credentials to log in.

You can visit the GraphiQL platform `http://localhost:8000/graphql` to try out GraphQL queries.

### Front End

Open a new terminal and navigate into `front_end/`. Then, install the front-end requirements:

```sh
$ npm install --include dev
```

Run the Vite development server:

```sh
$ npm run dev
```

You must have the Django development server and the Vite server running at the same time.
