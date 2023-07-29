FROM python:3.9-alpine
WORKDIR /home
COPY . /home/
RUN apk add --no-cache bash curl
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/requirements.txt
RUN chmod +x /home/api/index.py
RUN chmod +x /home/commands.sh
ENTRYPOINT ["/home/commands.sh"]
EXPOSE 5000