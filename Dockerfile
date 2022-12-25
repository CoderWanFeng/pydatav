FROM ubuntu

ENV pydatav /opt/pydatav/
# 进入容器时的路径
WORKDIR $pydatav
# 代码挂在此处
VOLUME $pydatav
COPY ./ $pydatav
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
RUN apt-get update
RUN apt install python3-pip -y
RUN apt-get install nginx -y

# 安装依赖环境
RUN pip3 install -r $pydatav/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 修改nginx配置
COPY nginx/nginx.conf /etc/nginx/

EXPOSE 80
#CMD /usr/sbin/nginx

CMD /bin/bash
