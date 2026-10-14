# my-mbti
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MBTI로 나와 닮은 포켓몬 찾기 ⚡</title>
    <style>
        :root {
            --bg-main: #FFFDF0;
            --bg-card: #FFFFFF;
            --accent-yellow: #FFDE00;
            --accent-warm: #FF9A3C;
            --text-main: #4A3E3D;
            --text-sub: #7A6865;
            --border-color: #FFE699;
            --shadow: 0 8px 24px rgba(230, 180, 80, 0.18);
            --radius-lg: 24px;
            --radius-sm: 16px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px 16px;
        }

        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
        }

        .card {
            background: var(--bg-card);
            border: 3px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 32px 24px;
            box-shadow: var(--shadow);
            text-align: center;
            transition: all 0.3s ease;
        }

        header h1 {
            font-size: 1.8rem;
            color: var(--text-main);
            margin-bottom: 8px;
            font-weight: 800;
            word-break: keep-all;
        }

        header p {
            font-size: 1.05rem;
            color: var(--text-sub);
            margin-bottom: 28px;
            word-break: keep-all;
        }

        .mbti-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }

        @media (max-width: 480px) {
            .mbti-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
            }
        }

        .mbti-btn {
            background-color: #FFF9E6;
            border: 2px solid var(--border-color);
            border-radius: var(--radius-sm);
            padding: 18px 8px;
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--text-main);
            cursor: pointer;
            transition: transform 0.15s ease, background-color 0.2s ease, box-shadow 0.2s ease;
            outline: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .mbti-btn:hover {
            background-color: var(--accent-yellow);
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(255, 200, 0, 0.35);
        }

        .mbti-btn:active {
            transform: translateY(0);
        }

        .hidden {
            display: none !important;
        }

        .result-container {
            animation: fadeIn 0.4s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .badge {
            display: inline-block;
            background-color: #FFEBB3;
            color: var(--text-main);
            padding: 8px 18px;
            border-radius: 20px;
            font-weight: 800;
            font-size: 1.05rem;
            margin-bottom: 12px;
        }

        .pokemon-emoji {
            font-size: 6rem;
            line-height: 1.2;
            margin: 16px 0;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
            animation: bounce 1.2s infinite alternate ease-in-out;
        }

        @keyframes bounce {
            from { transform: translateY(0); }
            to { transform: translateY(-8px); }
        }

        .pokemon-name {
            font-size: 2rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 20px;
        }

        .reason-box {
            background-color: #FFFDF0;
            border: 2px dashed var(--border-color);
            border-radius: var(--radius-sm);
            padding: 20px;
            text-align: left;
            margin-bottom: 20px;
            line-height: 1.6;
            font-size: 1.05rem;
            word-break: keep-all;
        }

        .reason-box strong {
            color: var(--accent-warm);
        }

        .match-box {
            background-color: #FFF3E0;
            border-radius: var(--radius-sm);
            padding: 16px;
            margin-bottom: 28px;
            text-align: left;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .match-icon {
            font-size: 2rem;
        }

        .match-info h4 {
            font-size: 0.95rem;
            color: var(--accent-warm);
            margin-bottom: 2px;
        }

        .match-info p {
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-main);
        }

        .retry-btn {
            background: linear-gradient(135deg, var(--accent-yellow), var(--accent-warm));
            color: #FFFFFF;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
            border: none;
            border-radius: 30px;
            padding: 16px 36px;
            font-size: 1.15rem;
            font-weight: 800;
            cursor: pointer;
            width: 100%;
            transition: opacity 0.2s, transform 0.1s;
            box-shadow: 0 4px 14px rgba(255, 154, 60, 0.4);
        }

        .retry-btn:hover {
            opacity: 0.95;
            transform: scale(1.02);
        }

        .retry-btn:active {
            transform: scale(0.98);
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- 선택 카드 화면 -->
        <div id="selection-card" class="card">
            <header>
                <h1>⚡ MBTI로 포켓몬 찾기 🍃</h1>
                <p>나의 MBTI 유형을 선택하고, 나와 찰떡궁합인 포켓몬을 확인해보세요!</p>
            </header>

            <div class="mbti-grid" id="mbti-grid">
                <!-- 자바스크립트로 버튼 생성 -->
            </div>
        </div>

        <!-- 결과 표시 카드 화면 -->
        <div id="result-card" class="card result-container hidden">
            <div id="user-mbti-badge" class="badge">INTJ</div>
            <div id="pokemon-emoji" class="pokemon-emoji">🔮</div>
            <h2 id="pokemon-name" class="pokemon-name">뮤츠</h2>

            <div class="reason-box">
                <p id="pokemon-reason">어울리는 이유 설명이 들어갑니다.</p>
            </div>

            <div class="match-box">
                <div class="match-icon">💖</div>
                <div class="match-info">
                    <h4>잘 맞는 찰떡 궁합 유형</h4>
                    <p id="pokemon-match">ENFP (피카츄 ⚡)</p>
                </div>
            </div>

            <button class="retry-btn" onclick="resetSelection()">🔄 다시 고르기</button>
        </div>
    </div>

    <script>
        const pokemonData = {
            "ISTJ": {
                name: "거북왕 🐢💦",
                emoji: "🐢",
                reason: "신중하고 책임감이 강하여 어떤 시련이 와도 묵묵히 자리를 지킵니다. 철저한 계획성으로 주변 친구들에게 깊은 신뢰감을 주는 든든한 등껍질 같은 존재예요!",
                match: "ESFP (푸린 🎤)",
                matchDesc: "자유롭고 쾌활한 ESFP가 당신의 견고한 일상에 기분 좋은 활력을 선물해 줍니다."
            },
            "ISFJ": {
                name: "럭키 💖🩺",
                emoji: "💖",
                reason: "온화하고 헌신적인 성품으로 주변 사람들을 살뜰히 챙깁니다. 상대방의 작은 변화도 금방 알아차리고 따뜻한 해피 알로 마음을 치유해 주는 천사 같아요!",
                match: "ESTP (라이츄 ⚡)",
                matchDesc: "모험심 강하고 화끈한 ESTP가 당신의 따뜻한 보살핌 속에서 최고의 시너지를 발휘합니다."
            },
            "INFJ": {
                name: "가디안 🔮✨",
                emoji: "🔮",
                reason: "깊은 통찰력과 따뜻한 공감 능력을 갖추고 있습니다. 자신이 믿는 사람이나 이상을 위해서라면 어떠한 위험도 무릅쓰고 끝까지 지켜내는 숭고한 마음을 가졌어요.",
                match: "ENFP (피카츄 ⚡)",
                matchDesc: "통통 튀는 ENFP의 순수한 열정이 당신의 깊은 내면세계를 밝고 환하게 열어줍니다."
            },
            "INTJ": {
                name: "뮤츠 🧠🌌",
                emoji: "🧬",
                reason: "독창적이고 뛰어난 전략가 타입으로 독자적인 길을 개척합니다. 명확한 비전과 분석력으로 사물의 본질을 단번에 파악하는 압도적인 지혜를 가지고 있어요!",
                match: "ENTP (팬텀 👻)",
                matchDesc: "호기심 많은 ENTP와의 지적인 대화는 서로에게 끊임없는 영감과 즐거움을 줍니다."
            },
            "ISTP": {
                name: "파이리 🔥🦎",
                emoji: "🔥",
                reason: "조용하지만 필요할 때 엄청난 집중력과 순발력을 발휘합니다. 손재주가 좋고 도구를 잘 다루며, 상황을 냉철하게 분석하여 깔끔하게 해결해냅니다.",
                match: "ESFJ (치코리타 🍃)",
                matchDesc: "친절하고 다정한 ESFJ가 당신의 무심한 듯 따뜻한 마음을 가장 잘 이해해 줍니다."
            },
            "ISFP": {
                name: "메타몽 🎨🫠",
                emoji: "🫠",
                reason: "유연하고 온화하며 어디든 맞춰줄 수 있는 넓은 포용력을 자랑합니다. 예술적인 감각이 뛰어나고 자신만의 유유자적한 라이프스타일을 소중히 여겨요.",
                match: "ENTJ (자시안 ⚔️)",
                matchDesc: "확고한 방향성을 제시하는 ENTJ 덕분에 당신의 풍부한 잠재력이 유감없이 발휘됩니다."
            },
            "INFP": {
                name: "이브이 🌟🦊",
                emoji: "🦊",
                reason: "풍부한 감수성과 무한한 가능성을 가슴속에 품고 있습니다. 따뜻한 마음씨와 유연한 상상력으로 어떤 모습으로든 아름답게 성장할 수 있는 원석 같은 존재입니다.",
                match: "ENFJ (망나뇽 🐉)",
                matchDesc: "따뜻하고 리더십 있는 ENFJ가 당신의 가치관과 꿈을 열렬히 응원하고 지켜줍니다."
            },
            "INTP": {
                name: "잠만보 😴💤",
                emoji: "😴",
                reason: "느긋해 보이지만 두뇌 회전이 매우 빠르고 호기심이 많습니다. 관심 있는 분야에 빠지면 밤을 새워 탐구하며, 고요한 평정심을 유지하는 매력이 있어요.",
                match: "ENTJ (자시안 ⚔️)",
                matchDesc: "추진력 넘치는 ENTJ가 당신의 탁월한 아이디어를 현실로 구현할 수 있도록 이끌어 줍니다."
            },
            "ESTP": {
                name: "라이츄 ⚡🐭",
                emoji: "⚡",
                reason: "에너지 넘치고 자극과 모험을 두려워하지 않는 행동파입니다! 스릴을 즐기며 당면한 문제를 즉각적인 대처 능력으로 시원하게 해결하는 능력자예요.",
                match: "ISFJ (럭키 💖)",
                matchDesc: "세심한 ISFJ가 당신의 거침없는 도전을 안정적으로 뒷받침해 주는 최고의 든든한 편입니다."
            },
            "ESFP": {
                name: "푸린 🎤🎶",
                emoji: "🎤",
                reason: "어디서나 스포트라이트를 받는 매력적인 분위기 메이커입니다! 넘치는 흥과 친화력으로 사람들을 즐겁게 하며 사랑스러운 에너지를 온 동네에 퍼뜨립니다.",
                match: "ISTJ (거북왕 🐢)",
                matchDesc: "차분하고 진중한 ISTJ가 당신이 마음껏 재능을 펼칠 수 있는 안전한 울타리가 되어줍니다."
            },
            "ENFP": {
                name: "피카츄 ⚡️",
                emoji: "⚡",
                reason: "밝고 긍정적인 에너지로 언제나 주변을 환하게 밝힙니다! 창의적인 아이디어가 샘솟고 열정적이며, 누구와도 금방 친해지는 인싸 중의 인싸 포켓몬입니다.",
                match: "INFJ (가디안 🔮)",
                matchDesc: "깊이감 있는 INFJ는 당신의 빛나는 아이디어들을 진심으로 귀담아들어 줍니다."
            },
            "ENTP": {
                name: "팬텀 👻🎃",
                emoji: "👻",
                reason: "재치 있고 장난기 넘치며 독창적인 고정관념 파괴자입니다! 재치 있는 입담과 독특한 시각으로 지루할 틈이 없는 유쾌한 대화를 이끌어 나갑니다.",
                match: "INTJ (뮤츠 🧬)",
                matchDesc: "지적인 INTJ와의 논쟁과 대화는 당신의 호기심을 가장 완벽하게 충족시켜 줍니다."
            },
            "ESTJ": {
                name: "윈디 🦁🔥",
                emoji: "🦁",
                reason: "체계적이고 리더십이 뛰어나 무리를 당당하게 이끕니다. 강한 책임감과 위풍당당한 추진력으로 설정한 목표를 향해 흔들림 없이 직진하는 리더예요!",
                match: "INTP (잠만보 😴)",
                matchDesc: "창의적인 INTP의 아이디어와 당신의 강력한 실행력이 만나면 못 이룰 것이 없습니다."
            },
            "ESFJ": {
                name: "치코리타 🍃🌸",
                emoji: "🍃",
                reason: "사교성이 풍부하고 타인에 대한 애정과 배려가 넘쳐납니다. 주변 분위기를 늘 화기애애하게 만들며 함께하는 사람들에게 상쾌한 힐링을 주는 존재입니다.",
                match: "ISTP (파이리 🔥)",
                matchDesc: "솔직하고 담백한 ISTP와의 만남은 당신에게 색다른 편안함과 재미를 선사합니다."
            },
            "ENFJ": {
                name: "망나뇽 🐉🧡",
                emoji: "🐉",
                reason: "크고 따뜻한 마음으로 주변 사람들을 품어주는 유능한 조력자입니다. 카리스마와 친절함을 동시에 갖추어 모두를 올바른 방향으로 이끄는 리더십을 발휘해요.",
                match: "INFP (이브이 🦊)",
                matchDesc: "순수하고 풍부한 감성의 INFP를 지켜주고 끌어주며 깊은 유대감을 형성합니다."
            },
            "ENTJ": {
                name: "자시안 ⚔️👑",
                emoji: "⚔️",
                reason: "단호한 결단력과 높은 목표 의식을 바탕으로 승리를 이끌어내는 당당한 개척자입니다. 지치지 않는 열정과 효율적인 전략으로 언제나 최고를 향해 나아갑니다.",
                match: "INTP (잠만보 😴)",
                matchDesc: "당신의 완벽한 실행력에 INTP의 깊이 있는 원리 분석이 더해지면 무적의 팀이 됩니다."
            }
        };

        const mbtiList = [
            "INTJ", "INTP", "ENTJ", "ENTP",
            "INFJ", "INFP", "ENFJ", "ENFP",
            "ISTJ", "ISFJ", "ESTJ", "ESFJ",
            "ISTP", "ISFP", "ESTP", "ESFP"
        ];

        function renderMbtiButtons() {
            const grid = document.getElementById('mbti-grid');
            grid.innerHTML = '';

            mbtiList.forEach(mbti => {
                const btn = document.createElement('button');
                btn.className = 'mbti-btn';
                btn.onclick = () => selectMBTI(mbti);
                btn.innerHTML = `<span>${mbti}</span>`;
                grid.appendChild(btn);
            });
        }

        function selectMBTI(mbti) {
            const data = pokemonData[mbti];
            if (!data) return;

            document.getElementById('user-mbti-badge').innerText = `내 MBTI: ${mbti}`;
            document.getElementById('pokemon-emoji').innerText = data.emoji;
            document.getElementById('pokemon-name').innerText = data.name;
            
            document.getElementById('pokemon-reason').innerHTML = `
                <strong>${mbti}</strong> 유형인 당신은...<br><br>${data.reason}
            `;
            
            document.getElementById('pokemon-match').innerText = `${data.match} - ${data.matchDesc}`;

            document.getElementById('selection-card').classList.add('hidden');
            document.getElementById('result-card').classList.remove('hidden');

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function resetSelection() {
            document.getElementById('result-card').classList.add('hidden');
            document.getElementById('selection-card').classList.remove('hidden');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.onload = function() {
            renderMbtiButtons();
        };
    </script>
</body>
</html>
