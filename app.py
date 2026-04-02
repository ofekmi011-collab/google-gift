import streamlit as st
import yfinance as yf
import time

# הגדרות דף - שם נייטרלי להפתעה
st.set_page_config(page_title="הגרלת מתנה לאלמוג", page_icon="🎁", layout="centered")

# הזרקת CSS לתיקון כיוון כתיבה (RTL), מרכזיות ועיצוב כפתור
st.markdown("""
    <style>
    .rtl-center {
        direction: RTL;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        border-radius: 50px;
        width: 250px;
        height: 60px;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    .stMetric {
        background-color: #1e2129;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
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
        return 175.0  # מחיר גיבוי למקרה של תקלה

# כותרת ראשית מסתורית
st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
st.title("🎁 הגרלת מתנה לאלמוג")
st.write("### אלמוג היקר, הגיע הזמן לגלות מה מחכה לך...")
st.write("לחץ על הכפתור למטה כדי להפעיל את הגרלת המתנה שלך לשנת 2026!")
st.markdown('</div>', unsafe_allow_html=True)

# כפתור הפעלה ממורכז
st.markdown('<div style="display: flex; justify-content: center; padding-top: 20px;">', unsafe_allow_html=True)
if st.button('🎊 הפעל הגרלה! 🎊'):
    # אפקט טעינה ליצירת מתח
    with st.spinner('מבצע הגרלה במערכת...'):
        time.sleep(2)
    
    st.balloons()
    
    # הצגת המתנה - הכל נחשף כאן
    st.markdown("""
        <div style="background-color: #1e3a2f; padding: 25px; border-radius: 15px; border: 2px solid #2ecc71; direction: RTL; text-align: center; margin-bottom: 20px;">
            <h1 style="color: #2ecc71; margin-bottom: 0;">זכית ב-2 מניות GOOGL!</h1>
            <p style="font-size: 20px; color: white;">חברת Alphabet Inc (Google)</p>
        </div>
    """, unsafe_allow_html=True)

    # הבאת מחיר חי לאחר החשיפה
    current_price = get_stock_price("GOOGL")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.metric(label="שווי מניה נוכחי (USD)", value=f"${current_price}")

    st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
    st.write(f"""
    החלטנו שהשנה המתנה שלך תהיה נכס אמיתי שיצמח יחד איתך. 
    אלו לא סתם מספרים, אלא בעלות באחת החברות המשפיעות בעולם.
    """)
    st.markdown(f"## **באהבה גדולה, מאבא ומאופק**")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", width=150)
    
    st.info(f"""
    **פרטי התיק המעודכנים:**
    * **כמות:** 2 מניות שלמות
    * **שווי שוק כולל:** ${round(current_price * 2, 2)}
    * **סטטוס:** הועבר לחשבון אינטראקטיב ישראל שלך
    """)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # מה שרואים לפני הלחיצה - רק תמונה נייטרלית של מתנה
    st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/214/214305.png", width=200)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# הערה בתחתית
st.markdown('<br><div class="rtl-center" style="font-size: 12px; color: gray;">מתנה לטווח ארוך | כוחה של הריבית דריבית עובד בשבילך</div>', unsafe_allow_html=True)
