
import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(page_title="Spam Message Detector", page_icon="📩")

model_path = Path(__file__).with_name("spam_model.pkl")
model = joblib.load(model_path)

st.title("📩 Spam Message Detector")
st.write("Enter a message to check whether it is spam or not.")

message = st.text_area("Your message", placeholder="Type your message here...")

if st.button("Check Message"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        prediction = str(model.predict([message])[0]).strip().lower()

        if prediction in ("spam", "1"):
            st.error("🚨 This message is SPAM.")
        elif prediction in ("ham", "not spam", "0"):
            st.success("✅ This message is NOT SPAM.")
        else:
            st.info(f"Model prediction: {prediction}")
