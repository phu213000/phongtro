import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("processing/phongtro_processed_with_duration.csv")

# Loại bỏ cụm từ ", nhà trọ" trong cột 'ad_type'
df['ad_type'] = df['ad_type'].str.replace(", nhà trọ", "", regex=False)

# Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi trong cột 'ad_type'
df['ad_type'] = df['ad_type'].str.strip()

# Lưu lại DataFrame vào file mới
df.to_csv("processing/phongtro_processed_only_phongtro.csv", index=False)

print("Đã xóa ', nhà trọ' trong cột 'ad_type' và lưu vào file phongtro_processed_only_phongtro.csv")
