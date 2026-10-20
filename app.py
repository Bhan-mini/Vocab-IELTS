import json
import streamlit as st

st.set_page_config(
    page_title="IELTS Vocabulary Shooter Pro", page_icon="🦋", layout="wide"
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng IELTS Chuẩn Cambridge & Reading")
st.write(
    "Kho từ vựng học thuật phong phú trích từ các bài IELTS Reading, Cambridge và"
    " SGK giúp học sinh ôn tập tối ưu!"
)

# --- BẢNG ĐIỀU KHIỂN TRÊN GIAO DIỆN ---
col1, col2, col3 = st.columns(3)

with col1:
  selected_level = st.selectbox(
      "🎯 Chọn Trình độ (CEFR):", ["A1", "A2", "B1", "B2", "C1", "C2"]
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
    f"👉 Đang ôn luyện: Trình độ **{selected_level}** | Chủ đề:"
    f" **{selected_topic}**"
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
            {"word": "walk", "display": "wal_াবহ", "missing": "l", "mean": "Đi bộ"},
        ],
    },
    "A2": {
        "Environment & Nature": [
            {"word": "energy", "display": "en_rgy", "missing": "e", "mean": "Năng lượng"},
            {"word": "river", "display": "ri_er", "missing": "v", "mean": "Dòng sông"},
            {"word": "forest", "display": "for_st", "missing": "e", "mean": "Rừng cây"},
            {"word": "weather", "display": "weath_r", "missing": "e", "mean": "Thời tiết"},
            {"word": "valley", "display": "vall_y", "missing": "e", "mean": "Thung lũng"},
            {"word": "nature", "display": "natur_e", "missing": "e", "mean": "Tự nhiên"},
            {"word": "global", "display": "glob_l", "missing": "a", "mean": "Toàn cầu"},
        ],
        "Technology & AI": [
            {"word": "device", "display": "devic_", "missing": "e", "mean": "Thiết bị"},
            {"word": "camera", "display": "cam_ra", "missing": "e", "mean": "Máy ảnh"},
            {"word": "digital", "display": "digit_l", "missing": "a", "mean": "Kỹ thuật số"},
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
            {"word": "routine", "display": "routin_e", "missing": "e", "mean": "Thói quen hằng ngày"},
        ],
    },
    "B1": {
        "Environment & Nature": [
            {"word": "recycle", "display": "recycl_e", "missing": "e", "mean": "Tái chế"},
            {"word": "climate", "display": "clim_te", "missing": "a", "mean": "Khí hậu"},
            {"word": "natural", "display": "natur_l", "missing": "a", "mean": "Tự nhiên"},
            {"word": "wildlife", "display": "wildl_fe", "missing": "i", "mean": "Động vật hoang dã"},
            {"word": "protect", "display": "prot_ct", "missing": "e", "mean": "Bảo vệ"},
            {"word": "habitat", "display": "habit_t", "missing": "a", "mean": "Môi trường sống"},
            {"word": "disaster", "display": "disast_r", "missing": "e", "mean": "Thảm họa"},
        ],
        "Technology & AI": [
            {"word": "software", "display": "softwa_e", "missing": "r", "mean": "Phần mềm"},
            {"word": "virtual", "display": "virtu_l", "missing": "a", "mean": "Thực tế ảo"},
            {"word": "update", "display": "upda_e", "missing": "t", "mean": "Cập nhật"},
            {"word": "gadget", "display": "gadg_t", "missing": "e", "mean": "Thiết bị điện tử nhỏ"},
            {"word": "innovation", "display": "innovat_on", "missing": "i", "mean": "Sự đổi mới"},
        ],
        "Education & Career": [
            {"word": "employ", "display": "empl_y", "missing": "o", "mean": "Tuyển dụng"},
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
            {"word": "pollution", "display": "pollut_on", "missing": "i", "mean": "Sự ô nhiễm (IELTS Reading)"},
            {"word": "ecosystem", "display": "ecosyst_m", "missing": "e", "mean": "Hệ sinh thái"},
            {"word": "atmosphere", "display": "atmosph_re", "missing": "e", "mean": "Bầu khí quyển"},
            {"word": "conservation", "display": "conservat_on", "missing": "i", "mean": "Sự bảo tồn thiên nhiên"},
            {"word": "renewable", "display": "renewab_e", "missing": "l", "mean": "Có thể tái tạo (năng lượng)"},
            {"word": "emission", "display": "emissi_n", "missing": "o", "mean": "Khí thải công nghiệp"},
        ],
        "Technology & AI": [
            {"word": "algorithm", "display": "algorith_m", "missing": "m", "mean": "Thuật toán máy tính"},
            {"word": "automation", "display": "automat_on", "missing": "i", "mean": "Sự tự động hóa"},
            {"word": "database", "display": "databa_e", "missing": "s", "mean": "Cơ sở dữ liệu"},
            {"word": "interface", "display": "interfac_e", "missing": "e", "mean": "Giao diện tương tác"},
            {"word": "artificial", "display": "artificia_l", "missing": "l", "mean": "Nhân tạo (AI)"},
        ],
        "Education & Career": [
            {"word": "academic", "display": "academi_c", "missing": "c", "mean": "Mang tính học thuật"},
            {"word": "curriculum", "display": "curricul_m", "missing": "u", "mean": "Chương trình giảng dạy"},
            {"word": "scholarship", "display": "scholarsh_p", "missing": "i", "mean": "Học bổng du học"},
            {"word": "profession", "display": "professi_n", "missing": "o", "mean": "Ngành nghề chuyên môn"},
            {"word": "qualification", "display": "qualificat_on", "missing": "i", "mean": "Trình độ chuyên môn"},
        ],
        "Health & Lifestyle": [
            {"word": "nutrition", "display": "nutriti_n", "missing": "o", "mean": "Dinh dưỡng học"},
            {"word": "metabolism", "display": "metaboli_m", "missing": "s", "mean": "Sự trao đổi chất"},
            {"word": "wellbeing", "display": "wellbei_g", "missing": "n", "mean": "Sự khỏe mạnh toàn diện"},
            {"word": "epidemic", "display": "epidemi_c", "missing": "c", "mean": "Dịch bệnh lan rộng"},
            {"word": "therapy", "display": "thera_y", "missing": "p", "mean": "Liệu pháp y tế"},
        ],
    },
    "C1": {
        "Environment & Nature": [
            {"word": "biodiversity", "display": "biodiversit_y", "missing": "y", "mean": "Đa dạng sinh học (Cambridge)"},
            {"word": "catastrophic", "display": "catastroph_c", "missing": "i", "mean": "Thảm khốc, thảm họa lớn"},
            {"word": "deforestation", "display": "deforestat_on", "missing": "i", "mean": "Nạn phá rừng quy mô lớn"},
            {"word": "extinction", "display": "extincti_n", "missing": "o", "mean": "Sự tuyệt chủng loài"},
            {"word": "sanctuary", "display": "sanctuar_y", "missing": "y", "mean": "Khu bảo tồn hoang dã"},
        ],
        "Technology & AI": [
            {"word": "cybersecurity", "display": "cybersecurit_y", "missing": "y", "mean": "An ninh mạng bảo mật"},
            {"word": "cryptography", "display": "cryptograph_y", "missing": "y", "mean": "Thuật toán mã hóa"},
            {"word": "implementation", "display": "implementati_n", "missing": "o", "mean": "Sự thi hành, triển khai"},
            {"word": "quantum", "display": "quant_m", "missing": "u", "mean": "Công nghệ lượng tử"},
            {"word": "biometrics", "display": "biometri_s", "missing": "c", "mean": "Công nghệ sinh trắc học"},
        ],
        "Education & Career": [
            {"word": "dissertation", "display": "dissertat_on", "missing": "i", "mean": "Luận văn tiến sĩ/thạc sĩ"},
            {"word": "pedagogy", "display": "pedagog_y", "missing": "y", "mean": "Khoa học giáo dục/Sư phạm"},
            {"word": "entrepreneur", "display": "entreprene_r", "missing": "u", "mean": "Doanh nhân khởi nghiệp"},
            {"word": "bureaucracy", "display": "bureaucrac_y", "missing": "y", "mean": "Nạn quan liêu hành chính"},
            {"word": "internship", "display": "internsh_p", "missing": "i", "mean": "Chương trình thực tập"},
        ],
        "Health & Lifestyle": [
            {"word": "cardiovascular", "display": "cardiovascul_r", "missing": "a", "mean": "Thuộc hệ tim mạch"},
            {"word": "longevity", "display": "longevit_y", "missing": "y", "mean": "Sự sống lâu, tuổi thọ"},
            {"word": "psychological", "display": "psychologic_l", "missing": "a", "mean": "Thuộc về tâm lý học"},
            {"word": "pharmaceutical", "display": "pharmaceutic_l", "missing": "a", "mean": "Công nghiệp dược phẩm"},
            {"word": "sedentary", "display": "sedentar_y", "missing": "y", "mean": "Lối sống ít vận động"},
        ],
    },
    "C2": {
        "Environment & Nature": [
            {"word": "sustainability", "display": "sustainabilit_y", "missing": "y", "mean": "Tính phát triển bền vững"},
            {"word": "anthropogenic", "display": "anthropogeni_c", "missing": "c", "mean": "Tác động do con người"},
            {"word": "biogeochemical", "display": "biogeochemic_l", "missing": "a", "mean": "Chu trình sinh địa hóa"},
            {"word": "desertification", "display": "desertificat_on", "missing": "i", "mean": "Quá trình hoang mạc hóa"},
        ],
        "Technology & AI": [
            {"word": "supercomputing", "display": "supercomputin_g", "missing": "g", "mean": "Công nghệ siêu máy tính"},
            {"word": "epistemology", "display": "epistemolog_y", "missing": "y", "mean": "Triết học nhận thức luận"},
            {"word": "interoperability", "display": "interoperabilit_y", "missing": "y", "mean": "Tính tương thích liên hệ thống"},
        ],
        "Education & Career": [
            {"word": "institutionalization", "display": "institutionalizat_on", "missing": "i", "mean": "Sự thể chế hóa tổ chức"},
            {"word": "interdisciplinary", "display": "interdisciplinar_y", "missing": "y", "mean": "Nghiên cứu liên ngành"},
        ],
        "Health & Lifestyle": [
            {"word": "neuroplasticity", "display": "neuroplasticit_y", "missing": "y", "mean": "Tính thích ứng thần kinh"},
            {"word": "psychoneuroimmunology", "display": "psychoneuroimmunolog_y", "missing": "y", "mean": "Tâm lý thần kinh miễn dịch"},
            {"word": "homeostasis", "display": "homeostas_s", "missing": "i", "mean": "Sự cân bằng nội môi cơ thể"},
        ],
    },
}

level_dict = vocab_database.get(selected_level, vocab_database["B2"])
filtered_words = level_dict.get(
    selected_topic, list(level_dict.values())[0]
)

vocab_json = json.dumps(filtered_words)
slow_speed = 0.4 if selected_level in ["C1", "C2"] else 0.35

if keyboard_layout == "Laptop / PC (QWERTY)":
  kb_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
else:
  kb_rows = ["123", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

kb_json = json.dumps(kb_rows)

# --- MÃ NGUỒN GAME HTML/JS (ĐÃ KHẮC PHỤC LẶP TỪ) ---
game_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            margin: 0;
            background: #1e1e2f;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
        }}
        #game-container {{
            position: relative;
            width: 100%;
            max-width: 750px;
            margin: 0 auto;
        }}
        canvas {{
            background: linear-gradient(180deg, #2b1055, #7597de);
            display: block;
            width: 100%;
            height: auto;
            border-radius: 12px;
            border: 3px solid #ff69b4;
            box-shadow: 0 0 25px rgba(255, 105, 180, 0.4);
        }}
        .info-bar {{
            display: flex;
            justify-content: space-between;
            background: #282a36;
            padding: 10px 20px;
            border-radius: 8px;
            margin-bottom: 8px;
            font-weight: bold;
            font-size: 15px;
            color: #f1fa8c;
        }}
        .virtual-keyboard {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            margin-top: 12px;
            padding: 0 5px;
        }}
        .kb-row {{
            display: flex;
            gap: 6px;
            justify-content: center;
        }}
        .key-btn {{
            background: #44475a;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 12px 15px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px #282a36;
            min-width: 36px;
        }}
        .key-btn:active {{
            background: #ff69b4;
            transform: translateY(2px);
            box-shadow: 0 2px #282a36;
        }}
    </style>
</head>
<body>

    <div id="game-container">
        <div class="info-bar">
            <span id="unit-info">📌 {selected_level} - {selected_topic}</span>
            <span id="score-info">🏆 Điểm: 0</span>
        </div>
        <canvas id="gameCanvas" width="750" height="500"></canvas>
        <div class="virtual-keyboard" id="keyboard"></div>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const vocabList = {vocab_json};
        const fallSpeed = {slow_speed};
        const kbRows = {kb_json};

        let score = 0;
        let targets = [];
        let bullets = [];
        let particles = [];
        let isGameOver = false;
        let spawnTimer = 0;

        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        function playSound(type) {{
            if (!audioCtx) return;
            let osc = audioCtx.createOscillator();
            let gainNode = audioCtx.createGain();
            osc.connect(gainNode);
            gainNode.connect(audioCtx.destination);

            if (type === "shoot") {{
                osc.type = "sine";
                osc.frequency.setValueAtTime(600, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(300, audioCtx.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.1);
            }} else if (type === "hit") {{
                osc.type = "triangle";
                osc.frequency.setValueAtTime(400, audioCtx.currentTime);
                osc.frequency.setValueAtTime(800, audioCtx.currentTime + 0.08);
                gainNode.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.2);
            }} else if (type === "gameover") {{
                osc.type = "sawtooth";
                osc.frequency.setValueAtTime(200, audioCtx.currentTime);
                osc.frequency.linearRampToValueAtTime(80, audioCtx.currentTime + 0.4);
                gainNode.gain.setValueAtTime(0.2, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.4);
            }}
        }}

        const player = {{
            x: canvas.width / 2 - 25,
            y: canvas.height - 50,
            width: 50,
            height: 50
        }};

        // Thuật toán chọn từ thông minh: Tránh lặp lại các từ đang có sẵn trên màn hình
        function spawnTarget() {{
            if (vocabList.length === 0) return;

            // Lọc ra các từ chưa xuất hiện trên màn hình
            let activeWords = targets.map(t => t.word);
            let availableWords = vocabList.filter(v => !activeWords.includes(v.word));

            // Nếu tất cả từ đã xuất hiện hết, reset lại danh sách cho phép chọn ngẫu nhiên lại
            if (availableWords.length === 0) {{
                availableWords = vocabList;
            }}

            const randomIndex = Math.floor(Math.random() * availableWords.length);
            const item = availableWords[randomIndex];
            
            let randomX = Math.random() * (canvas.width - 200) + 20;
            
            targets.push({{
                ...item,
                x: randomX,
                y: -60,
                speed: fallSpeed
            }});
        }}

        function handleInput(typedKey) {{
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            if (isGameOver) return;

            typedKey = typedKey.toLowerCase();

            for (let i = 0; i < targets.length; i++) {{
                let t = targets[i];
                if (typedKey === t.missing) {{
                    playSound("shoot");
                    bullets.push({{
                        x: player.x + player.width / 2,
                        y: player.y,
                        targetId: i,
                        targetX: t.x + 80,
                        targetY: t.y + 20,
                        speed: 10
                    }});
                    break;
                }}
            }}
        }}

        document.addEventListener("keydown", function(e) {{
            handleInput(e.key);
        }});

        const keyboardDiv = document.getElementById("keyboard");
        keyboardDiv.innerHTML = "";
        kbRows.forEach(rowStr => {{
            const rowDiv = document.createElement("div");
            rowDiv.className = "kb-row";
            for (let char of rowStr) {{
                const btn = document.createElement("button");
                btn.innerText = char.toUpperCase();
                btn.className = "key-btn";
                btn.onclick = () => handleInput(char);
                rowDiv.appendChild(btn);
            }}
            keyboardDiv.appendChild(rowDiv);
        }});

        function update() {{
            if (isGameOver) return;

            spawnTimer++;
            // Khoảng thời gian giãn cách vừa đủ để từ vựng xuất hiện thong thả, không bị dồn cục
            if (spawnTimer > 120) {{
                spawnTarget();
                spawnTimer = 0;
            }}

            for (let i = targets.length - 1; i >= 0; i--) {{
                targets[i].y += targets[i].speed;

                if (targets[i].y > canvas.height - 70) {{
                    isGameOver = true;
                    playSound("gameover");
                }}
            }}

            for (let i = bullets.length - 1; i >= 0; i--) {{
                let b = bullets[i];
                b.y -= b.speed;

                let targetObj = targets[b.targetId];
                if (targetObj && b.y <= targetObj.y + 30) {{
                    score += 10;
                    document.getElementById("score-info").innerText = "🏆 Điểm: " + score;
                    playSound("hit");
                    createExplosion(targetObj.x + 80, targetObj.y + 20);
                    
                    targets.splice(b.targetId, 1);
                    bullets.splice(i, 1);
                    break;
                }}
            }}

            for (let i = particles.length - 1; i >= 0; i--) {{
                let p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.alpha -= 0.03;
                if (p.alpha <= 0) particles.splice(i, 1);
            }}
        }}

        function createExplosion(x, y) {{
            for (let i = 0; i < 15; i++) {{
                particles.push({{
                    x: x,
                    y: y,
                    vx: (Math.random() - 0.5) * 6,
                    vy: (Math.random() - 0.5) * 6,
                    alpha: 1,
                    color: "#ff69b4"
                }});
            }}
        }}

        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Vẽ nhân vật bướm 🦋
            ctx.fillStyle = "#ff69b4";
            ctx.beginPath();
            ctx.arc(player.x + 25, player.y + 25, 20, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = "#000";
            ctx.font = "26px Arial";
            ctx.fillText("🦋", player.x + 8, player.y + 35);

            // Vẽ danh sách từ vựng đa dạng không lặp nhau
            targets.forEach(t => {{
                ctx.fillStyle = "#ff9800";
                ctx.shadowColor = "#ff5722";
                ctx.shadowBlur = 10;
                ctx.fillRect(t.x, t.y, 170, 45);
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 17px Arial";
                ctx.fillText(t.display, t.x + 10, t.y + 24);

                ctx.fillStyle = "#e0e0e0";
                ctx.font = "italic 11px Arial";
                ctx.fillText("(" + t.mean + ")", t.x + 10, t.y + 40);
            }});

            // Vẽ đạn
            ctx.fillStyle = "#00ffff";
            bullets.forEach(b => {{
                ctx.beginPath();
                ctx.arc(b.x, b.y, 6, 0, Math.PI * 2);
                ctx.fill();
            }});

            // Vẽ hiệu ứng hạt nổ
            particles.forEach(p => {{
                ctx.save();
                ctx.globalAlpha = p.alpha;
                ctx.fillStyle = p.color;
                ctx.fillRect(p.x, p.y, 4, 4);
                ctx.restore();
            }});

            // Màn hình Game Over
            if (isGameOver) {{
                ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#ff4757";
                ctx.font = "bold 32px Arial";
                ctx.fillText("GAME OVER", canvas.width / 2 - 90, 200);

                ctx.fillStyle = "#ffffff";
                ctx.font = "18px Arial";
                ctx.fillText("Từ vựng đã chạm đáy màn hình!", canvas.width / 2 - 145, 240);
                ctx.fillText("Tải lại trang để thử lại vòng chơi mới nhé!", canvas.width / 2 - 160, 280);
            }}
        }}

        function loop() {{
            update();
            draw();
            requestAnimationFrame(loop);
        }}

        spawnTarget();
        loop();
    </script>
</body>
</html>
"""

st.components.v1.html(game_code, height=620)
