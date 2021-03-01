FROM python:3 as build

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

FROM build as test

RUN python3 -m unittest test_main.py

FROM test as run

CMD [ "python3", "main.py"]