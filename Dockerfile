FROM python:3.10

RUN apt update


RUN mkdir /hub

WORKDIR /hub

COPY /src ./
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["python", "manage.py", "runserver", "0:8008"]

# docker run --rm -d -p 8000:8008 --name vol_hub hub
# docker logs -f vol_hub
# localhost:8000