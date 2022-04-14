FROM python:3.10.4-alpine3.15
ADD main.py /
RUN pip install telethon --no-cache-dir
CMD [ "python", "./main.py" ]