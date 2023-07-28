FROM ubuntu:latest
USER root
RUN apt-get update -y
RUN apt-get install -y net-tools
RUN apt-get install -y python3 python3-pip
COPY .  /home
RUN pip3 install -r /home/requirements.txt
WORKDIR /home
RUN chmod +x /home/api/index.py
RUN chmod +x /home/commands.sh
ENTRYPOINT ["/home/commands.sh"]
EXPOSE 3000 5050 5000