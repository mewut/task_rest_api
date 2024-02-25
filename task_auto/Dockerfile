FROM python:3.11.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -ms /bin/bash myuser
USER myuser

WORKDIR /app

COPY . .

RUN python -m venv /home/myuser/venv
RUN /home/myuser/venv/bin/pip install -r requirements.txt
RUN /home/myuser/venv/bin/pip install django

CMD ["/home/myuser/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]