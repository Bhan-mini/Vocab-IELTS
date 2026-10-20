import json
import streamlit as st

st.set_page_config(
    page_title="IELTS Vocabulary Shooter Pro", page_icon="🦋", layout="wide"
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng IELTS - Chinh Phục Cấp Độ")
st.write(
    "Hệ thống từ vựng phong phú chuẩn IELTS Reading, tự động thăng cấp khi đạt"
    " mỗi 100 điểm!"
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
    f"👉 Bắt đầu ôn luyện ở Trình độ: **{selected_level}** | Chủ đề:"
    f" **{selected_topic}** (Tự động thăng cấp sau mỗi 100 điểm!)"
)

# KHO TỪ VỰNG KHỔNG LỒ CHUẨN CAMBRIDGE & IELTS READING (A1 - C2)
vocab_database = {
    "A1": {
        "Environment & Nature": [
            {"word": "water", "display": "wat_r", "missing": "e", "mean": "Nước"},
            {"word": "plant", "display": "pl_nt", "missing": "a", "mean": "Thực vật"},
            {"word": "tree", "display": "tr_e", "missing": "e", "mean": "Cây cối"},
            {"word": "sun", "display": "s_n", "missing": "u", "mean": "Mặt trời"},
            {
                "word": "animal",
                "display": "anim_l",
                "missing": "a",
                "mean": "Động vật",
            },
            {
                "word": "earth",
                "display": "ear_h",
                "missing": "t",
                "mean": "Trái Đất",
            },
            {"word": "river", "display": "riv_r", "missing": "e", "mean": "Dòng sông"},
            {"word": "flower", "display": "flow_r", "missing": "e", "mean": "Hoa"},
            {"word": "wind", "display": "wi_d", "missing": "n", "mean": "Gió"},
            {"word": "rain", "display": "ra_n", "missing": "i", "mean": "Mưa"},
        ],
        "Technology & AI": [
            {
                "word": "phone",
                "display": "ph_ne",
                "missing": "o",
                "mean": "Điện thoại",
            },
            {
                "word": "computer",
                "display": "comput_r",
                "missing": "e",
                "mean": "Máy tính",
            },
            {"word": "game", "display": "g_me", "missing": "a", "mean": "Trò chơi"},
            {
                "word": "screen",
                "display": "scr_en",
                "missing": "e",
                "mean": "Màn hình",
            },
            {
                "word": "email",
                "display": "em_il",
                "missing": "a",
                "mean": "Thư điện tử",
            },
            {"word": "wifi", "display": "wi_fi", "missing": "f", "mean": "Mạng wifi"},
            {"word": "video", "display": "vid_o", "missing": "e", "mean": "Video"},
            {
                "word": "online",
                "display": "onl_ne",
                "missing": "i",
                "mean": "Trực tuyến",
            },
        ],
        "Education & Career": [
            {"word": "study", "display": "st_dy", "missing": "u", "mean": "Học tập"},
            {"word": "book", "display": "bo_k", "missing": "o", "mean": "Sách"},
            {"word": "class", "display": "cl_ss", "missing": "a", "mean": "Lớp học"},
            {"word": "job", "display": "j_b", "missing": "o", "mean": "Công việc"},
            {
                "word": "teacher",
                "display": "teach_r",
                "missing": "e",
                "mean": "Giáo viên",
            },
            {
                "word": "school",
                "display": "scho_l",
                "missing": "o",
                "mean": "Trường học",
            },
            {
                "word": "student",
                "display": "stud_nt",
                "missing": "e",
                "mean": "Học sinh",
            },
            {"word": "read", "display": "re_d", "missing": "a", "mean": "Đọc sách"},
            {"word": "write", "display": "writ_e", "missing": "e", "mean": "Viết"},
        ],
        "Health & Lifestyle": [
            {
                "word": "health",
                "display": "heal_h",
                "missing": "t",
                "mean": "Sức khỏe",
            },
            {"word": "food", "display": "fo_d", "missing": "o", "mean": "Thức ăn"},
            {
                "word": "sleep",
                "display": "sle_p",
                "missing": "e",
                "mean": "Ngủ nghỉ",
            },
            {"word": "sport", "display": "spo_t", "missing": "r", "mean": "Thể thao"},
            {"word": "happy", "display": "hap_y", "missing": "p", "mean": "Vui vẻ"},
            {
                "word": "life",
                "display": "li_e",
                "missing": "f",
                "mean": "Cuộc sống",
            },
            {"word": "fruit", "display": "fru_t", "missing": "i", "mean": "Trái cây"},
            {
                "word": "water",
                "display": "wat_r",
                "missing": "e",
                "mean": "Nước uống",
            },
            {"word": "walk", "display": "wal_k", "missing": "l", "mean": "Đi bộ"},
        ],
    },
    "A2": {
        "Environment & Nature": [
            {
                "word": "energy",
                "display": "en_rgy",
                "missing": "e",
                "mean": "Năng lượng",
            },
            {"word": "river", "display": "ri_er", "missing": "v", "mean": "Dòng sông"},
            {"word": "forest", "display": "for_st", "missing": "e", "mean": "Rừng cây"},
            {
                "word": "weather",
                "display": "weath_r",
                "missing": "e",
                "mean": "Thời tiết",
            },
            {"word": "valley", "display": "vall_y", "missing": "e", "mean": "Thung lũng"},
            {"word": "nature", "display": "natur_e", "missing": "e", "mean": "Tự nhiên"},
            {"word": "global", "display": "glob_l", "missing": "a", "mean": "Toàn cầu"},
        ],
        "Technology & AI": [
            {"word": "device", "display": "devic_", "missing": "e", "mean": "Thiết bị"},
            {"word": "camera", "display": "cam_ra", "missing": "e", "mean": "Máy ảnh"},
            {
                "word": "digital",
                "display": "digit_l",
                "missing": "a",
                "mean": "Kỹ thuật số",
            },
            {"word": "website", "display": "websi_e", "missing": "t", "mean": "Trang web"},
            {"word": "network", "display": "netwo_k", "missing": "r", "mean": "Mạng lưới"},
        ],
        "Education & Career": [
            {"word": "career", "display": "car_er", "missing": "e", "mean": "Sự nghiệp"},
            {"word": "lesson", "display": "less_n", "missing": "o", "mean": "Bài học"},
            {"word": "office", "display": "off_ce", "missing": "i", "mean": "Văn phòng"},
            {"word": "salary", "display": "sala_y", "missing": "r", "mean": "Tiền lương"},
            {"word": "library", "display": "librar_y", "missing": "y", "mean": "Thư viện"},
        ],
        "Health & Lifestyle": [
            {"word": "fitness", "display": "fitn_ss", "missing": "e", "mean": "Thể lực"},
            {"word": "doctor", "display": "doct_r", "missing": "o", "mean": "Bác sĩ"},
            {"word": "travel", "display": "trav_l", "missing": "e", "mean": "Du lịch"},
            {"word": "balance", "display": "balan_e", "missing": "c", "mean": "Sự cân bằng"},
            {
                "word": "routine",
                "display": "routin_e",
                "missing": "e",
                "mean": "Thói quen hằng ngày",
            },
        ],
    },
    "B1": {
        "Environment & Nature": [
            {"word": "recycle", "display": "recycl_e", "missing": "e", "mean": "Tái chế"},
            {"word": "climate", "display": "clim_te", "missing": "a", "mean": "Khí hậu"},
            {"word": "natural", "display": "natur_l", "missing": "a", "mean": "Tự nhiên"},
            {
                "word": "wildlife",
                "display": "wildl_fe",
                "missing": "i",
                "mean": "Động vật hoang dã",
            },
            {"word": "protect", "display": "prot_ct", "missing": "e", "mean": "Bảo vệ"},
            {
                "word": "habitat",
                "display": "habit_t",
                "missing": "a",
                "mean": "Môi trường sống",
            },
            {"word": "disaster", "display": "disast_r", "missing": "e", "mean": "Thảm họa"},
        ],
        "Technology & AI": [
            {
                "word": "software",
                "display": "softwa_e",
                "missing": "r",
                "mean": "Phần mềm",
            },
            {"word": "virtual", "display": "virtu_l", "missing": "a", "mean": "Thực tế ảo"},
            {"word": "update", "display": "upda_e", "missing": "t", "mean": "Cập nhật"},
            {
                "word": "gadget",
                "display": "gadg_t",
                "missing": "e",
                "mean": "Thiết bị điện tử nhỏ",
            },
            {
                "word": "innovation",
                "display": "innovat_on",
                "missing": "i",
                "mean": "Sự đổi mới",
            },
        ],
        "Education & Career": [
            {
                "word": "employ",
                "display": "empl_y",
                "missing": "o",
                "mean": "Tuyển dụng",
            },
            {"word": "degree", "display": "degr_e", "missing": "e", "mean": "Bằng đại học"},
            {"word": "skill", "display": "sk_ll", "missing": "i", "mean": "Kỹ năng"},
            {"word": "training", "display": "train_ng", "missing": "i", "mean": "Đào tạo"},
            {"word": "income", "display": "inc_me", "missing": "o", "mean": "Thu nhập"},
        ],
        "Health & Lifestyle": [
            {"word": "disease", "display": "disea_e", "missing": "s", "mean": "Bệnh tật"},
            {"word": "habit", "display": "hab_t", "missing": "i", "mean": "Thói quen"},
            {"word": "relax", "display": "rel_x", "missing": "a", "mean": "Thư giãn"},
            {"word": "active", "display": "acti_e", "missing": "v", "mean": "Năng động"},
            {"word": "mental", "display": "ment_l", "missing": "a", "mean": "Tinh thần"},
        ],
    },
    "B2": {
        "Environment & Nature": [
            {
                "word": "pollution",
                "display": "pollut_on",
                "missing": "i",
                "mean": "Sự ô nhiễm (IELTS Reading)",
            },
            {"word": "ecosystem", "display": "ecosyst_m", "missing": "e", "mean": "Hệ sinh thái"},
            {
                "word": "atmosphere",
                "display": "atmosph_re",
                "missing": "e",
                "mean": "Bầu khí quyển",
            },
            {
                "word": "conservation",
                "display": "conservat_on",
                "missing": "i",
                "mean": "Sự bảo tồn thiên nhiên",
            },
            {
                "word": "renewable",
                "display": "renewab_e",
                "missing": "l",
                "mean": "Có thể tái tạo (năng lượng)",
            },
            {
                "word": "emission",
                "display": "emissi_n",
                "missing": "o",
                "mean": "Khí thải công nghiệp",
            },
        ],
        "Technology & AI": [
            {
                "word": "algorithm",
                "display": "algorith_m",
                "missing": "m",
                "mean": "Thuật toán máy tính",
            },
            {
                "word": "automation",
                "display": "automat_on",
                "missing": "i",
                "mean": "Sự tự động hóa",
            },
            {"word": "database", "display": "databa_e", "missing": "s", "mean": "Cơ sở dữ liệu"},
            {
                "word": "interface",
                "display": "interfac_e",
                "missing": "e",
                "mean": "Giao diện tương tác",
            },
            {
                "word": "artificial",
                "display": "artificia_l",
                "missing": "l",
                "mean": "Nhân tạo (AI)",
            },
        ],
        "Education & Career": [
            {
                "word": "academic",
                "display": "academi_c",
                "missing": "c",
                "mean": "Mang tính học thuật",
            },
            {
                "word": "curriculum",
                "display": "curricul_m",
                "missing": "u",
                "mean": "Chương trình giảng dạy",
            },
            {
                "word": "scholarship",
                "display": "scholarsh_p",
                "missing": "i",
                "mean": "Học bổng du học",
            },
            {
                "word": "profession",
                "display": "professi_n",
                "missing": "o",
                "mean": "Ngành nghề chuyên môn",
            },
            {
                "word": "qualification",
                "display": "qualificat_on",
                "missing": "i",
                "mean": "Trình độ chuyên môn",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "nutrition",
                "display": "nutriti_n",
                "missing": "o",
                "mean": "Dinh dưỡng học",
            },
            {
                "word": "metabolism",
                "display": "metaboli_m",
                "missing": "s",
                "mean": "Sự trao đổi chất",
            },
            {
                "word": "wellbeing",
                "display": "wellbei_g",
                "missing": "n",
                "mean": "Sự khỏe mạnh toàn diện",
            },
            {
                "word": "epidemic",
                "display": "epidemi_c",
                "missing": "c",
                "mean": "Dịch bệnh lan rộng",
            },
            {"word": "therapy", "display": "thera_y", "missing": "p", "mean": "Liệu pháp y tế"},
        ],

