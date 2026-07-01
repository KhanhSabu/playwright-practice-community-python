# 🚀 Dự án Thực hành Playwright E-Commerce (Python Version)

Chào mừng các bạn đến với phiên bản Python của dự án thực hành kiểm thử tự động sử dụng **Playwright** và **Pytest**!

🔗 **Website thực hành:** [https://e-commerce-dev.betterbytesvn.com/](https://e-commerce-dev.betterbytesvn.com/)

---

## 📂 Cấu trúc thư mục (Folder Structure)

Dự án được tổ chức theo cấu trúc chuẩn như sau:

```text
├── src/
│   ├── components/       # Các component dùng chung trên giao diện
│   ├── config/           # Cấu hình hệ thống, môi trường
│   ├── data/             # Dữ liệu phục vụ kiểm thử (test data)
│   └── pages/            # Các Page Object Model (POM) đại diện cho các trang
│       ├── base_page.py
│       └── home/
│           └── home_page.py
├── tests/                # Chứa các kịch bản kiểm thử (Test Cases)
│   ├── conftest.py       # Khai báo pytest fixtures dùng chung
│   ├── blog/
│   ├── home/
│   │   └── test_home.py
│   ├── search/
│   └── shop/
├── docs/                 # Tài liệu hướng dẫn, ghi chú của dự án
├── .env.example          # File mẫu biến môi trường
├── pytest.ini            # Cấu hình pytest
└── requirements.txt      # Định nghĩa các thư viện Python phụ thuộc
```

---

## 🛠️ Hướng dẫn Chạy Test locally

Để cài đặt và chạy test trên máy cá nhân, vui lòng thực hiện theo các bước sau:

### 1. Tạo môi trường ảo (Virtual Environment)
```bash
# Tạo môi trường ảo .venv
python3 -m venv .venv

# Kích hoạt môi trường ảo (Linux/macOS)
source .venv/bin/activate

# Kích hoạt môi trường ảo (Windows Command Prompt)
# .venv\Scripts\activate.bat

# Kích hoạt môi trường ảo (Windows PowerShell)
# .venv\Scripts\Activate.ps1
```

### 2. Cài đặt thư viện & Playwright Browsers
```bash
# Cài đặt các thư viện cần thiết từ requirements.txt
pip install -r requirements.txt

# Cài đặt trình duyệt cho Playwright
playwright install
```

### 3. Cấu hình biến môi trường
Sao chép file `.env.example` thành `.env`:
```bash
cp .env.example .env
```
Đảm bảo giá trị `BASE_URL` trong file `.env` trỏ đúng tới địa chỉ website cần test:
```env
BASE_URL=https://e-commerce-dev.betterbytesvn.com/
```

### 4. Chạy kịch bản test
Sử dụng `pytest` để chạy các kịch bản kiểm thử:
```bash
# Chạy toàn bộ test
pytest

# Chạy test và hiển thị trình duyệt (Headed mode)
pytest --headed

# Chạy cụ thể một file test
pytest tests/home/test_home.py

# Chạy test theo tag (marker)
pytest -m SAMPLE_20260701
```

---

## 📐 Coding Conventions

Để giữ cho mã nguồn luôn sạch sẽ, dễ đọc và dễ bảo trì, vui lòng tuân thủ các quy định đặt tên theo chuẩn PEP 8:

### 1. File & Folder Names
- Sử dụng dạng **`snake_case`** (viết thường, ngăn cách bằng dấu gạch dưới).
- *Ví dụ:* `login_page.py`, `test_home.py`.

### 2. Variables & Functions Names
- Sử dụng dạng **`snake_case`**.
- *Ví dụ:* `login_button = ...`, `def click_submit_button():`.

### 3. Class Names
- Sử dụng dạng **`PascalCase`** (viết hoa chữ cái đầu của tất cả các từ).
- *Ví dụ:* `class LoginPage:`, `class HomePage(BasePage):`.

### 4. Constants Names
- Sử dụng dạng **`SCREAMING_SNAKE_CASE`** (viết hoa toàn bộ, ngăn cách bằng dấu gạch dưới).
- *Ví dụ:* `BASE_URL = ...`.

---

## 🌿 Git Convention

### 1. Quy tắc đặt tên Branch
Trước khi đẩy code, vui lòng đặt tên nhánh (branch) theo định dạng:
```text
QA-{ten-ban}-{challenge-number}
```
*Ví dụ:*
- `QA-alex-challenge-1`

### 2. Quy tắc viết Commit Message
Sử dụng các tiền tố chuẩn sau cho commit message:
- **`feat:`** Thêm test case mới hoặc viết thêm tính năng.
- **`fix:`** Sửa lỗi, cập nhật locator, sửa logic test.
- **`chore:`** Cập nhật tài liệu (README, docs), file cấu hình hoặc dọn dẹp code.

*Ví dụ:*
- `feat: add sample verification test`
- `fix: refactor locator of homepage`
- `chore: update readme with git convention`
