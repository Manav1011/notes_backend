# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Set environment variables
# ENV SECRET_KEY="&o)w8#lzaqzk*o&hmh3e^6p&2mh8xf_1o2q5a-!h#b!@jq$nka"   
# ENV EMAIL_HOST_PASSWORD="icazovxlqsauknfe"
# ENV EMAIL_HOST_USER="forythononlymanavshah@gmail.com"

# Expose the port the app runs on
EXPOSE 8000

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations, flush database, collect static files, and start the server
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py flush --noinput && \
    python manage.py collectstatic --noinput

# Define the command to run the application

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]