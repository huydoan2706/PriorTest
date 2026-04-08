# Cách chạy chương trình

## Bước 1: Chạy terminal và truy cập vào folder Day4567

`cd ~/duong/dan/PriorTest/Day4567`

## Bước 2:

### Nếu chạy local: 

Gõ dòng code dưới đây để chạy backend:

`uv run ./main.py`

Sau đó giữ nguyên hiện trạng của terminal đang chạy backend;
Thêm 1 terminal mới, truy cập vào folder Day4567 như Bước 1,
sau đó gõ dòng code dưới đây:

`uv run streamlit run frontend_local.py`

### Nếu sử dụng Docker để chạy:

Gõ dòng code dưới đây để chạy cả backend lẫn frontend:

`docker compose up --build`

