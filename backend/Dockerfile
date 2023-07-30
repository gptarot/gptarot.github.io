# Use the official lightweight Python image. (debian based)
FROM python:3.9-slim-buster 

# Setup working directory
WORKDIR /home
COPY . /home/

# Install production dependencies.
RUN pip install --no-cache-dir -r /home/requirements.txt

# Change permissions
RUN chmod +x /home/api/index.py
RUN chmod +x /home/commands.sh

# Run the web service on container startup.
ENTRYPOINT ["/home/commands.sh"]
EXPOSE 5000