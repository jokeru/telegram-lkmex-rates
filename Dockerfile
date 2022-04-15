FROM python:3.10.4-alpine3.15
COPY main.py /
RUN pip install telethon==1.24.0 --no-cache-dir
CMD [ "python", "./main.py" ]
