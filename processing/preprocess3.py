import pandas as pd

# Đường dẫn tới file CSV
file_path = 'phongtro_price_statistics.csv'  # Đảm bảo file CSV nằm trong cùng thư mục với file Python này

# Tải dữ liệu từ file CSV
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{file_path}'. Hãy kiểm tra lại đường dẫn tới file CSV.")
    exit()

# Bước 1: Xóa các hàng có cột "Quận/Huyện" chứa "Thành phố Hồ Chí Minh"
df = df[~df['Quận/Huyện'].str.contains("Thành phố Hồ Chí Minh", case=False, na=False)]

# Bước 2: Chuyển đổi cột 'acreage' sang kiểu số thực (float) bằng cách loại bỏ ký tự "m"
df['acreage'] = df['acreage'].str.replace('m', '').astype(float)

# Bước 3: Định nghĩa tên cột tiếng Việt và tiếng Anh
column_translations_vietnamese = {
    "Đường": "Đường",
    "Phường": "Phường",
    "Quận/Huyện": "Quận/Huyện",
    "Thành phố": "Thành phố",
    "duration_days": "số ngày",
    "price": "giá",
    "acreage": "diện tích",
    "package": "gói",
    "category": "thể loại",
    "public_date": "ngày đăng",
    "expired_date": "ngày hết hạn",
    "ad_type": "loại quảng cáo",
    "target_renter": "đối tượng thuê"
}

column_translations_english = {
    "Đường": "Street",
    "Phường": "Ward",
    "Quận/Huyện": "District",
    "Thành phố": "City",
    "duration_days": "DurationDays",
    "price": "Price",
    "acreage": "Acreage",
    "package": "Package",
    "category": "Category",
    "public_date": "PublicDate",
    "expired_date": "ExpiredDate",
    "ad_type": "AdType",
    "target_renter": "TargetRenter"
}

# Tạo phiên bản tiếng Việt với tên cột tiếng Việt
df_vietnamese = df.rename(columns=column_translations_vietnamese)

# Tạo phiên bản tiếng Anh với tên cột tiếng Anh
df_english = df.rename(columns=column_translations_english)

# Lưu các tập dữ liệu đã xử lý thành hai file CSV riêng biệt
df_vietnamese.to_csv('vietnamese_version_dataset.csv', index=False)  # Tập dữ liệu tiếng Việt
df_english.to_csv('english_version_dataset.csv', index=False)  # Tập dữ liệu tiếng Anh

print("Quá trình xử lý hoàn tất. Đã tạo hai file 'vietnamese_version_dataset.csv' và 'english_version_dataset.csv'.")
