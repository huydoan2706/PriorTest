FROM python:3.11

WORKDIR /app

# Cài đặt công cụ uv
RUN pip install uv

# Copy file cấu hình thư viện và cài đặt
COPY pyproject.toml uv.lock ./
RUN uv pip install --system -e .

# Copy toàn bộ source code
COPY . .

