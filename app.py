import json
import streamlit as st

st.set_page_config(
    page_title="IELTS & CEFR Vocabulary Shooter",
    page_icon="🦋",
    layout="centered",
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng Đa Thiết Bị (A1 - C2)")
st.write(
    "Hỗ trợ trên Điện thoại, Máy tính bảng, Laptop và PC! Chọn cấp độ và chủ"
    " đề để bắt đầu."
)

# --- PHẦN ĐIỀU KHIỂN TRÊN GIAO DIỆN STREAMLIT ---
col1, col2 = st.columns(2)

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

st.info(
    f"👉 Đang ôn luyện: Trình độ **{selected_level}** - Chủ đề:"
    f" **{selected_topic}**"
)

# Dữ liệu từ vựng mẫu phân loại theo chủ đề và trình độ
vocab_data = {
    "A1": [
        {
            "word": "water",
            "display": "wate_",
            "missing": "r",
            "mean": "Nước",
            "topic": "Environment & Nature",
        },
        {
            "word": "plant",
            "display": "plan_",
            "missing": "t",
            "mean": "Thực vật",
            "topic": "Environment & Nature",
        },
        {
            "word": "phone",
            "display": "phon_",
            "missing": "e",
            "mean": "Điện thoại",
            "topic": "Technology & AI",
        },
        {
            "word": "study",
            "display": "stud_",
            "missing": "y",
            "mean": "Học tập",
            "topic": "Education & Career",
        },
    ],
    "A2": [
        {
            "word": "energy",
            "display": "energ_",
            "missing": "y",
            "mean": "N năng lượng",
            "topic": "Environment & Nature",
        },
        {
            "word": "screen",
            "display": "scree_",
            "missing": "n",
            "mean": "Màn hình",
            "topic": "Technology & AI",
        },
        {
            "word": "school",
            "display": "schoo_",
            "missing": "l",
            "mean": "Trường học",
            "topic": "Education & Career",
        },
        {
            "word": "health",
            "display": "healt_",
            "missing": "h",
            "mean": "Sức khỏe",
            "topic": "Health & Lifestyle",
        },
    ],
    "B1": [
        {
            "word": "recycle",
            "display": "recycl_",
            "missing": "e",
            "mean": "Tái chế",
            "topic": "Environment & Nature",
        },
        {
            "word": "digital",
            "display": "digita_",
            "missing": "l",
            "mean": "Kỹ thuật số",
            "topic": "Technology & AI",
        },
        {
            "word": "career",
            "display": "caree_",
            "missing": "r",
            "mean": "Sự nghiệp",
            "topic": "Education & Career",
        },
        {
            "word": "fitness",
            "display": "fitnes_",
            "missing": "s",
            "mean": "Thể lực",
            "topic": "Health & Lifestyle",
        },
    ],
    "B2": [
        {
            "word": "pollution",
            "display": "pollutio_",
            "missing": "n",
            "mean": "Sự ô nhiễm",
            "topic": "Environment & Nature",
        },
        {
            "word": "algorithm",
            "display": "algorith_",
            "missing": "m",
            "mean": "Thuật toán",
            "topic": "Technology & AI",
        },
        {
            "word": "academic",
            "display": "academi_",
            "missing": "c",
            "mean": "Học thuật",
            "topic": "Education & Career",
        },
        {
            "word": "nutrition",
            "display": "nutritio_",
            "missing": "n",
            "mean": "Dinh dưỡng",
            "topic": "Health & Lifestyle",
        },
    ],
    "C1": [
        {
            "word": "biodiversity",
            "display": "biodiversit_",
            "missing": "y",
            "mean": "Đa dạng sinh học",
            "topic": "Environment & Nature",
        },
        {
            "word": "automation",
            "display": "automatio_",
            "missing": "n",
            "mean": "Tự động hóa",
            "topic": "Technology & AI",
        },
        {
            "word": "curriculum",
            "display": "curriculu_",
            "missing": "m",
            "mean": "Chương trình học",
            "topic": "Education & Career",
        },
        {
            "word": "metabolism",
            "display": "metabolis_",
            "missing": "m",
            "mean": "Sự trao đổi chất",
            "topic": "Health & Lifestyle",
        },
    ],
    "C2": [
        {
            "word": "sustainability",
            "display": "sustainabilit_",
            "missing": "y",
            "mean": "Tính bền vững",
            "topic": "Environment & Nature",
        },
        {
            "word": "implementation",
            "display": "implementatio_",
            "missing": "n",
            "mean": "Sự thi hành",
            "topic": "Education & Career",
        },
    ],
}

filtered_words = [
    item
    for item in vocab_data.get(selected_level, vocab_data["B2"])
    if item["topic"] == selected_topic
]
if not filtered_words:
  filtered_words = vocab_data.get(selected_level, vocab_data["B2"])

vocab_json = json.dumps(filtered_words)
speed_val = 1.4 if selected_level in ["C1", "C2"] else 1.2

# --- MÃ NGUỒN GAME HTML/JS HỖ TRỢ RESPONSIVE VÀ BÀN PHÍM ẢO ---
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
            max-width: 480px;
            margin: 0 auto;
        }}
        canvas {{
            background: linear-gradient(180deg, #2b1055, #7597de);
            display: block;
            width: 100%;
            height: auto;
            border-radius: 12px;
            border: 3px solid #ff69b4;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.4);
        }}
        .info-bar {{
            display: flex;
            justify-content: space-between;
            background: #282a36;
            padding: 8px 15px;
            border-radius: 8px;
            margin-bottom: 8px;
            font-weight: bold;
            font-size: 14px;
            color: #f1fa8c;
        }}
        /* Bàn phím ảo dành cho điện thoại/máy tính bảng */
        .virtual-keyboard {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 5px;
            margin-top: 10px;
            padding: 0 5px;
        }}
        .key-btn {{
            background: #44475a;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 14px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px #282a36;
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
        <canvas id="gameCanvas" width="480" height="420"></canvas>
        
        <!-- Bàn phím ảo bấm trực tiếp trên màn hình cảm ứng -->
        <div class="virtual-keyboard" id="keyboard"></div>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const vocabList = {vocab_json};
        const fallSpeed = {speed_val};

        let score = 0;
        let currentTarget = null;
        let bullets = [];
        let particles = [];
        let isGameOver = false;

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

        function spawnTarget() {{
            if (vocabList.length === 0) return;
            const randomIndex = Math.floor(Math.random() * vocabList.length);
            const item = vocabList[randomIndex];
            currentTarget = {{
                ...item,
                x: Math.random() * (canvas.width - 140) + 15,
                y: -40,
                speed: fallSpeed
            }};
        }}

        function handleInput(typedKey) {{
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            if (isGameOver || !currentTarget) return;

            if (typedKey === currentTarget.missing) {{
                playSound("shoot");
                bullets.push({{
                    x: player.x + player.width / 2,
                    y: player.y,
                    targetX: currentTarget.x + 60,
                    targetY: currentTarget.y + 20,
                    speed: 12
                }});
            }}
        }}

        // Hỗ trợ gõ phím từ bàn phím máy tính / laptop
        document.addEventListener("keydown", function(e) {{
            handleInput(e.key.toLowerCase());
        }});

        // Tự động tạo bàn phím ảo A-Z cho điện thoại và máy tính bảng
        const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
        const keyboardDiv = document.getElementById("keyboard");
        alphabet.forEach(letter => {{
            const btn = document.createElement("button");
            btn.innerText = letter.toUpperCase();
            btn.className = "key-btn";
            btn.onclick = () => handleInput(letter);
            keyboardDiv.appendChild(btn);
        }});

        function update() {{
            if (isGameOver) return;

            if (!currentTarget) {{
                spawnTarget();
            }} else {{
                currentTarget.y += currentTarget.speed;

                if (currentTarget.y > canvas.height - 60) {{
                    isGameOver = true;
                    playSound("gameover");
                }}
            }}

            for (let i = bullets.length - 1; i >= 0; i--) {{
                let b = bullets[i];
                b.y -= b.speed;

                if (currentTarget && b.y <= currentTarget.y + 30) {{
                    score += 10;
                    document.getElementById("score-info").innerText = "🏆 Điểm: " + score;
                    playSound("hit");
                    createExplosion(currentTarget.x + 50, currentTarget.y + 20);
                    bullets.splice(i, 1);
                    currentTarget = null;
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

            // Vẽ Chú bướm
            ctx.fillStyle = "#ff69b4";
            ctx.beginPath();
            ctx.arc(player.x + 25, player.y + 25, 20, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = "#000";
            ctx.font = "24px Arial";
            ctx.fillText("🦋", player.x + 10, player.y + 34);

            // Vẽ Từ vựng
            if (currentTarget) {{
                ctx.fillStyle = "#ff9800";
                ctx.shadowColor = "#ff5722";
                ctx.shadowBlur = 10;
                ctx.fillRect(currentTarget.x, currentTarget.y, 130, 40);
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 17px Arial";
                ctx.fillText(currentTarget.display, currentTarget.x + 10, currentTarget.y + 23);

                ctx.fillStyle = "#e0e0e0";
                ctx.font = "italic 11px Arial";
                ctx.fillText("(" + currentTarget.mean + ")", currentTarget.x + 10, currentTarget.y + 36);
            }}

            // Vẽ Đạn
            ctx.fillStyle = "#00ffff";
            bullets.forEach(b => {{
                ctx.beginPath();
                ctx.arc(b.x, b.y, 6, 0, Math.PI * 2);
                ctx.fill();
            }});

            // Vẽ Hiệu ứng hạt
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
                ctx.font = "bold 28px Arial";
                ctx.fillText("GAME OVER", canvas.width / 2 - 80, 180);

                ctx.fillStyle = "#ffffff";
                ctx.font = "16px Arial";
                ctx.fillText("Từ vựng đã chạm đáy!", canvas.width / 2 - 85, 220);
                ctx.fillText("Tải lại trang để chơi lại vòng mới!", canvas.width / 2 - 115, 250);
            }}
        }}

        function loop() {{
            update();
            draw();
            requestAnimationFrame(loop);
        }}

        loop();
    </script>
</body>
</html>
"""

st.components.v1.html(game_code, height=620)
