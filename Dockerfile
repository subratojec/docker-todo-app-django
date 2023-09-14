# Stage 1: Build the application
FROM python:3.9 AS builder

WORKDIR /app

# Copy the requirements file to the container 
COPY requirements.txt /app/

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code to the container
COPY . /app/

# Stage 2: Create runtime image
FROM python:3.9-slim

WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app

# Expose the port that the Django development server will run on
EXPOSE 8000

# Define the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]