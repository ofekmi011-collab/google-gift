import streamlit as st

# עיצוב דף האפליקציה
st.set_page_config(page_title="מתנה מאופק", page_icon="🎁")

st.title("🎁 אפליקציית הענקת מניות - אופק מיימון")
st.subheader("מזל טוב אח יקר!")

st.write("""
החלטתי שהשנה המתנה שלך תהיה כזו שתמשיך לצמוח יחד איתך. 
לא עוד כסף מזומן שנעלם, אלא חלק מאחת החברות הגדולות בעולם.
""")

# כפתור הפעלה
if st.button('לחץ כאן כדי לקבל את המתנה שלך'):
    st.balloons()
    st.success("ברכות! 2 מניות של GOOGL (Alphabet Inc) הועברו לחשבונך!")
    
    # תצוגת פרטי המניה
    st.info("""
    **פרטי הנכס:**
    * **חברה:** Alphabet Inc.
    * **סימול:** GOOGL
    * **כמות:** 2 מניות
    * **סטטוס:** הועבר בתיאום עם אינטראקטיב ישראל
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg", width=200)
    
    st.write("---")
    st.warning("הערה: המניות מיועדות להחזקה לטווח ארוך. אל תמכור לפני 2030! 😉")
