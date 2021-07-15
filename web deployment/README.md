# Recognition

Các bước thực hiện:

- Bước 1: Clone Respository về:
  `git clone https://github.com/latruonghai/Recognition && cd Recognition`
- Bước 2: Tạo môi trường ảo:
  - Với conda:

    `conda env create -f environment.yml && conda activate recognition && pip3 install requirements.txt`

  - Với `virtualenv`:
    `virtualenv recognition`
    Với Windows:
    `regconition/Scripts/activate`
- Bước 3: Cài đặt thư viện
  - Với ubuntu:
    `pip3 install -r requirements.txt`
- Bước 4: Khởi chạy chương trình
  `python3 main.py`
