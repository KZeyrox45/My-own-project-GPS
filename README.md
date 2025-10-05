# GPS Target System

Hệ thống tính toán tọa độ mục tiêu dựa trên vị trí quan sát (GPS) và dữ liệu ngắm bắn (góc phương vị, góc ngẩng, khoảng cách).

## Tổng quan

Dự án tập trung vào việc xây dựng thuật toán tính toán tọa độ mục tiêu từ các thông tin đầu vào:
- Tọa độ GPS của người quan sát (vĩ độ, kinh độ, độ cao)
- Góc ngắm (azimuth/phương vị, elevation/ngẩng) từ cảm biến IMU/la bàn
- Khoảng cách đến mục tiêu từ laser rangefinder

Hệ thống chuyển đổi các dữ liệu này thành tọa độ địa lý (kinh độ, vĩ độ, cao độ) của mục tiêu, có thể hiển thị trên bản đồ số.

## Cấu trúc dự án

```
├── core/                   # Module core của hệ thống
│   ├── __init__.py
│   ├── coordinate_transforms.py    # Chuyển đổi hệ tọa độ
│   ├── gps_target_system.py       # Lớp chính của hệ thống
│   ├── sensor_fusion.py           # Xử lý dữ liệu cảm biến
│   └── target_calculator.py       # Tính toán tọa độ mục tiêu
├── visualization/          # Module hiển thị kết quả
│   ├── __init__.py
│   ├── export_utils.py            # Xuất dữ liệu (GeoJSON)
│   ├── map_viewer.py             # Hiển thị bản đồ cơ bản
│   ├── plot_utils.py             # Công cụ vẽ đồ thị
│   └── webmap_viewer.py          # Hiển thị bản đồ web
├── tests/                 # Unit tests
│   └── test_calculations.py      # Kiểm thử tính toán
├── output/                # Thư mục chứa kết quả xuất
├── main.py               # Chương trình chính
└── README.md             # Tài liệu dự án
```

## Tính năng chính

1. **Tính toán tọa độ:**
   - Chuyển đổi góc azimuth/elevation thành vector định hướng 3D
   - Tính toán vị trí mục tiêu từ vector định hướng và khoảng cách
   - Chuyển đổi giữa các hệ tọa độ (ECEF, ENU, NED)

2. **Hiển thị kết quả:**
   - Bản đồ 2D với matplotlib
   - Bản đồ web tương tác (OpenStreetMap)
   - Profile độ cao giữa quan sát viên và mục tiêu

3. **Xuất dữ liệu:**
   - Định dạng GeoJSON cho các phần mềm GIS
   - Bản đồ web HTML có thể chia sẻ

## Yêu cầu hệ thống

- Python 3.8+
- Các thư viện Python:
  ```
  pip install numpy matplotlib folium
  ```

## Cách sử dụng

1. **Cài đặt dependencies:**
   ```bash
   pip install numpy matplotlib folium
   ```

2. **Chạy chương trình:**
   ```bash
   python main.py
   ```

3. **Nhập dữ liệu:**
   - Vị trí quan sát (vĩ độ, kinh độ, độ cao)
   - Góc phương vị (0-360 độ)
   - Góc ngẩng (-90 đến +90 độ)
   - Khoảng cách đến mục tiêu (mét)

4. **Xem kết quả:**
   - Tọa độ mục tiêu sẽ hiển thị trong terminal
   - Đồ thị matplotlib sẽ hiện lên
   - Trình duyệt web sẽ mở bản đồ tương tác
   - Các file kết quả được lưu trong thư mục `output/`

### Ví dụ dữ liệu test

```
=== Nhập thông tin vị trí quan sát ===
Vĩ độ (độ): 10.762622     # Đại học Bách Khoa
Kinh độ (độ): 106.660172
Độ cao (mét): 10

=== Nhập thông tin ngắm ===
Góc phương vị (độ): 45    # Hướng Đông Bắc
Góc ngẩng (độ): 0         # Ngang tầm
Khoảng cách (mét): 1000   # 1km
```

## Kiểm thử

Chạy unit tests:
```bash
python -m unittest tests/test_calculations.py
```

## Kết quả xuất

1. **Terminal:**
   - Tọa độ mục tiêu (lat, lon, alt)
   - Thông báo lỗi nếu có

2. **Matplotlib:**
   - Bản đồ 2D với vị trí quan sát và mục tiêu
   - Profile độ cao

3. **Bản đồ web (output/scenario_map.html):**
   - Bản đồ tương tác OpenStreetMap
   - Marker người quan sát (xanh) và mục tiêu (đỏ)
   - Thông tin chi tiết khi click vào marker:
     - Tọa độ đầy đủ
     - Khoảng cách
     - Góc phương vị
     - Góc ngẩng

4. **GeoJSON (output/scenario.geojson):**
   - Dữ liệu có thể import vào GIS
   - Thông tin đầy đủ về quan sát và mục tiêu

## Phát triển tiếp theo

- [ ] Giao diện đồ họa (GUI)
- [ ] Tích hợp với cảm biến thực
- [ ] Xử lý nhiễu và sai số
- [ ] Hỗ trợ nhiều định dạng xuất khác
- [ ] Real-time tracking và cập nhật
- [ ] Tối ưu hóa thuật toán

## Đóng góp

Mọi đóng góp đều được hoan nghênh. Vui lòng:
1. Fork dự án
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request