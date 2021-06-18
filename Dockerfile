FROM python:3

RUN mkdir -p /vat/www/project
WORKDIR /var/www/project

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000

CMD [ "python3", "./proj.py" ]
