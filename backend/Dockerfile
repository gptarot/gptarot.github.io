FROM python:3.10.6-slim-buster

# Setup working environment
WORKDIR /home
COPY . /home/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/requirements.txt
RUN chmod +x /home/api/index.py
RUN chmod +x /home/commands.sh

# Clean up unnecessary files and folders to reduce the image size
RUN echo "==> Clean up unnecessary files..."
RUN apt-get autoremove \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /home/requirements.txt /home/Dockerfile

# Print out the success message
RUN echo "==> Successfully built the image."
RUN echo "==> About to start the gunicorn server..."

# Run the web service on container startup.
ENTRYPOINT ["/home/commands.sh"]
EXPOSE 5000