FROM python:3.11-slim

# Setup working environment
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN chmod +x /app/commands.sh

# Clean up unnecessary files and folders to reduce the image size
RUN echo "==> Clean up unnecessary files..."
RUN apt-get update && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /app/requirements.txt /app/Dockerfile /app/docker-compose.yaml

# Print out the success message
RUN echo "==> Successfully built the image."
RUN echo "==> About to start the gunicorn server..."

# Run the web service on container startup.
ENTRYPOINT ["/app/commands.sh"]
EXPOSE 5000