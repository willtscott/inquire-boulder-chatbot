# Use an official Python runtime as a parent image
FROM python:3.7.2-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY ../../data/interim/faq-text-separated.csv /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install python-dotenv
RUN python -m nltk.downloader wordnet

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "main.py"]
