import json
import random
import streamlit as st

st.set_page_config(
    page_title="IELTS Vocabulary Shooter Pro", page_icon="🦋", layout="wide"
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng IELTS - Chinh Phục Cấp Độ")
st.write(
    "Hệ thống từ vựng chuẩn IELTS Reading, chữ cái cần điền xuất hiện ngẫu nhiên"
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

# KHO TỪ VỰNG GỐC (Hệ thống sẽ tự động chọn ngẫu nhiên vị trí chữ cái cần điền)
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
        "Education & Career": [
            {"word": "academic", "mean": "Học thuật"},
            {"word": "curriculum", "mean": "Chương trình học"},
            {"word": "scholarship", "mean": "Học bổng"},
            {"word": "profession", "mean": "Nghề nghiệp"},
            {"word": "qualification", "mean": "Trình độ chuyên môn"},
        ],
        "Health & Lifestyle": [
            {"word": "nutrition", "mean": "Dinh dưỡng"},
            {"word": "metabolism", "mean": "Trao đổi chất"},
            {"word": "wellbeing", "mean": "Sức khỏe toàn diện"},
            {"word": "epidemic", "mean": "Dịch bệnh"},
        ],
    },
    "C1": {
        "Environment & Nature": [
            {"word": "biodiversity", "mean": "Đa dạng sinh học"},
            {"word": "catastrophic", "mean": "Thảm khốc"},
            {"word": "deforestation", "mean": "Nạn phá rừng"},
            {"word": "extinction", "mean": "Sự tuyệt chủng"},
        ],
        "Technology & AI": [
            {"word": "cybersecurity", "mean": "An ninh mạng"},
            {"word": "cryptography", "mean": "Mật mã học"},
            {"word": "implementation", "mean": "Sự triển khai"},
            {"word": "biometrics", "mean": "Sinh trắc học"},
        ],
        "Education & Career": [
            {"word": "dissertation", "mean": "Luận văn"},
            {"word": "pedagogy", "mean": "Sư phạm"},
            {"word": "entrepreneur", "mean": "Doanh nhân"},
            {"word": "bureaucracy", "mean": "Nạn quan liêu"},
        ],
        "Health & Lifestyle": [
            {"word": "cardiovascular", "mean": "Tim mạch"},
            {"word": "longevity", "mean": "Tuổi thọ"},
            {"word": "psychological", "mean": "Tâm lý học"},
            {"word": "pharmaceutical", "mean": "Dược phẩm"},
        ],
    },
    "C2": {
        "Environment & Nature": [
            {"word": "sustainability", "mean": "Tính bền vững"},
            {"word": "anthropogenic", "mean": "Do con người gây ra"},
            {"word": "biogeochemical", "mean": "Sinh địa hóa"},
            {"word": "desertification", "mean": "Hoang mạc hóa"},
        ],
        "Technology & AI": [
            {"word": "supercomputing", "mean": "Siêu máy tính"},
            {"word": "epistemology", "mean": "Nhận thức luận"},
            {"word": "interoperability", "mean": "Tính tương tác"},
        ],
        "Education & Career": [
            {"word": "institutionalization", "mean": "Thể chế hóa"},
            {"word": "interdisciplinary", "mean": "Liên ngành"},
        ],
        "Health & Lifestyle": [
            {"word": "neuroplasticity", "mean": "Tính dẻo thần kinh"},
            {"word": "psychoneuroimmunology", "mean": "Miễn dịch học thần kinh"},
            {"word": "homeostasis", "mean": "Cân bằng nội môi"},
        ],
    },
}

# Tiền xử lý để tự động ẩn ký tự ngẫu nhiên cho từng từ
processed_database = {}
for lvl, topics in raw_vocab_database.items():
  processed_database[lvl] = {}
  for top, words in topics.items():
    processed_words = []
    for item in words:
      w = item["word"].upper()
      idx = random.randint(
          0, len(w) - 1
      )  # Chọn ngẫu nhiên vị trí chữ cái bị ẩn
      missing_char = w[idx].lower()

      # Tạo chuỗi hiển thị dạng trực quan (Ví dụ: WAT [ E ] R)
      display_str = ""
      for i, char in enumerate(w):
        if i == idx:
          display_str += f" [{char}] "
        else:
          display_str += char

      processed_words.append({
          "word": item["word"],
          "display": display_str.strip(),
          "missing": missing_char,
          "mean": item["mean"],
      })
    processed_database[lvl][top] = processed_words

database_json = json.dumps(processed_database)

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

            let randomX = Math.random() * (canvas.width - 280) + 15;
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
                        targetX: t.x + 120,
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
                    createExplosion(targetObj.x + 120, targetObj.y + 25);

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
                // Khung chứa từ vựng rộng rãi
                ctx.fillRect(t.x, t.y, 250, 60);
                ctx.shadowBlur = 0;

                // Chữ tiếng Anh hiển thị rõ ràng, chữ cái cần điền nằm trong ngoặc vuông [ ]
                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 22px Arial";
                ctx.fillText(t.display, t.x + 12, t.y + 32);

                // Nghĩa tiếng Việt
                ctx.fillStyle = "#f1fa8c";
                ctx.font = "bold italic 13px Arial";
                ctx.fillText("(" + t.mean + ")", t.x + 12, t.y + 50);
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
