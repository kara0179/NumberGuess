# Use the official Python image from the Docker Hub
FROM python:3.9-slim

ADD numberguess.py .

# Run the application
CMD ["python", "numberguess.py"]
