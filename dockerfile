#Use official python image
from python:3.11-slim

# Set working directory
workdir /app

#copy all the files to container
copy . .

#command to run Python file
cmd ["python","student.py"]