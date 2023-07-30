FROM python:3.9-slim-buster 
WORKDIR /home
COPY . /home/
RUN pip install --no-cache-dir -r /home/requirements.txt
RUN chmod +x /home/api/index.py
RUN chmod +x /home/commands.sh
ENTRYPOINT ["/home/commands.sh"]
EXPOSE 5000