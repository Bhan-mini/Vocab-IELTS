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
        ],
        "Education & Career": [
            {"word": "study", "display": "st_dy", "missing": "u", "mean": "Học tập"},
            {"word": "book", "display": "bo_k", "missing": "o", "mean": "Sách"},
            {"word": "class", "display": "cl_ss", "missing": "a", "mean": "Lớp học"},
            {"word": "job", "display": "j_b", "missing": "o", "mean": "Công việc"},
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
        ],
        "Education & Career": [
            {"word": "career", "display": "car_er", "missing": "e", "mean": "Sự nghiệp"},
            {"word": "lesson", "display": "less_n", "missing": "o", "mean": "Bài học"},
            {"word": "office", "display": "off_ce", "missing": "i", "mean": "Văn phòng"},
        ],
        "Health & Lifestyle": [
            {"word": "fitness", "display": "fitn_ss", "missing": "e", "mean": "Thể lực"},
            {"word": "doctor", "display": "doct_r", "missing": "o", "mean": "Bác sĩ"},
            {"word": "travel", "display": "trav_l", "missing": "e", "mean": "Du lịch"},
        ],
    },
    "B1": {
        "Environment & Nature": [
            {"word": "recycle", "display": "recycl_e", "missing": "e", "mean": "Tái chế"},
            {"word": "climate", "display": "clim_te", "missing": "a", "mean": "Khí hậu"},
            {"word": "natural", "display": "natur_l", "missing": "a", "mean": "Tự nhiên"},
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
        ],
        "Health & Lifestyle": [
            {"word": "disease", "display": "disea_e", "missing": "s", "mean": "Bệnh tật"},
            {"word": "habit", "display": "hab_t", "missing": "i", "mean": "Thói quen"},
            {"word": "relax", "display": "rel_x", "missing": "a", "mean": "Thư giãn"},
        ],
    },
    "B2": {
        "Environment & Nature": [
            {
                "word": "pollution",
                "display": "pollut_on",
                "missing": "i",
                "mean": "Sự ô nhiễm",
            },
            {"word": "ecosystem", "display": "ecosyst_m", "missing": "e", "mean": "Hệ sinh thái"},
            {
                "word": "atmosphere",
                "display": "atmosph_re",
                "missing": "e",
                "mean": "Bầu khí quyển",
            },
        ],
        "Technology & AI": [
            {
                "word": "algorithm",
                "display": "algorith_m",
                "missing": "m",
                "mean": "Thuật toán",
            },
            {
                "word": "automation",
                "display": "automat_on",
                "missing": "i",
                "mean": "Tự động hóa",
            },
            {"word": "database", "display": "databa_e", "missing": "s", "mean": "Cơ sở dữ liệu"},
        ],
        "Education & Career": [
            {
                "word": "academic",
                "display": "academi_c",
                "missing": "c",
                "mean": "Học thuật",
            },
            {
                "word": "curriculum",
                "display": "curricul_m",
                "missing": "u",
                "mean": "Chương trình giảng dạy",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "nutrition",
                "display": "nutriti_n",
                "missing": "o",
                "mean": "Dinh dưỡng",
            },
            {
                "word": "metabolism",
                "display": "metaboli_m",
                "missing": "s",
                "mean": "Trao đổi chất",
            },
        ],
    },
    "C1": {
        "Environment & Nature": [
            {
                "word": "biodiversity",
                "display": "biodiversit_y",
                "missing": "y",
                "mean": "Đa dạng sinh học",
            },
            {
                "word": "catastrophic",
                "display": "catastroph_c",
                "missing": "i",
                "mean": "Thảm khốc",
            },
        ],
        "Technology & AI": [
            {
                "word": "cybersecurity",
                "display": "cybersecurit_y",
                "missing": "y",
                "mean": "An ninh mạng",
            },
            {
                "word": "cryptography",
                "display": "cryptograph_y",
                "missing": "y",
                "mean": "Mật mã học",
            },
        ],
        "Education & Career": [
            {
                "word": "dissertation",
                "display": "dissertat_on",
                "missing": "i",
                "mean": "Luận văn",
            },
            {
                "word": "pedagogy",
                "display": "pedagog_y",
                "missing": "y",
                "mean": "Sư phạm",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "cardiovascular",
                "display": "cardiovascul_r",
                "missing": "a",
                "mean": "Tim mạch",
            },
            {
                "word": "longevity",
                "display": "longevit_y",
                "missing": "y",
                "mean": "Tuổi thọ",
            },
        ],
    },
    "C2": {
        "Environment & Nature": [
            {
                "word": "sustainability",
                "display": "sustainabilit_y",
                "missing": "y",
                "mean": "Tính bền vững",
            },
            {
                "word": "anthropogenic",
                "display": "anthropogeni_c",
                "missing": "c",
                "mean": "Do con người gây ra",
            },
        ],
        "Technology & AI": [
            {
                "word": "supercomputing",
                "display": "supercomputin_g",
                "missing": "g",
                "mean": "Siêu máy tính",
            },
            {
                "word": "epistemology",
                "display": "epistemolog_y",
                "missing": "y",
                "mean": "Nhận thức luận",
            },
        ],
        "Education & Career": [
            {
                "word": "institutionalization",
                "display": "institutionalizat_on",
                "missing": "i",
                "mean": "Thể chế hóa",
            },
        ],
        "Health & Lifestyle": [
            {
                "word": "neuroplasticity",
                "display": "neuroplasticit_y",
                "missing": "y",
                "mean": "Tính dẻo thần kinh",
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

# --- MÃ NGUỒN GAME HTML/JS AN TOÀN ---
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
            max-width: 750px;
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
            font-size: 15px;
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
            min-width: 36px;
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
        <canvas id="gameCanvas" width="750" height="500"></canvas>
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
            if (usedVocabQueue.length > 3) usedVocabQueue.shift();

            let randomX = Math.random() * (canvas.width - 200) + 20;
            let currentSpeed = 0.35 + (levelsOrder.indexOf(currentLevel) * 0.05);

            targets.push({
                ...item,
                x: randomX,
                y: -60,
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
                        targetX: t.x + 80,
                        targetY: t.y + 20,
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
            if (spawnTimer > 120) {
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
                if (targetObj && b.y <= targetObj.y + 30) {
                    score += 10;
                    document.getElementById("score-info").innerText = "🏆 Điểm: " + score;
                    playSound("hit");
                    createExplosion(targetObj.x + 80, targetObj.y + 20);

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
                ctx.fillRect(t.x, t.y, 170, 45);
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 17px Arial";
                ctx.fillText(t.display, t.x + 10, t.y + 24);

                ctx.fillStyle = "#e0e0e0";
                ctx.font = "italic 11px Arial";
                ctx.fillText("(" + t.mean + ")", t.x + 10, t.y + 40);
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
                ctx.font = "bold 28px Arial";
                ctx.fillText("🎉 THĂNG CẤP LÊN " + currentLevel + "! 🎉", canvas.width / 2 - 180, 100);
            }

            if (isGameOver) {
                ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#ff4757";
                ctx.font = "bold 32px Arial";
                ctx.fillText("GAME OVER", canvas.width / 2 - 90, 200);

                ctx.fillStyle = "#ffffff";
                ctx.font = "18px Arial";
                ctx.fillText("Tổng điểm đạt được: " + score, canvas.width / 2 - 90, 240);
                ctx.fillText("Tải lại trang để thử thách lại nhé!", canvas.width / 2 - 120, 280);
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

st.components.v1.html(game_code, height=620)
