import pandas as pd

try:
    # Đọc dữ liệu từ file JSON
    df = pd.read_json('phongtro/spiders/phongtro.json', lines=True)
except ValueError as e:
    print(f"Error reading JSON file: {e}")
    df = pd.DataFrame()

# Xóa các cột không cần thiết
df = df.drop(columns=['description', 'phone_number', 'title'], errors='ignore')

# Loại bỏ từ "Địa chỉ: " trong cột 'address'
df['address'] = df['address'].str.replace("Địa chỉ: ", "", regex=False)

# Tách cột 'address' thành các phần tối đa là bốn cột
df[['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']] = df['address'].str.split(',', n=3, expand=True)

# Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi trong từng cột mới
df['Đường'] = df['Đường'].str.strip()
df['Phường'] = df['Phường'].str.strip()
df['Quận/Huyện'] = df['Quận/Huyện'].str.strip()
df['Thành phố'] = df['Thành phố'].str.strip()

# Xóa cột 'address' sau khi đã phân tách
df = df.drop(columns=['address'], errors='ignore')

# Xử lý 'public_date' và 'expired_date' để loại bỏ phần "Thứ X, "
df['public_date'] = df['public_date'].str.replace(r"^Thứ \w+, ", "", regex=True)
df['expired_date'] = df['expired_date'].str.replace(r"^Thứ \w+, ", "", regex=True)

# Chuyển đổi 'public_date' và 'expired_date' thành kiểu datetime
df['public_date'] = pd.to_datetime(df['public_date'], format="%H:%M %d/%m/%Y", errors='coerce')
df['expired_date'] = pd.to_datetime(df['expired_date'], format="%H:%M %d/%m/%Y", errors='coerce')

# Tính số ngày giữa 'expired_date' và 'public_date'
df['duration_days'] = (df['expired_date'] - df['public_date']).dt.days

# Đưa các cột mới lên đầu
columns_order = ['Đường', 'Phường', 'Quận/Huyện', 'Thành phố', 'duration_days'] + [col for col in df.columns if col not in ['Đường', 'Phường', 'Quận/Huyện', 'Thành phố', 'duration_days']]
df = df[columns_order]

# Lưu lại DataFrame vào file mới trong thư mục 'processing'
df.to_csv("processing/phongtro_processed_with_duration.csv", index=False)

print("Dữ liệu đã được xử lý, thời hạn bài đăng đã được tính và lưu vào file phongtro_processed_with_duration.csv trong thư mục processing")
