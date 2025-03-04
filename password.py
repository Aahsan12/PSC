import re
import streamlit as st

# Page styling 
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

#custom CSS
st.markdown(""" 
<style>
    .main { text-align: center; }
    .stTextInput { width: 60% !important; margin: auto; }
    .stButton { width: 30%, background-color: Blue; color: white; font-size: 18px; }
    .stButton:hover { background-color: Red, color: white; }
</style>
""", unsafe_allow_html=True)

# page title & Description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level.🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1 #increased score by 1 if password length is greater than 8
    else:
        feedback.append("❌ Password length should be at least 8 characters.")  
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase characters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain numbers.")
        
# special characters
    if re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain special characters.")

# Display password strength result
    if score == 4:
        feedback.append("✅ **Strong Password** - Your password is strong.")
    elif score == 3:
        st.info("🟡 **Medium Password** - Your password is medium.")
    else:    
        st.error("🔴 **Weak Password** - Your password is weak.")
        
#Feedback
    if feedback:
        with st.expander("Show Feedback 🔍"):
            for message in feedback:
                st.write(message)
        
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔒")

#Button Working 
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.") #Show warning if no password is entered