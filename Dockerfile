# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#Expose the port 8080
EXPOSE 80
# Run app.py when the container launches
CMD ["python", "app.py"]
