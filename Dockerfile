# Use an official Python runtime as the base image
FROM python:3.9

WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt /app/
# Install project dependencies
RUN pip install -r requirements.txt
# Copy the rest of the application code to the container
COPY . /app/
# Expose the port that the Django development server will run on
EXPOSE 8000
# Define the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]