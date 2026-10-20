import streamlit as st

st.set_page_config(
    page_title="IELTS & CEFR Vocabulary Shooter",
    page_icon="🦋",
    layout="centered",
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng Đa Chủ Đề (A1 - C2)")
st.write(
    "Lựa chọn cấp độ, chủ đề từ vựng yêu thích và giúp chú bướm bay lượn thu thập kiến thức!"
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
    f"👉 Đang ôn luyện: Trình độ **{selected_level}** - Chủ đề: **{selected_topic}**"
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
            "mean": "Năng lượng",
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

# Lọc từ vựng theo Level và Topic mà người dùng chọn
filtered_words = [
    item
    for item in vocab_data.get(selected_level, vocab_data["B2"])
    if item["topic"] == selected_topic
]
# Nếu chủ đề ít từ quá, lấy phòng hờ toàn bộ level đó để game không bị lỗi trống từ
if not filtered_words:
  filtered_words = vocab_data.get(selected_level, vocab_data["B2"])

import json

vocab_json = json.dumps(filtered_words)

# --- MÃ NGUỒN GAME HTML/JS NHÚNG KÈM HIỆU ỨNG ÂM THANH ---
game_code = f"""
<!DOCTYPE html>
<html>
<head>
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
            width: 500px;
            margin: 10px auto;
        }}
        canvas {{
            background: linear-gradient(180deg, #2b1055, #7597de);
            display: block;
            border-radius: 12px;
            border: 3px solid #ff69b4;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.4);
        }}
        .info-bar {{
            display: flex;
            justify-content: space-between;
            background: #282a36;
            padding: 10px 20px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-weight: bold;
            color: #f1fa8c;
        }}
    </style>
</head>
<body>

    <div id="game-container">
        <div class="info-bar">
            <span id="unit-info">📌 {selected_level} - {selected_topic}</span>
            <span id="score-info">🏆 Điểm: 0</span>
        </div>
        <canvas id="gameCanvas" width="500" height="550"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        // Nhận dữ liệu từ vựng truyền từ Python vào JavaScript
        const vocabList = {vocab_json};

        let score = 0;
        let currentTarget = null;
        let bullets = [];
        let particles = [];
        let isGameOver = false;

        // Sử dụng Web Audio API để tạo hiệu ứng âm thanh trực tiếp (Không cần file nhạc ngoài, chạy cực mượt)
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        function playSound(type) {{
            if (!audioCtx) return;
            let osc = audioCtx.createOscillator();
            let gainNode = audioCtx.createGain();
            osc.connect(gainNode);
            gainNode.connect(audioCtx.destination);

            if (type === "shoot") {{
                // Âm thanh đạn bắn (Tiếng bíp cao vút ngắn)
                osc.type = "sine";
                osc.frequency.setValueAtTime(600, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(300, audioCtx.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.1);
            }} else if (type === "hit") {{
                // Âm thanh ghi điểm / bắn trúng (Tiếng chuông vui tai)
                osc.type = "triangle";
                osc.frequency.setValueAtTime(400, audioCtx.currentTime);
                osc.frequency.setValueAtTime(800, audioCtx.currentTime + 0.08);
                gainNode.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.2);
            }} else if (type === "gameover") {{
                // Âm thanh thua cuộc (Tiếng trầm buồn)
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
            y: canvas.height - 60,
            width: 50,
            height: 50
        }};

        function spawnTarget() {{
            if (vocabList.length === 0) return;
            const randomIndex = Math.floor(Math.random() * vocabList.length);
            const item = vocabList[randomIndex];
            currentTarget = {{
                ...item,
                x: Math.random() * (canvas.width - 150) + 20,
                y: -40,
                speed: 1.2 + ({["A1","A2"].includes(selected_level) ? 0 : 0.4}) // Cấp độ cao hơn rơi nhanh hơn một chút
            }};
        }}

        // Bắt sự kiện gõ phím của học sinh
        document.addEventListener("keydown", function(e) {{
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            if (isGameOver || !currentTarget) return;

            const typedKey = e.key.toLowerCase();
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
        }});

        function update() {{
            if (isGameOver) return;

            if (!currentTarget) {{
                spawnTarget();
            }} else {{
                currentTarget.y += currentTarget.speed;

                if (currentTarget.y > canvas.height - 80) {{
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

            // 1. Vẽ Chú bướm nhân vật
            ctx.fillStyle = "#ff69b4";
            ctx.beginPath();
            ctx.arc(player.x + 25, player.y + 25, 20, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = "#000";
            ctx.font = "24px Arial";
            ctx.fillText("🦋", player.x + 10, player.y + 34);

            // 2. Vẽ Từ vựng mục tiêu
            if (currentTarget) {{
                ctx.fillStyle = "#ff9800";
                ctx.shadowColor = "#ff5722";
                ctx.shadowBlur = 10;
                ctx.fillRect(currentTarget.x, currentTarget.y, 140, 45);
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 18px Arial";
                ctx.fillText(currentTarget.display, currentTarget.x + 10, currentTarget.y + 25);

                ctx.fillStyle = "#e0e0e0";
                ctx.font = "italic 11px Arial";
                ctx.fillText("(" + currentTarget.mean + ")", currentTarget.x + 10, currentTarget.y + 40);
            }}

            // 3. Vẽ Đạn
            ctx.fillStyle = "#00ffff";
            bullets.forEach(b => {{
                ctx.beginPath();
                ctx.arc(b.x, b.y, 6, 0, Math.PI * 2);
                ctx.fill();
            }});

            // 4. Hiệu ứng hạt
            particles.forEach(p => {{
                ctx.save();
                ctx.globalAlpha = p.alpha;
                ctx.fillStyle = p.color;
                ctx.fillRect(p.x, p.y, 4, 4);
                ctx.restore();
            }});

            // 5. Màn hình Game Over
            if (isGameOver) {{
                ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#ff4757";
                ctx.font = "bold 32px Arial";
                ctx.fillText("GAME OVER", 150, 240);

                ctx.fillStyle = "#ffffff";
                ctx.font = "18px Arial";
                ctx.fillText("Từ vựng đã chạm đáy!", 155, 280);
                ctx.fillText("Chọn lại cấp độ ở menu trên và F5 chơi lại!", 80, 320);
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

st.components.v1.html(game_code, height=650)
