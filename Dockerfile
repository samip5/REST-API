# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3.7

LABEL mainainer="sm+docker@samip.fi"

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
ENV MAIN /main

# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir -p $MAIN/$APP
WORKDIR $MAIN

# Expose the port uWSGI will listen on
EXPOSE 80

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# We copy the rest of the codebase into the image
COPY . .

# Finally, we run uWSGI with the ini file we
# created earlier
CMD [ "uwsgi", "--ini", "configs/app.ini", "--enable-threads"]
