import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv("processing/phongtro_price_statistics.csv")

# Đếm số lượng các giá trị duy nhất trong cột "Quận/Huyện"
district_counts = df['Quận/Huyện'].value_counts()

# Vẽ biểu đồ cột
# plt.figure(figsize=(10, 6))
# district_counts.plot(kind='bar')
# plt.title("Số lượng các giá trị duy nhất trong cột 'Quận/Huyện'")
# plt.xlabel("Quận/Huyện")
# plt.ylabel("Số lượng")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()
# # Hiển thị kết quả
print("Số lượng các giá trị duy nhất trong cột 'Quận/Huyện':")
print(district_counts)
