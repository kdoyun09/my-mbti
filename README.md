# my-mbti
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MBTI로 포켓몬 찾기 ⚡</title>
    <style>
        :root {
            --cover-bg: #FFE542;
            --cover-dot: #EBCB10;
            --main-yellow: #FFC700;
            --text-dark: #222222;
            --notebook-border: #332A15;
            --paper-bg: #FFFDF5;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: #0F141C;
            background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 0);
            background-size: 24px 24px;
            color: var(--text-dark);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 24px 12px;
        }

        .outer-frame {
            position: relative;
            width: 100%;
            max-width: 650px;
            border: 2px solid #C19932;
            border-radius: 20px;
            padding: 12px;
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6), 0 0 15px rgba(203, 161, 53, 0.3);
            background: #19202E;
        }

        .notebook {
            position: relative;
            background-color: var(--cover-bg);
            background-image: radial-gradient(var(--cover-dot) 18%, transparent 19%);
            background-size: 18px 18px;
            border-radius: 18px;
            border: 3px solid var(--notebook-border);
            padding: 32px 24px 32px 48px;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.05), 0 8px 20px rgba(0,0,0,0.2);
            overflow: hidden;
        }

        .spiral-spine {
            position: absolute;
            left: 10px;
            top: 30px;
            bottom: 30px;
            width: 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            z-index: 10;
        }

        .spiral-ring {
            width: 24px;
            height: 12px;
            background: linear-gradient(180deg, #E0E0E0 0%, #888888 50%, #444444 100%);
            border-radius: 6px;
            box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
            border: 1px solid #222;
        }

        .title-container {
            text-align: center;
            margin-bottom: 24px;
        }

        .main-title {
            font-size: 2.8rem;
            font-weight: 900;
            color: #111111;
            text-shadow: 
                -2px -2px 0 #FFF, 2px -2px 0 #FFF, -2px 2px 0 #FFF, 2px 2px 0 #FFF,
                3px 3px 0px rgba(0, 0, 0, 0.15);
            letter-spacing: -1px;
            line-height: 1.2;
            word-break: keep-all;
        }

        .sub-title-badge {
            display: inline-block;
            background-color: #222222;
            color: #FFE542;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 6px 16px;
            border-radius: 20px;
            margin-top: 8px;
            box-shadow: 2px 2px 0px rgba(0,0,0,0.15);
        }

        .mbti-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-top: 16px;
        }

        @media (max-width: 480px) {
            .mbti-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
            }
            .main-title { font-size: 2.2rem; }
        }

        .mbti-btn {
            background-color: #FFF;
            border: 2.5px solid var(--notebook-border);
            border-radius: 12px;
            padding: 16px 8px;
            font-size: 1.2rem;
            font-weight: 900;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.15s ease;
            box-shadow: 3px 3px 0px var(--notebook-border);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .mbti-btn:nth-child(4n+1) { background-color: #FFF3CC; }
        .mbti-btn:nth-child(4n+2) { background-color: #E2F5FF; }
        .mbti-btn:nth-child(4n+3) { background-color: #FFE2E2; }
        .mbti-btn:nth-child(4n+4) { background-color: #E3FFE2; }

        .mbti-btn:hover {
            transform: translateY(-3px) scale(1.03);
            box-shadow: 4px 6px 0px var(--notebook-border);
            z-index: 2;
        }

        .mbti-btn:active {
            transform: translateY(1px) scale(0.98);
            box-shadow: 1px 1px 0px var(--notebook-border);
        }

        .result-box {
            animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes popIn {
            from { opacity: 0; transform: scale(0.9) translateY(10px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .polaroid-frame {
            background-color: #FFFFFF;
            border: 3px solid var(--notebook-border);
            border-radius: 16px;
            padding: 20px 16px;
            box-shadow: 4px 6px 0px rgba(0,0,0,0.12);
            text-align: center;
            position: relative;
            margin-bottom: 16px;
        }

        .pokemon-img-wrapper {
            width: 220px;
            height: 220px;
            margin: 8px auto 12px auto;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent;
        }

        .pokemon-img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            filter: drop-shadow(2px 6px 10px rgba(0, 0, 0, 0.2));
            transition: transform 0.3s ease;
        }

        .pokemon-img:hover {
            transform: scale(1.08) rotate(2deg);
        }

        .pokemon-name-title {
            font-size: 2rem;
            font-weight: 900;
            color: #111;
            letter-spacing: -0.5px;
        }

        .reason-paper {
            background-color: var(--paper-bg);
            border: 2.5px solid var(--notebook-border);
            border-radius: 12px;
            padding: 18px 20px;
            text-align: left;
            font-size: 1.05rem;
            line-height: 1.7;
            color: #222;
            box-shadow: 3px 3px 0px rgba(0,0,0,0.08);
            margin-bottom: 16px;
            background-image: repeating-linear-gradient(var(--paper-bg), var(--paper-bg) 27px, #E5DFC8 28px);
            word-break: keep-all;
        }

        .match-badge-box {
            background-color: #FFF0F5;
            border: 2.5px solid #FFB6C1;
            border-radius: 12px;
            padding: 14px 18px;
            display: flex;
            align-items: center;
            gap: 12px;
            text-align: left;
            margin-bottom: 20px;
        }

        .match-badge-box .heart-icon {
            font-size: 2.4rem;
        }

        .match-text h4 {
            font-size: 0.9rem;
            color: #D81B60;
            font-weight: 800;
        }

        .match-text p {
            font-size: 1.02rem;
            font-weight: 700;
            color: #222;
            margin-top: 2px;
        }

        .bottom-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 8px;
        }

        .retry-btn {
            background: linear-gradient(135deg, #FF5252, #FF1744);
            color: #FFFFFF;
            border: 2.5px solid var(--notebook-border);
            border-radius: 30px;
            padding: 14px 36px;
            font-size: 1.15rem;
            font-weight: 900;
            cursor: pointer;
            box-shadow: 3px 4px 0px var(--notebook-border);
            transition: all 0.15s ease;
        }

        .retry-btn:hover {
            transform: translateY(-2px);
            box-shadow: 4px 6px 0px var(--notebook-border);
            background: linear-gradient(135deg, #FF1744, #D50000);
        }

        .retry-btn:active {
            transform: translateY(1px);
            box-shadow: 1px 1px 0px var(--notebook-border);
        }

        .hidden { display: none !important; }
    </style>
</head>
<body>

    <div class="outer-frame">
        <div class="notebook">
            
            <!-- Left Binder Spiral Rings -->
            <div class="spiral-spine">
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
                <div class="spiral-ring"></div>
            </div>

            <!-- Header Section -->
            <div class="title-container">
                <div class="main-title">
                    MBTI로 포켓몬 찾기 ⚡
                </div>
                <div class="sub-title-badge">
                    자신의 MBTI를 누르면 어울리는 포켓몬이 나타나요!
                </div>
            </div>

            <!-- MBTI Selection View -->
            <div id="selection-card">
                <div class="mbti-grid" id="mbti-grid">
                    <!-- JS generated buttons -->
                </div>
            </div>

            <!-- Result Display View -->
            <div id="result-card" class="result-box hidden">
                <div class="polaroid-frame">
                    <div style="font-size: 1rem; font-weight: 800; color: #007AFF; margin-bottom: 8px;" id="result-mbti-badge">
                        [ INTJ 유형 ]
                    </div>
                    
                    <div class="pokemon-img-wrapper">
                        <img id="pokemon-img" class="pokemon-img" src="" alt="포켓몬 이미지">
                    </div>

                    <h2 class="pokemon-name-title" id="pokemon-name">뮤츠</h2>
                </div>

                <div class="reason-paper">
                    <p id="pokemon-reason">어울리는 이유 설명이 나타납니다.</p>
                </div>

                <div class="match-badge-box">
                    <div class="heart-icon">💖</div>
                    <div class="match-text">
                        <h4>최고의 찰떡 궁합 MBTI</h4>
                        <p id="pokemon-match">ENTP (팬텀 👻)</p>
                    </div>
                </div>

                <div class="bottom-bar">
                    <button class="retry-btn" onclick="resetSelection()">🔄 다시 고르기</button>
                </div>
            </div>

        </div>
    </div>

    <script>
        const pokemonData = {
            "ISTJ": {
                id: 9,
                name: "거북왕 🐢💦",
                reason: "신중하고 책임감이 강하여 어떤 시련이 와도 묵묵히 자리를 지킵니다. 철저한 계획성으로 주변 사람들에게 깊은 신뢰감을 주는 든든한 등껍질 같은 존재예요!",
                match: "ESFP (푸린 🎤)",
                matchDesc: "자유롭고 쾌활한 ESFP가 당신의 견고한 일상에 기분 좋은 활력을 선물해 줍니다."
            },
            "ISFJ": {
                id: 113,
                name: "럭키 💖🩺",
                reason: "온화하고 헌신적인 성품으로 주변 사람들을 살뜰히 챙깁니다. 상대방의 작은 변화도 금방 알아차리고 따뜻한 마음으로 모두를 치유해 주는 천사 같아요!",
                match: "ESTP (라이츄 ⚡)",
                matchDesc: "모험심 강하고 화끈한 ESTP가 당신의 따뜻한 보살핌 속에서 최고의 시너지를 발휘합니다."
            },
            "INFJ": {
                id: 282,
                name: "가디안 🔮✨",
                reason: "깊은 통찰력과 따뜻한 공감 능력을 갖추고 있습니다. 자신이 믿는 사람이나 이상을 위해서라면 어떠한 위험도 무릅쓰고 끝까지 지켜내는 숭고한 마음을 가졌어요.",
                match: "ENFP (피카츄 ⚡)",
                matchDesc: "통통 튀는 ENFP의 순수한 열정이 당신의 깊은 내면세계를 밝고 환하게 열어줍니다."
            },
            "INTJ": {
                id: 150,
                name: "뮤츠 🧠🌌",
                reason: "독창적이고 뛰어난 전략가 타입으로 자신만의 길을 개척합니다. 명확한 비전과 분석력으로 사물의 본질을 단번에 파악하는 압도적인 지혜를 가지고 있어요!",
                match: "ENTP (팬텀 👻)",
                matchDesc: "호기심 많은 ENTP와의 지적인 대화는 서로에게 끊임없는 영감과 즐거움을 줍니다."
            },
            "ISTP": {
                id: 4,
                name: "파이리 🔥🦎",
                reason: "조용하지만 필요할 때 엄청난 집중력과 순발력을 발휘합니다. 손재주가 좋고 도구를 잘 다루며, 상황을 냉철하게 분석하여 깔끔하게 해결해내는 능력이 뛰어납니다.",
                match: "ESFJ (치코리타 🍃)",
                matchDesc: "친절하고 다정한 ESFJ가 당신의 무심한 듯 따뜻한 마음을 가장 잘 이해해 줍니다."
            },
            "ISFP": {
                id: 132,
                name: "메타몽 🎨🫠",
                reason: "유연하고 온화하며 어디든 맞춰줄 수 있는 넓은 포용력을 자랑합니다. 예술적인 감각이 뛰어나고 자신만의 유유자적한 라이프스타일을 소중히 여겨요.",
                match: "ENTJ (자시안 ⚔️)",
                matchDesc: "확고한 방향성을 제시하는 ENTJ 덕분에 당신의 풍부한 잠재력이 유감없이 발휘됩니다."
            },
            "INFP": {
                id: 133,
                name: "이브이 🌟🦊",
                reason: "풍부한 감수성과 무한한 가능성을 가슴속에 품고 있습니다. 따뜻한 마음씨와 유연한 상상력으로 어떤 모습으로든 아름답게 성장할 수 있는 원석 같은 존재입니다.",
                match: "ENFJ (망나뇽 🐉)",
                matchDesc: "따뜻하고 리더십 있는 ENFJ가 당신의 가치관과 꿈을 열렬히 응원하고 지켜줍니다."
            },
            "INTP": {
                id: 143,
                name: "잠만보 😴💤",
                reason: "느긋해 보이지만 두뇌 회전이 매우 빠르고 호기심이 많습니다. 관심 있는 분야에 빠지면 집중적으로 탐구하며, 고요한 평정심을 유지하는 매력이 있어요.",
                match: "ENTJ (자시안 ⚔️)",
                matchDesc: "추진력 넘치는 ENTJ가 당신의 탁월한 아이디어를 현실로 구현할 수 있도록 이끌어 줍니다."
            },
            "ESTP": {
                id: 26,
                name: "라이츄 ⚡🐭",
                reason: "에너지 넘치고 자극과 모험을 두려워하지 않는 행동파입니다! 스릴을 즐기며 당면한 문제를 즉각적인 대처 능력으로 시원하게 해결하는 솔직담백한 능력자예요.",
                match: "ISFJ (럭키 💖)",
                matchDesc: "세심한 ISFJ가 당신의 거침없는 도전을 안정적으로 뒷받침해 주는 최고의 든든한 편입니다."
            },
            "ESFP": {
                id: 39,
                name: "푸린 🎤🎶",
                reason: "어디서나 스포트라이트를 받는 매력적인 분위기 메이커입니다! 넘치는 흥과 친화력으로 사람들을 즐겁게 하며 사랑스러운 에너지를 온 동네에 퍼뜨립니다.",
                match: "ISTJ (거북왕 🐢)",
                matchDesc: "차분하고 진중한 ISTJ가 당신이 마음껏 재능을 펼칠 수 있는 안전한 울타리가 되어줍니다."
            },
            "ENFP": {
                id: 25,
                name: "피카츄 ⚡️",
                reason: "밝고 긍정적인 에너지로 언제나 주변을 환하게 밝힙니다! 창의적인 아이디어가 샘솟고 열정적이며, 누구와도 금방 친해지는 분위기 메이커 포켓몬입니다.",
                match: "INFJ (가디안 🔮)",
                matchDesc: "깊이감 있는 INFJ는 당신의 빛나는 아이디어들을 진심으로 귀담아들어 줍니다."
            },
            "ENTP": {
                id: 94,
                name: "팬텀 👻🎃",
                reason: "재치 있고 장난기 넘치며 독창적인 고정관념 파괴자입니다! 독특한 시각과 유쾌한 입담으로 지루할 틈이 없는 흥미진진한 일상을 만들어갑니다.",
                match: "INTJ (뮤츠 🧬)",
                matchDesc: "지적인 INTJ와의 논쟁과 대화는 당신의 호기심을 가장 완벽하게 충족시켜 줍니다."
            },
            "ESTJ": {
                id: 59,
                name: "윈디 🦁🔥",
                reason: "체계적이고 리더십이 뛰어나 무리를 당당하게 이끕니다. 강한 책임감과 위풍당당한 추진력으로 설정한 목표를 향해 흔들림 없이 직진하는 단단한 리더예요!",
                match: "INTP (잠만보 😴)",
                matchDesc: "창의적인 INTP의 아이디어와 당신의 강력한 실행력이 만나면 못 이룰 것이 없습니다."
            },
            "ESFJ": {
                id: 152,
                name: "치코리타 🍃🌸",
                reason: "사교성이 풍부하고 타인에 대한 애정과 배려가 넘쳐납니다. 주변 분위기를 늘 화기애애하게 만들며 함께하는 사람들에게 상쾌한 힐링을 주는 존재입니다.",
                match: "ISTP (파이리 🔥)",
                matchDesc: "솔직하고 담백한 ISTP와의 만남은 당신에게 색다른 편안함과 재미를 선사합니다."
            },
            "ENFJ": {
                id: 149,
                name: "망나뇽 🐉🧡",
                reason: "크고 따뜻한 마음으로 주변 사람들을 품어주는 유능한 조력자입니다. 카리스마와 친절함을 동시에 갖추어 모두를 올바른 방향으로 이끄는 따뜻한 리더십을 발휘해요.",
                match: "INFP (이브이 🦊)",
                matchDesc: "순수하고 풍부한 감성의 INFP를 지켜주고 끌어주며 깊은 유대감을 형성합니다."
            },
            "ENTJ": {
                id: 888,
                name: "자시안 ⚔️👑",
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

            document.getElementById('result-mbti-badge').innerText = `[ ${mbti} 유형 ]`;
            document.getElementById('pokemon-name').innerText = data.name;
            
            // Fast & reliable global CDN for PokeAPI official artwork
            const imgUrl = `https://cdn.jsdelivr.net/gh/PokeAPI/sprites@master/sprites/pokemon/other/official-artwork/${data.id}.png`;
            document.getElementById('pokemon-img').src = imgUrl;

            document.getElementById('pokemon-reason').innerHTML = `
                <strong>${mbti}</strong> 유형의 당신은...<br><br>${data.reason}
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
