FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ .

# Expose the application port
EXPOSE 8002

# Command to run the application
CMD ["python", "main_agent.py"]