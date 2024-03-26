# 실행 스크립트 (proxy/run.sh)
# 컨테이너가 시작될 때 실행되는 스크립트입니다. 환경 변수를 사용하여 Nginx 구성 파일을 생성하고, Nginx를 실행합니다.
#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'