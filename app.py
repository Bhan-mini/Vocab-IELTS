import json
import streamlit as st

st.set_page_config(
    page_title="IELTS Vocabulary Shooter Pro", page_icon="🦋", layout="wide"
)

st.title("🦋 Trò Chơi Ôn Luyện Từ Vựng IELTS Đa Năng")
st.write(
    "Lựa chọn cấp độ, chủ đề, kiểu bàn phím yêu thích và giúp chú bướm chinh phục"
    " từ vựng!"
)

# --- BẢNG ĐIỀU KHIỂN TRÊN GIAO DIỆN STREAMLIT ---
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
    f" **{selected_topic}** | Kiểu bàn phím: **{keyboard_layout}**"
)

# Kho từ vựng chi tiết theo cấp độ và chủ đề
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
        {
            "word": "book",
            "display": "boo_",
            "missing": "k",
            "mean": "Sách",
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
        {
            "word": "river",
            "display": "rive_",
            "missing": "r",
            "mean": "Dòng sông",
            "topic": "Environment & Nature",
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
        {
            "word": "climate",
            "display": "climat_",
            "missing": "e",
            "mean": "Khí hậu",
            "topic": "Environment & Nature",
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

# Tốc độ rơi được chỉnh chậm hơn rõ rệt (0.5 đến 0.7)
slow_speed = 0.5 if selected_level in ["C1", "C2"] else 0.45

# Định nghĩa cấu hình bàn phím ảo theo yêu cầu
if keyboard_layout == "Laptop / PC (QWERTY)":
  kb_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
else:
  # Kiểu bàn phím điện thoại tối ưu ngón tay khi cầm dọc
  kb_rows = ["123", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

kb_json = json.dumps(kb_rows)

# --- MÃ NGUỒN GAME HTML/JS ---
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
            max-width: 650px;
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
            padding: 12px 16px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px #282a36;
            min-width: 38px;
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
        <!-- Khung Canvas rộng và lớn hơn -->
        <canvas id="gameCanvas" width="650" height="480"></canvas>
        
        <!-- Bàn phím ảo tương thích -->
        <div class="virtual-keyboard" id="keyboard"></div>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const vocabList = {vocab_json};
        const fallSpeed = {slow_speed};
        const kbRows = {kb_json};

        let score = 0;
        let targets = []; // Cho phép chứa nhiều từ vựng xuất hiện song song
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

        // Tạo từ vựng liên tục theo thời gian (xuất hiện chậm rãi, lần lượt/song song)
        function spawnTarget() {{
            if (vocabList.length === 0) return;
            const randomIndex = Math.floor(Math.random() * vocabList.length);
            const item = vocabList[randomIndex];
            
            // Tránh sinh trùng quá gần vị trí ngang nhau
            let randomX = Math.random() * (canvas.width - 160) + 20;
            
            targets.push({{
                ...item,
                x: randomX,
                y: -50,
                speed: fallSpeed
            }});
        }}

        // Xử lý khi người chơi bấm ký tự
        function handleInput(typedKey) {{
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            if (isGameOver) return;

            typedKey = typedKey.toLowerCase();

            // Tìm từ vựng nào trên màn hình có ký tự thiếu khớp với phím vừa gõ
            for (let i = 0; i < targets.length; i++) {{
                let t = targets[i];
                if (typedKey === t.missing) {{
                    playSound("shoot");
                    // Bắn đạn hướng về từ vựng đó
                    bullets.push({{
                        x: player.x + player.width / 2,
                        y: player.y,
                        targetId: i,
                        targetX: t.x + 65,
                        targetY: t.y + 20,
                        speed: 10
                    }});
                    break; // Bắn từ đầu tiên tìm thấy khớp
                }}
            }}
        }}

        // Bàn phím cứng máy tính
        document.addEventListener("keydown", function(e) {{
            handleInput(e.key);
        }});

        // Khởi tạo bàn phím ảo hiển thị theo layout học sinh chọn
        const keyboardDiv = document.getElementById("keyboard");
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
            // Cứ khoảng 130 khung hình thì sinh thêm 1 từ vựng mới rơi xuống (tạo độ giãn cách chậm rãi, lần lượt)
            if (spawnTimer > 130) {{
                spawnTarget();
                spawnTimer = 0;
            }}

            // Cập nhật vị trí các từ vựng đang rơi
            for (let i = targets.length - 1; i >= 0; i--) {{
                targets[i].y += targets[i].speed;

                // Nếu có từ vựng chạm gần đáy màn hình -> Game Over
                if (targets[i].y > canvas.height - 70) {{
                    isGameOver = true;
                    playSound("gameover");
                }}
            }}

            // Cập nhật đường đạn bay
            for (let i = bullets.length - 1; i >= 0; i--) {{
                let b = bullets[i];
                b.y -= b.speed;

                // Kiểm tra nếu đạn chạm mục tiêu
                let targetObj = targets[b.targetId];
                if (targetObj && b.y <= targetObj.y + 30) {{
                    score += 10;
                    document.getElementById("score-info").innerText = "🏆 Điểm: " + score;
                    playSound("hit");
                    createExplosion(targetObj.x + 65, targetObj.y + 20);
                    
                    // Xóa từ vựng đã bắn trúng khỏi màn hình
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

            // 1. Vẽ Chú bướm nhân vật
            ctx.fillStyle = "#ff69b4";
            ctx.beginPath();
            ctx.arc(player.x + 25, player.y + 25, 20, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = "#000";
            ctx.font = "26px Arial";
            ctx.fillText("🦋", player.x + 8, player.y + 35);

            // 2. Vẽ tất cả các từ vựng đang rơi trên màn hình
            targets.forEach(t => {{
                ctx.fillStyle = "#ff9800";
                ctx.shadowColor = "#ff5722";
                ctx.shadowBlur = 10;
                ctx.fillRect(t.x, t.y, 140, 45);
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 18px Arial";
                ctx.fillText(t.display, t.x + 10, t.y + 25);

                ctx.fillStyle = "#e0e0e0";
                ctx.font = "italic 11px Arial";
                ctx.fillText("(" + t.mean + ")", t.x + 10, t.y + 40);
            }});

            // 3. Vẽ Đạn
            ctx.fillStyle = "#00ffff";
            bullets.forEach(b => {{
                ctx.beginPath();
                ctx.arc(b.x, b.y, 6, 0, Math.PI * 2);
                ctx.fill();
            }});

            // 4. Hiệu ứng hạt nổ
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
                ctx.fillText("GAME OVER", canvas.width / 2 - 90, 200);

                ctx.fillStyle = "#ffffff";
                ctx.font = "18px Arial";
                ctx.fillText("Có từ vựng đã chạm đáy màn hình!", canvas.width / 2 - 145, 240);
                ctx.fillText("Tải lại trang để thử lại vòng chơi mới nhé!", canvas.width / 2 - 160, 280);
            }}
        }}

        function loop() {{
            update();
            draw();
            requestAnimationFrame(loop);
        }}

        // Khởi tạo ngay từ đầu một từ vựng
        spawnTarget();
        loop();
    </script>
</body>
</html>
"""

st.components.v1.html(game_code, height=600)
