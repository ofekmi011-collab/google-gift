import streamlit as st
import yfinance as yf
import time
from datetime import datetime

# --- הגדרות דף ---
st.set_page_config(
    page_title="מתנה מאבא ואופק לאלמוג", 
    page_icon="🎁", 
    layout="centered"
)

# --- הזרקת CSS למרכזיות מוחלטת ועיצוב ---
st.markdown("""
    <style>
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .rtl-center {
        direction: RTL;
        text-align: center;
        width: 100%;
    }
    div.stButton {
        display: flex;
        justify-content: center;
    }
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 24px;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    h1, h2, h3, p, span, li, label {
        text-align: center !important;
        direction: RTL !important;
        width: 100%;
    }
    .stAlert ul {
        display: flex;
        flex-direction: column;
        align-items: center;
        list-style-type: none;
        padding: 0;
    }
    .stAlert li {
        margin: 5px 0;
    }
    [data-testid="stMetricValue"] {
        display: flex;
        justify-content: center;
        font-size: 48px !important;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציה להבאת מחיר מניה
def get_stock_price(ticker):
    try:
        data = yf.Ticker(ticker)
        price = data.history(period="1d")['Close'].iloc[-1]
        return round(price, 2)
    except:
        return 295.77

# תאריך נוכחי בפורמט ישראלי
today_date = datetime.now().strftime("%d/%m/%Y")

# --- תצוגה לפני הלחיצה ---
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
    st.title("🎁 הגרלת מתנה לאלמוג")
    st.markdown(f"### היום: {today_date}")
    st.markdown("### אלמוג היקר, הגיע הזמן לגלות מה מחכה לך...")
    st.write("לחץ על הכפתור למטה כדי להפעיל את הגרלת המתנה שלך!")
    st.image("https://cdn-icons-png.flaticon.com/512/214/214305.png", width=200)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button('🎊 הפעל הגרלה! 🎊'):
        st.session_state.clicked = True
        st.rerun()

# --- תצוגה אחרי הלחיצה ---
else:
    with st.spinner('מבצע הגרלה במערכת...'):
        time.sleep(2)
    
    st.balloons()
    
    st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #1e3a2f; padding: 25px; border-radius: 15px; border: 2px solid #2ecc71; margin-bottom: 25px;">
            <h1 style="color: #2ecc71; margin: 0;">זכית במניה 1 של GOOGL!</h1>
            <p style="font-size: 22px; color: white; margin-top: 10px;">חברת Alphabet Inc (Google)</p>
        </div>
    """, unsafe_allow_html=True)

    current_price = get_stock_price("GOOGL")
    st.metric(label="שווי המניה כרגע (USD)", value=f"${current_price}")

    st.markdown(f"## **באהבה גדולה, מאבא ומאופק**")
    st.write(f"החלטנו שהשנה המתנה שלך תהיה נכס אמיתי שיצמח יחד איתך.")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", width=150)
    
    st.markdown('<br>', unsafe_allow_html=True)
    
    # סיכום הזכייה כולל תאריכים
    st.info(f"""
    **סיכום הזכייה:**
    * כמות: מניה 1 שלמה
    * שווי כולל: ${current_price}
    * תאריך רכישה: {today_date}
    * סטטוס: הועבר לחשבון אינטראקטיב ישראל שלך
    """)
    
    st.markdown(f'<br><p style="font-size: 14px;">תאריך הצפייה: {today_date}</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 12px; color: gray;">מתנה לטווח ארוך | כוחה של הריבית דריבית עובד בשבילך</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
