import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("processing/phongtro_processed_with_duration.csv")

# Kiểm tra dữ liệu
# print("Thông tin về dataset:")
# print(df.info())

# print("\nHiển thị 5 dòng đầu của dataset:")
# print(df.head())

# Kiểm tra thông tin cơ bản về cột 'duration_days'
# print("Thông tin cơ bản về cột 'duration_days':")
# print(df['duration_days'].describe())


# Kiểm tra xem có giá trị NaN trong cột 'duration_days' không
nan_count = df['duration_days'].isna().sum()
print(f"\nSố lượng giá trị NaN trong cột 'duration_days': {nan_count}")

# Hiển thị các giá trị duy nhất trong cột 'duration_days'
unique_values = df['duration_days'].unique()
print("\nCác giá trị duy nhất trong cột 'duration_days':")
print(unique_values)