# Django Todo REST APIs

This repository contains a Django-based application that provides REST APIs for managing todo tasks. With this APIs, you can create, read, update, and delete tasks, as well as mark tasks as completed or incomplete.

## Features

- Create a new task.
- Retrieve a list of all tasks.
- Retrieve a single task by its ID.
- Update a task's title and description.
- Mark a task as completed or incomplete.
- Delete a task.

## Installation

1. Clone this repository to your local machine:

```shell
git clone https://github.com/sohitdeveloper/docker-todo-app-django.git
```

2. Navigate to the project directory:

```shell
cd docker-todo-app-django
```

3. Create a virtual environment (optional but recommended):

```shell
python -m venv venv
```

4. Activate the virtual environment:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the project dependencies:

```shell
pip install -r requirements.txt
```

6. Apply the database migrations:

```shell
python manage.py migrate
```

7. Start the development server:

```shell
python manage.py runserver
```

The API will be accessible at `http://localhost:8000/`.

## Authentication and Authorization

This API uses token-based authentication to secure endpoints. You should ensure that your token is kept secret. Additionally, the API includes basic authorization to ensure that only the task owner can update or delete a task.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. Feel free to open issues for bug reports or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
