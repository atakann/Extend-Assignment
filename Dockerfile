FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt requirements.txt

# Install app dependencies
RUN pip install -r requirements.txt

# Copy app code into container
COPY . .

# Expose port
EXPOSE 5000

# Start app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]