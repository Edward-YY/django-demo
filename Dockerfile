FROM python:3.8.20

# 设置工作目录
WORKDIR /app

# 复制项目的 requirements.txt 到工作目录
COPY requirements.txt /app/

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到容器
COPY . /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露 Django 默认端口
EXPOSE 8000

# 运行 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



