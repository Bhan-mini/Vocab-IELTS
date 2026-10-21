import json
import streamlit as st

st.set_page_config(
    page_title="IELTS Vocabulary Shooter Pro", page_icon="🦋", layout="wide"
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng IELTS - Chinh Phục Cấp Độ")
st.write(
    "Hệ thống từ vựng chuẩn IELTS Reading, phóng to chữ siêu lớn, không lặp từ"
    " và tự động thăng cấp!"
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

# KHO TỪ VỰNG KHỔNG LỒ VÀ ĐA DẠNG KHÔNG BỊ TRÙNG LẶP
vocab_database = {
    "A1": {
        "Environment & Nature": [
            {
                "word": "water",
                "display": "WATE [ R ]",
                "missing": "r",
                "mean": "Nước",
            },
            {
                "word": "plant",
                "display": "PLAN [ T ]",
                "missing": "t",
                "mean": "Thực vật",
            },
            {
                "word": "tree",
                "display": "TRE [ E ]",
                "missing": "e",
                "mean": "Cây cối",
            },
            {
                "word": "sun",
                "display": "SU [ N ]",
                "missing": "n",
                "mean": "Mặt trời",
            },
            {
                "word": "animal",
                "display": "ANIMA [ L ]",
                "missing": "l",
                "mean": "Động vật",
            },
            {
                "word": "earth",
                "display": "EART [ H ]",
                "missing": "h",
                "mean": "Trái Đất",
            },
            {
                "word": "river",
                "display": "RIVE [ R ]",
                "missing": "r",
                "mean": "Dòng sông",
            },
            {
                "word": "flower",
                "display": "FLOWE [ R ]",
                "missing": "r",
                "mean": "Bông hoa",
            },
        ],
        "Technology & AI": [
            {
                "word": "phone",
                "display": "PHON [ E ]",
                "missing": "e",
                "mean": "Điện thoại",
            },
            {
                "word": "computer",
                "display": "COMPUTE [ R ]",
                "missing": "r",
                "mean": "Máy tính",
            },
            {
                "word": "game",
                "display": "GAM [ E ]",
                "missing": "e",
                "mean": "Trò chơi",
            },
            {
                "word": "screen",
                "display": "SCREE [ N ]",
                "missing": "n",
                "mean": "Màn hình",
            },
            {
                "word": "email",
                "display": "EMAI [ L ]",
                "missing": "l",
                "mean": "Thư điện tử",
            },
            {
                "word": "video",
                "display": "VIDE [ O ]",
                "missing": "o",
                "mean": "Video",
            },
        ],
        "Education & Career": [
            {
                "word": "study",
                "display": "STUD [ Y ]",
                "missing": "y",
                "mean": "Học tập",
            },
            {"word": "book", "display": "BOO [ K ]", "missing": "k", "mean": "Sách"},
            {
                "word": "class",
                "display": "CLAS [ S ]",
                "missing": "s",
                "mean": "Lớp học",
            },
            {"word": "job", "display": "JO [ B ]", "missing": "b", "mean": "Công việc"},
            {
                "word": "teacher",
                "display": "TEACHE [ R ]",
                "missing": "r",
                "mean": "Giáo viên",
            },
            {
                "word": "school",
                "display": "SCHOO [ L ]",
                "missing": "l",
                "mean": "Trường học",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "health",
                "display": "HEALT [ H ]",
                "missing": "h",
                "mean": "Sức khỏe",
            },
            {"word": "food", "display": "FOO [ D ]", "missing": "d", "mean": "Thức ăn"},
            {
                "word": "sleep",
                "display": "SLEE [ P ]",
                "missing": "p",
                "mean": "Ngủ nghỉ",
            },
            {
                "word": "sport",
                "display": "SPOR [ T ]",
                "missing": "t",
                "mean": "Thể thao",
            },
            {
                "word": "fruit",
                "display": "FRUI [ T ]",
                "missing": "t",
                "mean": "Trái cây",
            },
        ],
    },
    "A2": {
        "Environment & Nature": [
            {
                "word": "energy",
                "display": "ENERG [ Y ]",
                "missing": "y",
                "mean": "Năng lượng",
            },
            {
                "word": "forest",
                "display": "FORES [ T ]",
                "missing": "t",
                "mean": "Rừng cây",
            },
            {
                "word": "weather",
                "display": "WEATHE [ R ]",
                "missing": "r",
                "mean": "Thời tiết",
            },
            {
                "word": "nature",
                "display": "NATUR [ E ]",
                "missing": "e",
                "mean": "Tự nhiên",
            },
        ],
        "Technology & AI": [
            {
                "word": "device",
                "display": "DEVIC [ E ]",
                "missing": "e",
                "mean": "Thiết bị",
            },
            {
                "word": "camera",
                "display": "CAMER [ A ]",
                "missing": "a",
                "mean": "Máy ảnh",
            },
            {
                "word": "digital",
                "display": "DIGITA [ L ]",
                "missing": "l",
                "mean": "Kỹ thuật số",
            },
            {
                "word": "website",
                "display": "WEBSIT [ E ]",
                "missing": "e",
                "mean": "Trang web",
            },
        ],
        "Education & Career": [
            {
                "word": "career",
                "display": "CAREE [ R ]",
                "missing": "r",
                "mean": "Sự nghiệp",
            },
            {
                "word": "lesson",
                "display": "LESSO [ N ]",
                "missing": "n",
                "mean": "Bài học",
            },
            {
                "word": "office",
                "display": "OFFIC [ E ]",
                "missing": "e",
                "mean": "Văn phòng",
            },
            {
                "word": "salary",
                "display": "SALAR [ Y ]",
                "missing": "y",
                "mean": "Tiền lương",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "fitness",
                "display": "FITNES [ S ]",
                "missing": "s",
                "mean": "Thể lực",
            },
            {
                "word": "doctor",
                "display": "DOCTO [ R ]",
                "missing": "r",
                "mean": "Bác sĩ",
            },
            {
                "word": "travel",
                "display": "TRAVE [ L ]",
                "missing": "l",
                "mean": "Du lịch",
            },
            {
                "word": "balance",
                "display": "BALANC [ E ]",
                "missing": "e",
                "mean": "Cân bằng",
            },
        ],
    },
    "B1": {
        "Environment & Nature": [
            {
                "word": "recycle",
                "display": "RECYCL [ E ]",
                "missing": "e",
                "mean": "Tái chế",
            },
            {
                "word": "climate",
                "display": "CLIMAT [ E ]",
                "missing": "e",
                "mean": "Khí hậu",
            },
            {
                "word": "natural",
                "display": "NATURA [ L ]",
                "missing": "l",
                "mean": "Tự nhiên",
            },
            {
                "word": "wildlife",
                "display": "WILDLIF [ E ]",
                "missing": "e",
                "mean": "Động thực vật hoang dã",
            },
        ],
        "Technology & AI": [
            {
                "word": "software",
                "display": "SOFTWAR [ E ]",
                "missing": "e",
                "mean": "Phần mềm",
            },
            {
                "word": "virtual",
                "display": "VIRTU_L",
                "missing": "a",
                "mean": "Thực tế ảo",
            },
            {
                "word": "update",
                "display": "UPDAT [ E ]",
                "missing": "e",
                "mean": "Cập nhật",
            },
            {
                "word": "gadget",
                "display": "GADGE [ T ]",
                "missing": "t",
                "mean": "Thiết bị điện tử nhỏ",
            },
        ],
        "Education & Career": [
            {
                "word": "employ",
                "display": "EMPLO [ Y ]",
                "missing": "y",
                "mean": "Tuyển dụng",
            },
            {
                "word": "degree",
                "display": "DEGRJ [ E ]",
                "missing": "e",
                "mean": "Bằng đại học",
            },
            {
                "word": "skill",
                "display": "SKIL [ L ]",
                "missing": "l",
                "mean": "Kỹ năng",
            },
            {
                "word": "income",
                "display": "INCOM [ E ]",
                "missing": "e",
                "mean": "Thu nhập",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "disease",
                "display": "DISEAS [ E ]",
                "missing": "e",
                "mean": "Bệnh tật",
            },
            {
                "word": "habit",
                "display": "HABI [ T ]",
                "missing": "t",
                "mean": "Thói quen",
            },
            {
                "word": "relax",
                "display": "RELA [ X ]",
                "missing": "x",
                "mean": "Thư giãn",
            },
            {
                "word": "active",
                "display": "ACTIV [ E ]",
                "missing": "e",
                "mean": "Năng động",
            },
        ],
    },
    "B2": {
        "Environment & Nature": [
            {
                "word": "pollution",
                "display": "POLLUTIO [ N ]",
                "missing": "n",
                "mean": "Sự ô nhiễm",
            },
            {
                "word": "ecosystem",
                "display": "ECOSYSTE [ M ]",
                "missing": "m",
                "mean": "Hệ sinh thái",
            },
            {
                "word": "atmosphere",
                "display": "ATMOSPHER [ E ]",
                "missing": "e",
                "mean": "Bầu khí quyển",
            },
            {
                "word": "conservation",
                "display": "CONSERVATIO [ N ]",
                "missing": "n",
                "mean": "Sự bảo tồn",
            },
            {
                "word": "renewable",
                "display": "RENEWABL [ E ]",
                "missing": "e",
                "mean": "Có thể tái tạo",
            },
        ],
        "Technology & AI": [
            {
                "word": "algorithm",
                "display": "ALGORITH [ M ]",
                "missing": "m",
                "mean": "Thuật toán",
            },
            {
                "word": "automation",
                "display": "AUTOMATIO [ N ]",
                "missing": "n",
                "mean": "Tự động hóa",
            },
            {
                "word": "database",
                "display": "DATABAS [ E ]",
                "missing": "e",
                "mean": "Cơ sở dữ liệu",
            },
            {
                "word": "interface",
                "display": "INTERFAC [ E ]",
                "missing": "e",
                "mean": "Giao diện",
            },
        ],
        "Education & Career": [
            {
                "word": "academic",
                "display": "ACADEMI [ C ]",
                "missing": "c",
                "mean": "Học thuật",
            },
            {
                "word": "curriculum",
                "display": "CURRICULU [ M ]",
                "missing": "m",
                "mean": "Chương trình học",
            },
            {
                "word": "scholarship",
                "display": "SCHOLARSHI [ P ]",
                "missing": "p",
                "mean": "Học bổng",
            },
            {
                "word": "profession",
                "display": "PROFESSIO [ N ]",
                "missing": "n",
                "mean": "Nghề nghiệp",
            },
            {
                "word": "qualification",
                "display": "QUALIFICATIO [ N ]",
                "missing": "n",
                "mean": "Trình độ chuyên môn",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "nutrition",
                "display": "NUTRITIO [ N ]",
                "missing": "n",
                "mean": "Dinh dưỡng",
            },
            {
                "word": "metabolism",
                "display": "METABOLIS [ M ]",
                "missing": "m",
                "mean": "Trao đổi chất",
            },
            {
                "word": "wellbeing",
                "display": "WELLBEIN [ G ]",
                "missing": "g",
                "mean": "Sức khỏe toàn diện",
            },
            {
                "word": "epidemic",
                "display": "EPIDEMI [ C ]",
                "missing": "c",
                "mean": "Dịch bệnh",
            },
        ],
    },
    "C1": {
        "Environment & Nature": [
            {
                "word": "biodiversity",
                "display": "BIODIVERSIT [ Y ]",
                "missing": "y",
                "mean": "Đa dạng sinh học",
            },
            {
                "word": "catastrophic",
                "display": "CATASTROPHI [ C ]",
                "missing": "c",
                "mean": "Thảm khốc",
            },
            {
                "word": "deforestation",
                "display": "DEFORESTATIO [ N ]",
                "missing": "n",
                "mean": "Nạn phá rừng",
            },
            {
                "word": "extinction",
                "display": "EXTINCTIO [ N ]",
                "missing": "n",
                "mean": "Sự tuyệt chủng",
            },
        ],
        "Technology & AI": [
            {
                "word": "cybersecurity",
                "display": "CYBERSECURIT [ Y ]",
                "missing": "y",
                "mean": "An ninh mạng",
            },
            {
                "word": "cryptography",
                "display": "CRYPTOGRAPh [ Y ]",
                "missing": "y",
                "mean": "Mật mã học",
            },
            {
                "word": "implementation",
                "display": "IMPLEMENTATIO [ N ]",
                "missing": "n",
                "mean": "Sự triển khai",
            },
            {
                "word": "biometrics",
                "display": "BIOMETRIC [ S ]",
                "missing": "s",
                "mean": "Sinh trắc học",
            },
        ],
        "Education & Career": [
            {
                "word": "dissertation",
                "display": "DISSERTATIO [ N ]",
                "missing": "n",
                "mean": "Luận văn",
            },
            {
                "word": "pedagogy",
                "display": "PEDAGOG [ Y ]",
                "missing": "y",
                "mean": "Sư phạm",
            },
            {
                "word": "entrepreneur",
                "display": "ENTREPRENEU [ R ]",
                "missing": "r",
                "mean": "Doanh nhân",
            },
            {
                "word": "bureaucracy",
                "display": "BUREAUCRAC [ Y ]",
                "missing": "y",
                "mean": "Nạn quan liêu",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "cardiovascular",
                "display": "CARDIOVASCULA [ R ]",
                "missing": "r",
                "mean": "Tim mạch",
            },
            {
                "word": "longevity",
                "display": "LONGEVIT [ Y ]",
                "missing": "y",
                "mean": "Tuổi thọ",
            },
            {
                "word": "psychological",
                "display": "PSYCHOLOGICA [ L ]",
                "missing": "l",
                "mean": "Tâm lý học",
            },
            {
                "word": "pharmaceutical",
                "display": "PHARMACEUTICA [ L ]",
                "missing": "l",
                "mean": "Dược phẩm",
            },
        ],
    },
    "C2": {
        "Environment & Nature": [
            {
                "word": "sustainability",
                "display": "SUSTAINABILIT [ Y ]",
                "missing": "y",
                "mean": "Tính bền vững",
            },
            {
                "word": "anthropogenic",
                "display": "ANTHROPOGENI [ C ]",
                "missing": "c",
                "mean": "Do con người gây ra",
            },
            {
                "word": "biogeochemical",
                "display": "BIOGEOCHEMICAL [ L ]",
                "missing": "l",
                "mean": "Sinh địa hóa",
            },
            {
                "word": "desertification",
                "display": "DESERTIFICATIO [ N ]",
                "missing": "n",
                "mean": "Hoang mạc hóa",
            },
        ],
        "Technology & AI": [
            {
                "word": "supercomputing",
                "display": "SUPERCOMPUTIN [ G ]",
                "missing": "g",
                "mean": "Siêu máy tính",
            },
            {
                "word": "epistemology",
                "display": "EPISTEMOLOG [ Y ]",
                "missing": "y",
                "mean": "Nhận thức luận",
            },
            {
                "word": "interoperability",
                "display": "INTEROPERABILIT [ Y ]",
                "missing": "y",
                "mean": "Tính tương tác",
            },
        ],
        "Education & Career": [
            {
                "word": "institutionalization",
                "display": "INSTITUTIONALIZATIO [ N ]",
                "missing": "n",
                "mean": "Thể chế hóa",
            },
            {
                "word": "interdisciplinary",
                "display": "INTERDISCIPLINAR [ Y ]",
                "missing": "y",
                "mean": "Liên ngành",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "neuroplasticity",
                "display": "NEUROPLASTICIT [ Y ]",
                "missing": "y",
                "mean": "Tính dẻo thần kinh",
            },
            {
                "word": "psychoneuroimmunology",
                "display": "PSYCHONEUROIMMUNOLOG [ Y ]",
                "missing": "y",
                "mean": "Miễn dịch học thần kinh",
            },
            {
                "word": "homeostasis",
                "display": "HOMEOSTASI [ S ]",
                "missing": "s",
                "mean": "Cân bằng nội môi",
            },
        ],
    },
}

database_json = json.dumps(vocab_database)

if keyboard_layout == "Laptop / PC (QWERTY)":
  kb_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
else:
  kb_rows = ["123", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

kb_json = json.dumps(kb_rows)

# --- MÃ NGUỒN GAME HTML/JS ---
game_code = (
    """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            background: #1e1e2f;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
        }
        #game-container {
            position: relative;
            width: 100%;
            max-width: 850px;
            margin: 0 auto;
        }
        canvas {
            background: linear-gradient(180deg, #2b1055, #7597de);
            display: block;
            width: 100%;
            height: auto;
            border-radius: 12px;
            border: 3px solid #ff69b4;
            box-shadow: 0 0 25px rgba(255, 105, 180, 0.4);
        }
        .info-bar {
            display: flex;
            justify-content: space-between;
            background: #282a36;
            padding: 10px 20px;
            border-radius: 8px;
            margin-bottom: 8px;
            font-weight: bold;
            font-size: 16px;
            color: #f1fa8c;
        }
        .virtual-keyboard {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            margin-top: 12px;
            padding: 0 5px;
        }
        .kb-row {
            display: flex;
            gap: 6px;
            justify-content: center;
        }
        .key-btn {
            background: #44475a;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 12px 15px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px #282a36;
            min-width: 38px;
        }
        .key-btn:active {
            background: #ff69b4;
            transform: translateY(2px);
            box-shadow: 0 2px #282a36;
        }
    </style>
</head>
<body>

    <div id="game-container">
        <div class="info-bar">
            <span id="level-info">📌 Cấp độ: """
    + selected_level
    + " | Chủ đề: "
    + selected_topic
    + """</span>
            <span id="score-info">🏆 Điểm: 0</span>
        </div>
        <canvas id="gameCanvas" width="850" height="540"></canvas>
        <div class="virtual-keyboard" id="keyboard"></div>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const vocabDatabase = """
    + database_json
    + """
        const selectedTopic = """
    + json.dumps(selected_topic)
    + """
        let currentLevel = """
    + json.dumps(selected_level)
    + """
        const levelsOrder = ["A1", "A2", "B1", "B2", "C1", "C2"];

        let currentVocabList = [];
        let usedVocabQueue = [];

        function loadVocabularyForLevel(lvl) {
            let levelData = vocabDatabase[lvl] || vocabDatabase["B2"];
            let topicList = levelData[selectedTopic] || Object.values(levelData)[0];
            currentVocabList = [...topicList].sort(() => Math.random() - 0.5);
            usedVocabQueue = [];
        }

        loadVocabularyForLevel(currentLevel);

        const kbRows = """
    + kb_json
    + """
        let score = 0;
        let targets = [];
        let bullets = [];
        let particles = [];
        let isGameOver = false;
        let spawnTimer = 0;
        let levelUpMessageTimer = 0;

        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        function playSound(type) {
            if (!audioCtx) return;
            let osc = audioCtx.createOscillator();
            let gainNode = audioCtx.createGain();
            osc.connect(gainNode);
            gainNode.connect(audioCtx.destination);

            if (type === "shoot") {
                osc.type = "sine";
                osc.frequency.setValueAtTime(600, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(300, audioCtx.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.1);
            } else if (type === "hit") {
                osc.type = "triangle";
                osc.frequency.setValueAtTime(400, audioCtx.currentTime);
                osc.frequency.setValueAtTime(800, audioCtx.currentTime + 0.08);
                gainNode.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.2);
            } else if (type === "levelup") {
                osc.type = "square";
                osc.frequency.setValueAtTime(500, audioCtx.currentTime);
                osc.frequency.setValueAtTime(750, audioCtx.currentTime + 0.15);
                osc.frequency.setValueAtTime(1000, audioCtx.currentTime + 0.3);
                gainNode.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.4);
            } else if (type === "gameover") {
                osc.type = "sawtooth";
                osc.frequency.setValueAtTime(200, audioCtx.currentTime);
                osc.frequency.linearRampToValueAtTime(80, audioCtx.currentTime + 0.4);
                gainNode.gain.setValueAtTime(0.2, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.4);
            }
        }

        const player = {
            x: canvas.width / 2 - 25,
            y: canvas.height - 50,
            width: 50,
            height: 50
        };

        function spawnTarget() {
            if (currentVocabList.length === 0) {
                loadVocabularyForLevel(currentLevel);
            }

            let activeWords = targets.map(t => t.word);
            let available = currentVocabList.filter(v => !activeWords.includes(v.word) && !usedVocabQueue.includes(v.word));

            if (available.length === 0) {
                available = currentVocabList.filter(v => !activeWords.includes(v.word));
                if (available.length === 0) available = currentVocabList;
            }

            const randomIndex = Math.floor(Math.random() * available.length);
            const item = available[randomIndex];

            usedVocabQueue.push(item.word);
            if (usedVocabQueue.length > 5) usedVocabQueue.shift();

            let randomX = Math.random() * (canvas.width - 260) + 15;
            let currentSpeed = 0.3 + (levelsOrder.indexOf(currentLevel) * 0.04);

            targets.push({
                ...item,
                x: randomX,
                y: -70,
                speed: currentSpeed
            });
        }

        function handleInput(typedKey) {
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            if (isGameOver) return;

            typedKey = typedKey.toLowerCase();

            for (let i = 0; i < targets.length; i++) {
                let t = targets[i];
                if (typedKey === t.missing) {
                    playSound("shoot");
                    bullets.push({
                        x: player.x + player.width / 2,
                        y: player.y,
                        targetId: i,
                        targetX: t.x + 110,
                        targetY: t.y + 25,
                        speed: 10
                    });
                    break;
                }
            }
        }

        document.addEventListener("keydown", function(e) {
            handleInput(e.key);
        });

        const keyboardDiv = document.getElementById("keyboard");
        keyboardDiv.innerHTML = "";
        kbRows.forEach(rowStr => {
            const rowDiv = document.createElement("div");
            rowDiv.className = "kb-row";
            for (let char of rowStr) {
                const btn = document.createElement("button");
                btn.innerText = char.toUpperCase();
                btn.className = "key-btn";
                btn.onclick = () => handleInput(char);
                rowDiv.appendChild(btn);
            }
            keyboardDiv.appendChild(rowDiv);
        });

        function update() {
            if (isGameOver) return;

            spawnTimer++;
            if (spawnTimer > 130) {
                spawnTarget();
                spawnTimer = 0;
            }

            for (let i = targets.length - 1; i >= 0; i--) {
                targets[i].y += targets[i].speed;

                if (targets[i].y > canvas.height - 70) {
                    isGameOver = true;
                    playSound("gameover");
                }
            }

            for (let i = bullets.length - 1; i >= 0; i--) {
                let b = bullets[i];
                b.y -= b.speed;

                let targetObj = targets[b.targetId];
                if (targetObj && b.y <= targetObj.y + 35) {
                    score += 10;
                    document.getElementById("score-info").innerText = "🏆 Điểm: " + score;
                    playSound("hit");
                    createExplosion(targetObj.x + 110, targetObj.y + 25);

                    if (score > 0 && score % 100 === 0) {
                        let currentIndex = levelsOrder.indexOf(currentLevel);
                        if (currentIndex < levelsOrder.length - 1) {
                            currentLevel = levelsOrder[currentIndex + 1];
                            loadVocabularyForLevel(currentLevel);
                            playSound("levelup");
                            levelUpMessageTimer = 90;
                            document.getElementById("level-info").innerText = "📌 Cấp độ: " + currentLevel + " | Chủ đề: " + selectedTopic;
                        }
                    }

                    targets.splice(b.targetId, 1);
                    bullets.splice(i, 1);
                    break;
                }
            }

            if (levelUpMessageTimer > 0) levelUpMessageTimer--;

            for (let i = particles.length - 1; i >= 0; i--) {
                let p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.alpha -= 0.03;
                if (p.alpha <= 0) particles.splice(i, 1);
            }
        }

        function createExplosion(x, y) {
            for (let i = 0; i < 15; i++) {
                particles.push({
                    x: x,
                    y: y,
                    vx: (Math.random() - 0.5) * 6,
                    vy: (Math.random() - 0.5) * 6,
                    alpha: 1,
                    color: "#ff69b4"
                });
            }
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "#ff69b4";
            ctx.beginPath();
            ctx.arc(player.x + 25, player.y + 25, 20, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = "#000";
            ctx.font = "26px Arial";
            ctx.fillText("🦋", player.x + 8, player.y + 35);

            targets.forEach(t => {
                ctx.fillStyle = "#ff9800";
                ctx.shadowColor = "#ff5722";
                ctx.shadowBlur = 10;
                // Phóng to kích thước thẻ chứa từ vựng
                ctx.fillRect(t.x, t.y, 230, 60);
                ctx.shadowBlur = 0;

                // Phóng to cực đại chữ tiếng Anh (24px đậm)
                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 24px Arial";
                ctx.fillText(t.display, t.x + 12, t.y + 33);

                // Phóng to nghĩa tiếng Việt (14px)
                ctx.fillStyle = "#f1fa8c";
                ctx.font = "bold italic 14px Arial";
                ctx.fillText("(" + t.mean + ")", t.x + 12, t.y + 52);
            });

            ctx.fillStyle = "#00ffff";
            bullets.forEach(b => {
                ctx.beginPath();
                ctx.arc(b.x, b.y, 6, 0, Math.PI * 2);
                ctx.fill();
            });

            particles.forEach(p => {
                ctx.save();
                ctx.globalAlpha = p.alpha;
                ctx.fillStyle = p.color;
                ctx.fillRect(p.x, p.y, 4, 4);
                ctx.restore();
            });

            if (levelUpMessageTimer > 0) {
                ctx.fillStyle = "rgba(255, 215, 0, 0.9)";
                ctx.font = "bold 32px Arial";
                ctx.fillText("🎉 THĂNG CẤP LÊN " + currentLevel + "! 🎉", canvas.width / 2 - 220, 100);
            }

            if (isGameOver) {
                ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#ff4757";
                ctx.font = "bold 34px Arial";
                ctx.fillText("GAME OVER", canvas.width / 2 - 100, 200);

                ctx.fillStyle = "#ffffff";
                ctx.font = "20px Arial";
                ctx.fillText("Tổng điểm đạt được: " + score, canvas.width / 2 - 100, 245);
                ctx.fillText("Tải lại trang để thử thách lại nhé!", canvas.width / 2 - 130, 285);
            }
        }

        function loop() {
            update();
            draw();
            requestAnimationFrame(loop);
        }

        spawnTarget();
        loop();
    </script>
</body>
</html>
"""
)

st.components.v1.html(game_code, height=650)
