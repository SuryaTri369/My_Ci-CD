# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY app.py .
COPY test_app.py .

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
