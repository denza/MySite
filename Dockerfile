# Metadata
FROM 		python:3.6

# Setting up directories
RUN 		mkdir -p /opt/mysite
WORKDIR 	/opt/mysite
ADD 		requirements.txt /opt/mysite/

# Install dependencies
RUN  		pip install -r requirements.txt
ADD 		. /opt/mysite/

EXPOSE 8000

# Boot the app
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
