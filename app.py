import streamlit as st
import yfinance as yf
import time

# הגדרות דף
st.set_page_config(page_title="מתנה מאבא ואופק לאלמוג", page_icon="🎁")

# הזרקת CSS למרכוז מוחלט מכל כיוון
st.markdown("""
    <style>
    /* מרכוז המכולה הראשית */
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        direction: RTL;
    }
    
    /* מרכוז כותרות וטקסט */
    h1, h2, h3, p, span, div {
        text-align: center !important;
        justify-content: center !important;
    }

    /* מרכוז תמונות */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }

    /* מרכוז ועיצוב הכפתור */
    div.stButton {
        display: flex;
        justify-content: center;
        width: 100%;
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

    /* מרכוז רכיב המטריקה (המחיר) */
    [data-testid="stMetric"] {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    [data-testid="stMetricValue"] {
        font-weight: bold;
    }

    /* עיצוב ומרכוז המלבן הכחול */
    .stAlert {
        display: flex;
        flex-direction: column;
        align-items: center;
        direction: RTL;
    }
    .stAlert ul {
        list-style-type: none;
        padding: 0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציה להבאת מחיר
def get_price():
    try:
        return round(yf.Ticker("GOOGL").history(period="1d")['Close'].iloc[-1], 2)
    except:
        return 295.77

lottery_date = "03/04/2026"

if 'show' not in st.session_state:
    st.session_state.show = False

# דף ההגרלה (לפני הלחיצה)
if not st.session_state.show:
    st.title("🎁 הגרלת מתנה לאלמוג")
    st.markdown("### אלמוג היקר, הגיע הזמן לגלות מה מחכה לך...")
    st.write("לחץ על הכפתור למטה כדי להפעיל את הגרלת המתנה שלך!")
    
    st.image("https://cdn-icons-png.flaticon.com/512/214/214305.png", width=200)
    
    if st.button('🎊 לחץ להפעלת ההגרלה! 🎊'):
        st.session_state.show = True
        st.rerun()

# דף התוצאה (אחרי הלחיצה)
else:
    with st.spinner('מחשב תוצאות הגרלה...'):
        time.sleep(2)
    st.balloons()
    
    st.success("## זכית במניה 1 של GOOGL!")
    
    price = get_price()
    st.metric(label="שווי המניה כרגע (USD)", value=f"${price}")
    
    st.markdown(f"## **באהבה גדולה, מאבא ומאופק**")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", width=150)
    
    st.info(f"""
    **סיכום הזכייה:**
    * כמות: מניה 1 שלמה
    * תאריך רכישה: {lottery_date}
    * סטטוס: הועבר לחשבון אינטראקטיב ישראל שלך
    """)
    
    st.caption(f"תאריך הצפייה: {lottery_date}")
    st.markdown('<p style="font-size: 12px; color: gray;">מתנה לטווח ארוך | כוחה של הריבית דריבית עובד בשבילך</p>', unsafe_allow_html=True)
