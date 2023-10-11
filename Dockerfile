FROM python:3.11

WORKDIR /app

COPY . .

ENV TZ=America/Sao_Paulo

ENV SECRET_KEY = 'django-insecure-n0f-98^ghv8y89b=!xl4*8h6l^cdd67+_gle=er_2+&ojh%v#b'

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]