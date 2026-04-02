import streamlit as st
import yfinance as yf
import time

# הגדרות דף - זה מה שיוצג בוואטסאפ
st.set_page_config(page_title="מתנה מאבא ואופק לאלמוג", page_icon="🎁")

# הזרקת CSS למרכזיות ויישור לימין
st.markdown("""
    <style>
    .main .block-container { direction: RTL; text-align: center; }
    div.stButton > button:first-child { 
        background-color: #FF4B4B; color: white; border-radius: 50px; 
        padding: 10px 30px; font-size: 20px; font-weight: bold;
    }
    [data-testid="stMetricValue"] { justify-content: center; display: flex; font-weight: bold; }
    [data-testid="stMetricLabel"] { justify-content: center; display: flex; }
    .stAlert { direction: RTL; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# פונקציה להבאת מחיר
def get_price():
    try:
        return round(yf.Ticker("GOOGL").history(period="1d")['Close'].iloc[-1], 2)
    except:
        return 295.77

# תאריך קבוע לבקשתך
lottery_date = "03/04/2026"

# לוגיקת הפתעה
if 'show' not in st.session_state:
    st.session_state.show = False

if not st.session_state.show:
    st.title("🎁 הגרלת מתנה לאלמוג")
    st.subheader("אלמוג היקר, הגיע הזמן לגלות מה מחכה לך...")
    st.image("https://cdn-icons-png.flaticon.com/512/214/214305.png", width=150)
    
    if st.button('🎊 לחץ להפעלת ההגרלה! 🎊'):
        st.session_state.show = True
        st.rerun()
else:
    with st.spinner('מחשב תוצאות הגרלה...'):
        time.sleep(1.5)
    st.balloons()
    
    st.success("## זכית במניה 1 של GOOGL!")
    
    price = get_price()
    st.metric(label="שווי המניה כרגע (USD)", value=f"${price}")
    
    st.markdown(f"### **באהבה גדולה, מאבא ומאופק**")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", width=120)
    
    st.info(f"""
    **פרטי המתנה:**
    * כמות: מניה 1 שלמה
    * תאריך רכישה: {lottery_date}
    * סטטוס: הועבר לחשבון אינטראקטיב ישראל שלך
    """)
    st.caption(f"תאריך הצפייה: {lottery_date} | לטווח ארוך בלבד! 😉")
