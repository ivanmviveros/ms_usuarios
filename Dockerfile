FROM ubuntu:16.04

WORKDIR .
COPY requirements.txt ./
COPY . /var/www/html/ms_usuarios
COPY ./_datos_iniciales/settings_inicial.py /var/www/html/ms_usuarios/ms_usuarios/settings.py
COPY ./_datos_iniciales/secrets_inicial.json /var/www/html/ms_usuarios/ms_usuarios/secrets.json

RUN echo "nameserver 172.18.0.1" >> /etc/resolv.conf && apt-get update && apt-get install -y --no-install-recommends apache2 apache2-utils python3 python3-setuptools libapache2-mod-wsgi-py3 python3-pip git && rm -rf /var/lib/apt/lists/* && ln /usr/bin/python3 /usr/bin/python && ln /usr/bin/pip3 /usr/bin/pip
RUN echo "nameserver 172.18.0.1" >> /etc/resolv.conf && pip install --upgrade pip
RUN echo "nameserver 172.18.0.1" >> /etc/resolv.conf && pip install -r requirements.txt && apt-get -y remove git

COPY ./_datos_iniciales/apache-conf.conf /etc/apache2/sites-available/000-default.conf

RUN mkdir -p /var/www/html/ms_usuarios/static_collected
RUN python3 /var/www/html/ms_usuarios/manage.py collectstatic --noinput
RUN mkdir -p /var/www/html/media
VOLUME /var/www/html/media

EXPOSE 80 8001
CMD ["apache2ctl", "-D", "FOREGROUND"]