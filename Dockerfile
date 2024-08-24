FROM python:3.9-alpine

WORKDIR /code

# Copy only the necessary files
COPY requirements.txt .
COPY main.py .

# Install any dependencies
RUN pip install -r requirements.txt

# Run your application
CMD ["python", "main.py"]
