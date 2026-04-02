import streamlit as st
import yfinance as yf
import time

# --- הגדרות דף ---
st.set_page_config(
    page_title="מתנה מאבא ואופק לאלמוג", 
    page_icon="🎁", 
    layout="centered"
)

# --- הזרקת CSS למרכזיות מוחלטת ועיצוב ---
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
    }

    /* מרכוז כותרות ורכיבי Streamlit רגילים */
    h1, h2, h3, p, span, li, label {
        text-align: center !important;
        direction: RTL !important;
        width: 100%;
    }
    
    /* תיקון ספציפי למרכוז רשימות (המלבן הכחול) */
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

    /* עיצוב המטריקה (המחיר) */
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
    
    /* מרכוז תמונות */
    [data-testid="stImage"] {
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
        return 175.20  # מחיר גיבוי

# תאריך ההגרלה/הרכישה הקבוע
lottery_date = "03/04/2026"

# --- תצוגה לפני הלחיצה ---
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    st.markdown('<div class="rtl-center">', unsafe_allow_html=True)
    st
