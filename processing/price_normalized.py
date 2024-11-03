import pandas as pd 
import numpy as np

#Đọc dữ liệu từ file csv 
df = pd.read_csv("processing/phongtro_processed_only_phongtro.csv")
#process data with 'price' column

#xem các giá trị duy nhất trong cột 'price'
unique_prices = df['price'].unique()
print("\nCác giá trị duy nhất trong cột 'price':")
print(unique_prices)
#count mỗi giá trị duy nhất nếu cần 
price_counts = df['price'].value_counts() 
print("\nSố lần xuất hiện của mỗi giá trị trong cột 'price':")  
# Xử lý cột 'price'
def convert_price(value):
    if pd.isna(value):
        return np.nan
    elif "triệu/tháng" in value:
        return float(value.replace(" triệu/tháng", ""))
    elif "đồng/tháng" in value:
        # Chuyển từ đồng sang triệu bằng cách chia cho 1,000,000
        return float(value.replace(" đồng/tháng", "").replace(".", "")) / 1_000_000
    elif "Thỏa thuận" in value:
        return np.nan  # Đặt giá trị NaN cho "Thỏa thuận" vì không thể chuyển đổi
    else:
        return np.nan  # Đặt NaN cho bất kỳ giá trị không hợp lệ nào

# Áp dụng hàm convert_price vào cột 'price'
df['price'] = df['price'].apply(convert_price)

# Loại bỏ các giá trị NaN trong cột 'price' (nếu cần) để tính toán chính xác
df_cleaned = df.dropna(subset=['price'])

# Thực hiện các phép thống kê cơ bản trên cột 'price'
print("Thống kê về giá thuê (triệu/tháng):")
print(df_cleaned['price'].describe())

# Kiểm tra phân phối giá trị trong cột 'price'
price_distribution = df_cleaned['price'].value_counts().sort_index()
print("\nPhân phối các giá trị trong cột 'price':")
print(price_distribution)

# Lưu lại DataFrame đã chuẩn hóa và thống kê vào file mới
df_cleaned.to_csv("processing/phongtro_price_statistics.csv", index=False)
print("Dữ liệu đã được chuẩn hóa và lưu vào file phongtro_price_statistics.csv")
