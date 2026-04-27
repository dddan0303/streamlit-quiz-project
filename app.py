import streamlit as st
import csv
import os
from datetime import datetime

STUDENT_ID = "2025404008"
STUDENT_NAME = "김다은"

RESULT_FILE = "quiz_result.csv"

st.set_page_config(
    page_title="나만의 동네 탐험 스타일 테스트",
    page_icon="🧭",
    layout="centered"
)


@st.cache_data
def load_quiz_data():
    return [
        {
            "question": "친구가 갑자기 오늘 놀자고 하면 나는?",
            "options": {
                "조용한 카페에서 이야기하고 싶다": "healing",
                "사람 많은 핫플에 가보고 싶다": "trend",
                "사진 잘 나오는 전시나 팝업을 찾는다": "record",
                "공원이나 산책길을 걷고 싶다": "nature"
            }
        },
        {
            "question": "처음 가는 장소를 고를 때 가장 중요하게 보는 것은?",
            "options": {
                "분위기와 편안함": "healing",
                "리뷰 수와 인기": "trend",
                "인테리어와 개성": "record",
                "주변 환경과 여유로움": "nature"
            }
        },
        {
            "question": "내가 리뷰를 남긴다면 가장 많이 쓸 말은?",
            "options": {
                "조용해서 쉬기 좋았어요": "healing",
                "웨이팅은 있지만 유명한 이유가 있어요": "trend",
                "사진 찍기 좋은 포인트가 많아요": "record",
                "걷기 좋고 마음이 편해졌어요": "nature"
            }
        },
        {
            "question": "탐험 앱에서 가장 받고 싶은 뱃지는?",
            "options": {
                "감성 카페 발견 뱃지": "healing",
                "핫플 정복 뱃지": "trend",
                "기록왕 뱃지": "record",
                "산책 마스터 뱃지": "nature"
            }
        },
        {
            "question": "나에게 가장 잘 맞는 하루 코스는?",
            "options": {
                "카페 → 서점 → 조용한 식당": "healing",
                "맛집 → 쇼핑거리 → 유명 디저트집": "trend",
                "전시회 → 포토존 → 감성 소품샵": "record",
                "공원 → 산책로 → 한적한 동네 카페": "nature"
            }
        },
        {
            "question": "새로운 장소를 발견했을 때 나는?",
            "options": {
                "나만 알고 싶은 장소로 저장한다": "healing",
                "친구들에게 바로 공유한다": "trend",
                "사진과 후기를 꼼꼼히 남긴다": "record",
                "근처까지 천천히 둘러본다": "nature"
            }
        },
        {
            "question": "장소를 탐험할 때 가장 기분 좋은 순간은?",
            "options": {
                "생각보다 조용하고 편안한 공간을 찾았을 때": "healing",
                "SNS에서 봤던 유명한 곳에 직접 갔을 때": "trend",
                "예쁜 사진을 남길 수 있는 공간을 찾았을 때": "record",
                "걷다가 우연히 좋은 풍경을 발견했을 때": "nature"
            }
        }
    ]


@st.cache_data
def load_result_data():
    return {
        "healing": {
            "emoji": "☕",
            "title": "조용한 힐링 탐험가",
            "desc": "당신은 복잡한 장소보다 조용하고 편안한 공간을 좋아하는 타입입니다. 혼자만의 시간을 즐기거나 차분한 분위기에서 에너지를 회복하는 편입니다.",
            "recommend": "감성 카페, 북카페, 조용한 식당, 독립서점"
        },
        "trend": {
            "emoji": "🔥",
            "title": "핫플 정복 탐험가",
            "desc": "당신은 새로운 유행과 인기 장소에 관심이 많은 타입입니다. 사람들이 많이 찾는 곳을 직접 경험하고 친구들과 공유하는 것을 좋아합니다.",
            "recommend": "핫플 맛집, 번화가, 유명 디저트 카페, 쇼핑 거리"
        },
        "record": {
            "emoji": "📸",
            "title": "감성 기록 탐험가",
            "desc": "당신은 장소의 분위기와 개성을 중요하게 생각하는 타입입니다. 예쁜 공간을 발견하고 사진과 글로 기록하는 것을 좋아합니다.",
            "recommend": "전시회, 팝업스토어, 포토존, 감성 소품샵"
        },
        "nature": {
            "emoji": "🌿",
            "title": "여유로운 산책 탐험가",
            "desc": "당신은 자연스럽고 여유로운 장소에서 편안함을 느끼는 타입입니다. 시끄러운 공간보다 걷기 좋고 조용한 장소를 선호합니다.",
            "recommend": "공원, 산책로, 한강, 조용한 골목길"
        }
    }


def save_result(name, result_title, scores):
    file_exists = os.path.exists(RESULT_FILE)

    with open(RESULT_FILE, "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "이름",
                "결과 유형",
                "힐링형 점수",
                "트렌드형 점수",
                "기록형 점수",
                "자연형 점수",
                "저장 시간"
            ])

        writer.writerow([
            name,
            result_title,
            scores["healing"],
            scores["trend"],
            scores["record"],
            scores["nature"],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])


def load_saved_results():
    if not os.path.exists(RESULT_FILE):
        return []

    with open(RESULT_FILE, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        return list(reader)


def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.quiz_finished = False
    st.session_state.result_saved = False


# 세션 상태 초기화
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "login_id" not in st.session_state:
    st.session_state.login_id = ""

if "login_pw" not in st.session_state:
    st.session_state.login_pw = ""

if "result_saved" not in st.session_state:
    st.session_state.result_saved = False


# 상단 화면
st.title("🧭 나만의 동네 탐험 스타일 테스트")

st.markdown(
    f"""
    <div style="
        background-color:#F3F8F4;
        padding:16px;
        border-radius:14px;
        border:1px solid #CFE8D5;
        margin-bottom:15px;
    ">
        <b>학번:</b> {STUDENT_ID}<br>
        <b>이름:</b> {STUDENT_NAME}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        background-color:#FFFDF6;
        padding:14px;
        border-radius:12px;
        border:1px solid #E8D9B5;
        margin-bottom:15px;
    ">
        이 앱은 사용자의 답변을 바탕으로 장소 탐험 성향을 분석하는 Streamlit 퀴즈 앱입니다.
    </div>
    """,
    unsafe_allow_html=True
)


# 로그인 전 화면
if not st.session_state.logged_in:
    st.divider()
    st.subheader("🔐 로그인")

    st.text_input("아이디", key="login_id")
    st.text_input("비밀번호", type="password", key="login_pw")

    st.caption("테스트용 로그인 정보: 아이디 dan / 비밀번호 1234")

    col1, col2 = st.columns(2)

    with col1:
        login_btn = st.button("로그인하기", use_container_width=True)

    with col2:
        cancel_btn = st.button("취소", use_container_width=True)

    if login_btn:
        if st.session_state.login_id == "dan" and st.session_state.login_pw == "1234":
            st.session_state.logged_in = True
            reset_quiz()
            st.success("로그인 성공!")
            st.rerun()
        else:
            st.error("로그인 실패! 아이디 또는 비밀번호를 확인하세요.")

    if cancel_btn:
        st.session_state.login_id = ""
        st.session_state.login_pw = ""
        st.info("로그인 입력을 취소했습니다.")
        st.rerun()


# 로그인 후 화면
else:
    st.caption("로그인 완료")

    questions = load_quiz_data()
    results = load_result_data()
    total_questions = len(questions)

    if not st.session_state.quiz_finished:
        current = st.session_state.current_question
        question_data = questions[current]

        st.divider()
        st.subheader("📝 탐험 스타일 퀴즈")

        st.progress((current + 1) / total_questions)
        st.caption(f"현재 문제 {current + 1} / {total_questions}")

        st.markdown(
            f"""
            <div style="
                background-color:#FFF8E7;
                padding:24px;
                border-radius:18px;
                border:1px solid #F1D28A;
                margin-top:15px;
                margin-bottom:20px;
            ">
                <h3>Q{current + 1}. {question_data['question']}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        options = list(question_data["options"].keys())

        # 이전에 선택했던 답변이 있으면 그 값을 기본 선택으로 유지
        if len(st.session_state.answers) > current:
            saved_type = st.session_state.answers[current]
            default_index = 0

            for option_text, option_type in question_data["options"].items():
                if option_type == saved_type:
                    default_index = options.index(option_text)
                    break
        else:
            default_index = 0

        selected = st.radio(
            "답변을 선택하세요",
            options,
            index=default_index,
            key=f"radio_{current}"
        )

        selected_type = question_data["options"][selected]

        # 현재 선택값을 세션에 바로 저장해서 이전/다음 이동 시 유지
        if len(st.session_state.answers) > current:
            st.session_state.answers[current] = selected_type
        else:
            st.session_state.answers.append(selected_type)

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("← 이전", disabled=current == 0, use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()

        with col2:
            if st.button("처음부터", use_container_width=True):
                reset_quiz()
                st.rerun()

        with col3:
            if current < total_questions - 1:
                if st.button("다음 →", use_container_width=True):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("결과 보기", use_container_width=True):
                    st.session_state.quiz_finished = True
                    st.rerun()

    else:
        scores = {
            "healing": 0,
            "trend": 0,
            "record": 0,
            "nature": 0
        }

        for answer in st.session_state.answers:
            scores[answer] += 1

        final_type = max(scores, key=scores.get)
        final_result = results[final_type]

        st.divider()
        st.subheader("🎉 나의 탐험 스타일 결과")

        st.markdown(
            f"""
            <div style="
                background-color:#F3F8F4;
                padding:28px;
                border-radius:20px;
                border:1px solid #CFE8D5;
                margin-bottom:20px;
            ">
                <h1>{final_result['emoji']} {final_result['title']}</h1>
                <p style="font-size:17px;">{final_result['desc']}</p>
                <p style="font-size:16px;"><b>추천 장소:</b> {final_result['recommend']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("### 📊 유형별 점수")

        st.write(f"☕ 힐링형: {scores['healing']}점")
        st.progress(scores["healing"] / total_questions)

        st.write(f"🔥 트렌드형: {scores['trend']}점")
        st.progress(scores["trend"] / total_questions)

        st.write(f"📸 기록형: {scores['record']}점")
        st.progress(scores["record"] / total_questions)

        st.write(f"🌿 자연형: {scores['nature']}점")
        st.progress(scores["nature"] / total_questions)

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("결과 저장", use_container_width=True, disabled=st.session_state.result_saved):
                save_result(STUDENT_NAME, final_result["title"], scores)
                st.session_state.result_saved = True
                st.success("결과가 저장되었습니다!")

        with col2:
            if st.button("다시 풀기", use_container_width=True):
                reset_quiz()
                st.rerun()

        with col3:
            if st.button("로그아웃", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.login_id = ""
                st.session_state.login_pw = ""
                reset_quiz()
                st.rerun()

        saved_results = load_saved_results()

        if len(saved_results) > 1:
            with st.expander("저장된 결과 보기"):
                st.table(saved_results)
