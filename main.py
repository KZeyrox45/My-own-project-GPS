"""
main.py
Chương trình chính để demo tính năng của hệ thống

Chức năng:
- Nhập dữ liệu từ người dùng
- Tính toán tọa độ mục tiêu
- Hiển thị kết quả trên bản đồ
"""

from core import GPSTargetSystem
from visualization.plot_utils import MapVisualizer
import matplotlib.pyplot as plt

def get_user_input():
    """Nhận dữ liệu đầu vào từ người dùng"""
    print("=== Nhập thông tin vị trí quan sát ===")
    obs_lat = float(input("Vĩ độ (độ): "))
    obs_lon = float(input("Kinh độ (độ): "))
    obs_alt = float(input("Độ cao (mét): "))
    
    print("\n=== Nhập thông tin ngắm ===")
    azimuth = float(input("Góc phương vị (độ): "))
    elevation = float(input("Góc ngẩng (độ): "))
    distance = float(input("Khoảng cách (mét): "))
    
    return obs_lat, obs_lon, obs_alt, azimuth, elevation, distance

def main():
    """Hàm chính của chương trình"""
    print("GPS Target System - Demo")
    print("-" * 40)
    
    # Khởi tạo hệ thống
    system = GPSTargetSystem()
    visualizer = MapVisualizer()
    
    try:
        # Nhập dữ liệu
        inputs = get_user_input()
        obs_lat, obs_lon, obs_alt, azimuth, elevation, distance = inputs
        
        # Validate dữ liệu
        system.validate_input_data(*inputs)
        
        # Tính toán tọa độ mục tiêu
        target_pos = system.calculate_target_position(*inputs)
        
        # In kết quả
        print("\n=== Kết quả tính toán ===")
        print(f"Tọa độ mục tiêu:")
        print(f"Vĩ độ:  {target_pos[0]:.6f}°")
        print(f"Kinh độ: {target_pos[1]:.6f}°")
        print(f"Độ cao:  {target_pos[2]:.1f}m")
        
        # Hiển thị trên bản đồ
        observer_pos = (obs_lat, obs_lon, obs_alt)
        visualizer.plot_target_scenario(observer_pos, target_pos)
        
        # Hiển thị profile độ cao
        visualizer.plot_elevation_profile(observer_pos, target_pos)
        
        plt.show()
        
    except ValueError as e:
        print(f"\nLỗi: {e}")
    except Exception as e:
        print(f"\nLỗi không xác định: {e}")
        
if __name__ == "__main__":
    main()