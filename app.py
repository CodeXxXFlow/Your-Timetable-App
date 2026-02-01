import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Your Timetable",
    page_icon="📚",
    layout="centered"
)

# Custom CSS for better look
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2E86C1;
    }
    .period {
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        background-color: #000000;
    }
    .break {
        background-color: #FAD7A0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>Your Timetable</div>", unsafe_allow_html=True)
st.write("### Select the day to see your periods")

# Timetable (edit subjects as per your class)
timetable = {
    "Monday": [
        ("Period 1", "2 Lang"),
        ("Period 2", "Lib/GK"),
        ("Period 3", "Math"),
        ("Period 4", "English"),
        ("Break", "🍎 Break Time"),
        ("Period 5", "Geography"),
        ("Period 6", "Chemistry"),
        ("Period 7", "AI"),
        ("Period 8", "Art"),
        ("Period 9", "3 lang")
    ],
    "Tuesday": [
        ("Period 1", "History"),
        ("Period 2", "3 Lang"),
        ("Period 3", "Math"),
        ("Period 4", "Biology"),
        ("Break", "🍎 Break Time"),
        ("Period 5", "Physics"),
        ("Period 6", "FL/VED"),
        ("Period 7", "2 Lang"),
        ("Period 8", "English"),
        ("Period 9", "Dance/Muisc")
    ],
    "Wednesday": [
        ("Period 1", "Math"),
        ("Period 2", "EVE"),
        ("Period 3", "English"),
        ("Period 4", "Biology"),
        ("Break", "🍎 Break Time"),
        ("Period 5", "2 Lang"),
        ("Period 6", "Physics"),
        ("Period 7", "Geography"),
        ("Period 8", "History"),
        ("Period 9", "SUPW")
    ],
    "Thursday": [
        ("Period 1", "Math"),
        ("Period 2", "Chemistry"),
        ("Period 3", "Games"),
        ("Period 4", "Geography"),
        ("Break", "🍎   Break Time"),
        ("Period 5", "Computer Science"),
        ("Period 6", "2 lang"),
        ("Period 7", "Biology"),
        ("Period 8", "English"),
        ("Period 9", "Afternoon Activities")
    ],
    "Friday": [
        ("Period 1", "Math"),
        ("Period 2", "English"),
        ("Period 3", "Computer science"),
        ("Period 4", "Maths"),
        ("Break", "🍎 Break Time"),
        ("Period 5", "Chemistry"),
        ("Period 6", "Physics"),
        ("Period 7", "History"),
        ("Period 8", "2 Lang")
    ]
}

# Day selector
day = st.selectbox("Which day is today?", list(timetable.keys()))

# Display timetable
st.write(f"## 📅 {day}")
for period, subject in timetable[day]:
    if period == "Break":
        st.markdown(f"<div class='period break'>{subject}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='period'>{period}: {subject}</div>", unsafe_allow_html=True)

st.write("Be a sigma and pack your bags!")
