import streamlit as st
import yfinance as yf
import time

# הגדרות דף
st.set_page_config(page_title="הגרלת מתנה לאלמוג", page_icon="🎁", layout="centered")

# הזרקת CSS מקיפה למרכזיות מוחלטת ועיצוב
st.markdown("""
    <style>
    /* מרכז את כל התוכן של האפליקציה */
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    /* הגדרות טקסט כלליות */
    .rtl-center {
        direction: RTL;
        text-align: center;
        width: 100%;
    }

    /* עיצוב כפתור ההגרלה */
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
        transition: transform 0.2s;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #ff3333;
    }

    /* מרכוז כותרות של Streamlit */
    h1, h2, h3, p, span {
        text-align: center !important;
        direction: RTL !important;
    }

    /* עיצוב המטריקה (המחיר) */
    [data-testid="stMetricValue"] {
        display: flex;
        justify-content: center;
        font-size: 40px !important;
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
        return 175.20  # מחיר לגיבוי

# --- תצוגה לפני הלחיצה ---
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
    st.title("🎁 הגרלת מתנה לאלמוג")
    st.markdown("### אלמוג היקר, הגיע הזמן לגלות מה מחכה לך...")
    st.write("לחץ על הכפתור למטה כדי להפעיל את הגרלת המתנה שלך לשנת 2026!")
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
            <h1 style="color: #2ecc71; margin: 0;">זכית ב-2 מניות GOOGL!</h1>
            <p style="font-size: 22px; color: white; margin-top: 10px;">חברת Alphabet Inc (Google)</p>
        </div>
    """, unsafe_allow_html=True)

    # מחיר חי
    current_price = get_stock_price("GOOGL")
    st.metric(label="שווי מניה נוכחי (USD)", value=f"${current_price}")

    st.markdown(f"## **באהבה גדולה, מאבא ומאופק**")
    st.write(f"""
    החלטנו שהשנה המתנה שלך תהיה נכס אמיתי שיצמח יחד איתך. 
    אלו לא סתם מספרים, אלא בעלות באחת החברות המשפיעות בעולם.
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", width=150)
    
    st.info(f"""
    **סיכום הזכייה:**
    * כמות: 2 מניות שלמות
    * שווי כולל: ${round(current_price * 2, 2)}
    * סטטוס: הועבר לחשבון אינטראקטיב ישראל שלך
    """)
    
    st.markdown('<br><p style="font-size: 12px; color: gray;">מתנה לטווח ארוך | כוחה של הריבית דריבית עובד בשבילך</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
