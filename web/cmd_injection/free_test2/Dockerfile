FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY src /app
COPY flag /
RUN chmod 444 /flag

# 安装依赖
RUN pip3 install -r requirements.txt