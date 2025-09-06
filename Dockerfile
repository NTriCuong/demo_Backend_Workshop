# syntax=docker/dockerfile:1
FROM python:3.13-slim

# Log ra ngay & không tạo .pyc
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Lib hệ thống để build mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev build-essential pkg-config \
 && rm -rf /var/lib/apt/lists/*

# Cài Python deps từ requirements.txt (hãy đảm bảo đã có drf-spectacular hoặc drf-yasg ở đây nếu bạn dùng)
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Mở cổng dev server
EXPOSE 8080

# Chạy Django dev server (phù hợp môi trường dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
