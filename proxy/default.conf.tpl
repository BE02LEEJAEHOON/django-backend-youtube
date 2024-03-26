# Nginx 서버 구성 템플릿 (proxy/default.conf.tpl)
# 실제 Nginx 구성 파일을 생성하기 위한 템플릿입니다. 환경 변수를 통해 유연하게 구성을 변경할 수 있습니다.

server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}