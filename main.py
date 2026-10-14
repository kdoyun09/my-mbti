import streamlit as st

# 1. 페이지 기본 설정 (타이틀, 레이아웃)
st.set_page_config(
    page_title="MBTI x 포켓몬 단짝 찾기",
    page_icon="⚡",
    layout="centered"
)

# 2. 크림 & 노란색 톤 커스텀 CSS 디자인
st.markdown("""
<style>
    /* 전체 배경 및 기본 폰트 설정 */
    .stApp {
        background-color: #FFFDF5;
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 제목 및 서브 타이틀 스타일 */
    .main-title {
        color: #D97706;
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        color: #78350F;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* 포켓몬 정보 카드 스타일 */
    .pokemon-card {
        background-color: #FEF3C7;
        border: 3px solid #F59E0B;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        margin-top: 15px;
    }
    
    /* 포켓몬 이름 */
    .pokemon-name {
        color: #B45309;
        font-size: 1.8rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 8px;
    }

    /* 포켓몬 타입 태그 */
    .type-badge {
        display: inline-block;
        background-color: #F59E0B;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.9rem;
        font-weight: bold;
        margin-bottom: 12px;
    }

    /* 특징 & 이유 본문 */
    .info-text {
        color: #451A03;
        font-size: 1.05rem;
        line-height: 1.6;
        word-break: keep-all;
    }
    
    .label-text {
        font-weight: bold;
        color: #B45309;
    }
</style>
""", unsafe_allow_html=True)

# 3. 16가지 MBTI 포켓몬 데이터베이스
POKEMON_DATA = {
    "ISTJ": {
        "ko_name": "거북왕",
        "en_name": "Blastoise",
        "type": "물 💧",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "feature": "묵묵히 책임을 다하며 어떤 상황에서도 쉽게 흔들리지 않는 신뢰의 대표주자.",
        "reason": "ISTJ의 원칙주의적이고 침착한 성향이 단단한 껍질로 팀을 지키는 거북왕과 완벽히 닮았습니다. 무슨 일이 있어도 신뢰를 저버리지 않는 최고의 단짝입니다."
    },
    "ISFJ": {
        "ko_name": "해피너스",
        "en_name": "Blissey",
        "type": "노멀 🥚",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "feature": "주변 사람들의 상처와 마음을 세심하게 챙겨주는 따뜻한 수호자.",
        "reason": "타인을 진심으로 배려하고 온기를 전하는 ISFJ의 따뜻함은 알을 나눠주며 행복을 주는 해피너스와 판박이입니다."
    },
    "INFJ": {
        "ko_name": "가디안",
        "en_name": "Gardevoir",
        "type": "에스퍼/페어리 ✨",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "feature": "깊은 통찰력과 이상적인 가치를 품고 트레이너를 묵묵히 지키는 충직함.",
        "reason": "INFJ 특유의 깊은 공감 능력과 헌신적인 태도는 미래를 내다보고 트레이너를 끝까지 보호하는 가디안과 꼭 맞습니다."
    },
    "INTJ": {
        "ko_name": "뮤츠",
        "en_name": "Mewtwo",
        "type": "에스퍼 🔮",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "feature": "독립적이고 치밀한 분석력을 가졌으며 늘 더 높은 철학적 비전을 탐구함.",
        "reason": "남들에게 의존하지 않고 스스로의 뛰어난 지능과 전략으로 결론을 도출하는 INTJ에게 뮤츠는 최고의 지적 동반자입니다."
    },
    "ISTP": {
        "ko_name": "루카리오",
        "en_name": "Lucario",
        "type": "격투/강철 🥊",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "feature": "상황 파악이 빠르고 도구를 자유자재로 다루는 냉철한 해결사.",
        "reason": "말보다 행동으로 실력을 증명하며 냉철하게 핵심을 파악하는 ISTP는 파동을 읽고 정밀하게 대처하는 루카리오와 가장 잘 어울립니다."
    },
    "ISFP": {
        "ko_name": "메타몽",
        "en_name": "Ditto",
        "type": "노멀 🫠",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "feature": "어디에나 유연하게 맞춰가는 예술가적 감성과 수용력.",
        "reason": "자유로운 영혼이자 상황에 맞춰 부드럽게 자신을 변화시킬 줄 아는 ISFP의 유연함은 어떤 모습으로든 변신할 수 있는 메타몽을 연상시킵니다."
    },
    "INFP": {
        "ko_name": "이브이",
        "en_name": "Eevee",
        "type": "노멀 🦊",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "feature": "무한한 가능성과 다정하고 무궁무진한 꿈을 품은 마음.",
        "reason": "어떤 모습으로든 진화할 수 있는 잠재력과 상상력을 가진 이브이는 내면의 가능성을 끊임없이 피워내는 INFP의 본모습입니다."
    },
    "INTP": {
        "ko_name": "후딘",
        "en_name": "Alakazam",
        "type": "에스퍼 🧠",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "feature": "아이디어가 샘솟고 논리적 탐구를 끝없이 즐기는 원조 지식인.",
        "reason": "IQ 5000을 자랑하며 지적 호기심을 지탱하는 후딘의 거대한 뇌는 끊임없이 사고하고 논리적 체계를 세우는 INTP와 정체성을 공유합니다."
    },
    "ESTP": {
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "type": "전기 ⚡",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "feature": "에너지가 넘치고 순발력 있게 행동으로 돌진하는 모험가.",
        "reason": "지루한 것을 못 참아하고 순간의 스릴과 에너지를 즐기는 ESTP의 행동력은 매 순간 찌릿찌릿한 활력을 뿜어내는 피카츄 그 자체입니다."
    },
    "ESFP": {
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "type": "노멀/페어리 🎤",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "feature": "어디서나 스포트라이트를 받는 유쾌한 분위기 메이커.",
        "reason": "사람들의 관심을 즐기고 분위기를 북돋우는 ESFP는 언제나 자신만의 무대에서 노래를 부르는 사랑스러운 푸린과 똑 닮았습니다."
    },
    "ENFP": {
        "ko_name": "파이리",
        "en_name": "Charmander",
        "type": "불꽃 🔥",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png",
        "feature": "열정이 꼬리 불꽃처럼 끊임없이 타오르는 긍정왕.",
        "reason": "새로운 것에 호기심이 많고 긍정적인 에너지를 내뿜는 ENFP는 꼬리의 불꽃이 꺼지지 않는 열정적인 파이리와 완벽한 케미를 자랑합니다."
    },
    "ENTP": {
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "type": "고스트/독 👻",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "feature": "장난기 넘치고 재치 있는 아이디어로 상대방을 놀라게 만듦.",
        "reason": "고정관념을 깨고 정형화된 틀을 흔드는 ENTP 특유의 위트와 논쟁가적 기질은 장난기 가득한 웃음을 지닌 팬텀과 찰떡궁합입니다."
    },
    "ESTJ": {
        "ko_name": "윈디",
        "en_name": "Arcanine",
        "type": "불꽃 🦁",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "feature": "당당한 리더십과 강력한 추진력으로 무리를 이끎.",
        "reason": "체계적이고 당당하게 조직을 지휘하는 ESTJ의 통솔력은 위풍당당한 기상으로 무리를 지켜내는 전설 포켓몬 윈디의 아우라와 일치합니다."
    },
    "ESFJ": {
        "ko_name": "꼬북이",
        "en_name": "Squirtle",
        "type": "물 🐢",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png",
        "feature": "친화력이 뛰어나고 동료들과의 협동을 최고로 중요시함.",
        "reason": "주변 사람들과의 관계를 중시하고 친화력이 폭발하는 ESFJ는 귀여운 팀워크로 의리를 다지는 꼬북이 군단과 환상의 조합입니다."
    },
    "ENFJ": {
        "ko_name": "망나뇽",
        "en_name": "Dragonite",
        "type": "드래곤/비행 🐲",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "feature": "넓은 바다 같은 포용력으로 모두를 따뜻하게 이끄는 조력자.",
        "reason": "상대방의 가능성을 이끌어주고 따뜻하게 보듬어주는 ENFJ는 바다에서 위험에 빠진 이들을 도와주는 다정한 망나뇽과 닮아 있습니다."
    },
    "ENTJ": {
        "ko_name": "리자몽",
        "en_name": "Charizard",
        "type": "불꽃/비행 🐲",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "feature": "목표를 향해 거침없이 나아가는 압도적인 비전과 승부욕.",
        "reason": "비전을 세우고 주도적으로 상황을 개척하는 ENTJ의 장군 같은 성향은 강력한 불꽃을 내뿜으며 전장을 지배하는 리자몽의 위엄과 통합니다."
    }
}

# 4. 헤더 영역 화면 출력
st.markdown("<div class='main-title'>⚡ MBTI로 찾는 나의 단짝 포켓몬 ⚡</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>당신의 MBTI를 선택하면 꼭 닮은 포켓몬 친구를 소개해 드려요!</div>", unsafe_allow_html=True)

# 5. MBTI 선택 드롭다운
mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택해 주세요:",
    options=mbti_list,
    index=0
)

st.write("") # 여백

# 6. 결과 출력 영역
if selected_mbti:
    pokemon = POKEMON_DATA[selected_mbti]
    
    # 단짝 포켓몬을 찾으면 축하 효과(풍선) 실행!
    st.balloons()
    
    # 단짝 포켓몬 정보 카드 렌더링
    st.markdown(f"""
    <div class="pokemon-card">
        <div style="text-align: center;">
            <span class="type-badge">{pokemon['type']}</span>
        </div>
        <div class="pokemon-name">{pokemon['ko_name']} <span style="font-size: 1.2rem; color: #92400E;">({pokemon['en_name']})</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2열 레이아웃 (좌: 이미지, 우: 정보)
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.image(pokemon['img_url'], use_container_width=True)
        
    with col2:
        st.markdown(f"""
        <div style="padding-top: 10px;">
            <p class="info-text"><span class="label-text">✨ 주요 특징:</span><br>{pokemon['feature']}</p>
            <p class="info-text"><span class="label-text">💛 잘 어울리는 이유:</span><br>{pokemon['reason']}</p>
        </div>
        """, unsafe_allow_html=True)

# 하단 푸터
st.markdown("---")
st.caption("© 2026 MBTI x Pokémon Partner Finder | Powered by Streamlit")
