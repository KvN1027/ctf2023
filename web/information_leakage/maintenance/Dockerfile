FROM php:7.4-apache

COPY custom-apache.conf /etc/apache2/conf-available/custom-apache.conf
RUN ln -s /etc/apache2/conf-available/custom-apache.conf /etc/apache2/conf-enabled/custom-apache.conf

ADD src /var/www/html
EXPOSE 80