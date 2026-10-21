import json
import random
import streamlit as st

st.set_page_config(
    page_title="IELTS Vocabulary Shooter Pro", page_icon="🦋", layout="wide"
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng IELTS - Chinh Phục Cấp Độ")
st.write(
    "Đoán chữ cái bị ẩn [ _ ], gõ đúng phím để chú bướm bắn hạ từ vựng và thăng"
    " cấp!"
)

# --- BẢNG ĐIỀU KHIỂN TRÊN GIAO DIỆN ---
col1, col2, col3 = st.columns(3)

with col1:
  selected_level = st.selectbox(
      "🎯 Chọn Trình độ bắt đầu (CEFR):", ["A1", "A2", "B1", "B2", "C1", "C2"]
  )

with col2:
  selected_topic = st.selectbox(
      "📚 Chọn Chủ đề từ vựng:",
      [
          "Environment & Nature",
          "Technology & AI",
          "Education & Career",
          "Health & Lifestyle",
      ],
  )

with col3:
  keyboard_layout = st.selectbox(
      "⌨️ Kiểu Bàn phím ảo:",
      ["Laptop / PC (QWERTY)", "Điện thoại (Phone Layout)"],
  )

st.info(
    f"👉 Đang ôn luyện ở Trình độ: **{selected_level}** | Chủ đề:"
    f" **{selected_topic}** (Tự động thăng cấp sau mỗi 100 điểm!)"
)

# KHO TỪ VỰNG CHUẨN IELTS & CAMBRIDGE
raw_vocab_database = {
    "A1": {
        "Environment & Nature": [
            {"word": "water", "mean": "Nước"},
            {"word": "plant", "mean": "Thực vật"},
            {"word": "tree", "mean": "Cây cối"},
            {"word": "sun", "mean": "Mặt trời"},
            {"word": "animal", "mean": "Động vật"},
            {"word": "earth", "mean": "Trái Đất"},
            {"word": "river", "mean": "Dòng sông"},
            {"word": "flower", "mean": "Bông hoa"},
        ],
        "Technology & AI": [
            {"word": "phone", "mean": "Điện thoại"},
            {"word": "computer", "mean": "Máy tính"},
            {"word": "game", "mean": "Trò chơi"},
            {"word": "screen", "mean": "Màn hình"},
            {"word": "email", "mean": "Thư điện tử"},
            {"word": "video", "mean": "Video"},
        ],
        "Education & Career": [
            {"word": "study", "mean": "Học tập"},
            {"word": "book", "mean": "Sách"},
            {"word": "class", "mean": "Lớp học"},
            {"word": "job", "mean": "Công việc"},
            {"word": "teacher", "mean": "Giáo viên"},
            {"word": "school", "mean": "Trường học"},
        ],
        "Health & Lifestyle": [
            {"word": "health", "mean": "Sức khỏe"},
            {"word": "food", "mean": "Thức ăn"},
            {"word": "sleep", "mean": "Ngủ nghỉ"},
            {"word": "sport", "mean": "Thể thao"},
            {"word": "fruit", "mean": "Trái cây"},
        ],
    },
    "A2": {
        "Environment & Nature": [
            {"word": "energy", "mean": "Năng lượng"},
            {"word": "forest", "mean": "Rừng cây"},
            {"word": "weather", "mean": "Thời tiết"},
            {"word": "nature", "mean": "Tự nhiên"},
        ],
        "Technology & AI": [
            {"word": "device", "mean": "Thiết bị"},
            {"word": "camera", "mean": "Máy ảnh"},
            {"word": "digital", "mean": "Kỹ thuật số"},
            {"word": "website", "mean": "Trang web"},
        ],
        "Education & Career": [
            {"word": "career", "mean": "Sự nghiệp"},
            {"word": "lesson", "mean": "Bài học"},
            {"word": "office", "mean": "Văn phòng"},
            {"word": "salary", "mean": "Tiền lương"},
        ],
        "Health & Lifestyle": [
            {"word": "fitness", "mean": "Thể lực"},
            {"word": "doctor", "mean": "Bác sĩ"},
            {"word": "travel", "mean": "Du lịch"},
            {"word": "balance", "mean": "Cân bằng"},
        ],
    },
    "B1": {
        "Environment & Nature": [
            {"word": "recycle", "mean": "Tái chế"},
            {"word": "climate", "mean": "Khí hậu"},
            {"word": "natural", "mean": "Tự nhiên"},
            {"word": "wildlife", "mean": "Động thực vật hoang dã"},
        ],
        "Technology & AI": [
            {"word": "software", "mean": "Phần mềm"},
            {"word": "virtual", "mean": "Thực tế ảo"},
            {"word": "update", "mean": "Cập nhật"},
            {"word": "gadget", "mean": "Thiết bị điện tử nhỏ"},
        ],
        "Education & Career": [
            {"word": "employ", "mean": "Tuyển dụng"},
            {"word": "degree", "mean": "Bằng đại học"},
            {"word": "skill", "mean": "Kỹ năng"},
            {"word": "income", "mean": "Thu nhập"},
        ],
        "Health & Lifestyle": [
            {"word": "disease", "mean": "Bệnh tật"},
            {"word": "habit", "mean": "Thói quen"},
            {"word": "relax", "mean": "Thư giãn"},
            {"word": "active", "mean": "Năng động"},
        ],
    },
    "B2": {
        "Environment & Nature": [
            {"word": "pollution", "mean": "Sự ô nhiễm"},
            {"word": "ecosystem", "mean": "Hệ sinh thái"},
            {"word": "atmosphere", "mean": "Bầu khí quyển"},
            {"word": "conservation", "mean": "Sự bảo tồn"},
            {"word": "renewable", "mean": "Có thể tái tạo"},
        ],
        "Technology & AI": [
            {"word": "algorithm", "mean": "Thuật toán"},
            {"word": "automation", "mean": "Tự động hóa"},
            {"word": "database", "mean": "Cơ sở dữ liệu"},
            {"word": "interface", "mean": "Giao diện"},
        ],
