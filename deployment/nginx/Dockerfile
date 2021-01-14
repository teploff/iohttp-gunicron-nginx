FROM nginx:stable-alpine

MAINTAINER Alexander Teplov <teplov_aa@rtsoft.ru>
LABEL maintainer="teplov_aa@rtsoft.ru"

#RUN rm /etc/nginx/conf.d/default.conf

ADD nginx.conf /etc/nginx/nginx.conf
COPY sites-enabled /etc/nginx/sites-enabled

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]