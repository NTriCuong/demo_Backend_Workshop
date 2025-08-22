# đay là file hướng dẫn tạo image docker 
# 1. Sử dụng image cơ sở là Python 3.13.3 trên nền tảng ARM64 dành cho mac silicon
FROM --platform=linux/arm64 python:3.13.3
# 2. Thiết lập thư mục làm việc bên trong container
WORKDIR /app
# 3. Copy toàn bộ code từ máy host (Mac) vào container
COPY . .
# 4. Cài đặt Django và các thư viện cần thiết cài django và djangorestframework
RUN pip install --no-cache-dir django djangorestframework
# 5. Mở cổng 8080 để truy cập ứng dụng Django
EXPOSE 8080
# 6. Chạy lệnh để khởi động ứng dụng Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
