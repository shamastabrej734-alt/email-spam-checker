import streamlit as st
import joblib
st.title("ML MODEL EMAIL CHECK SPAM AND NOT")

email=st.text_input("ENTER YOUR EMAIL SMS")

model=joblib.load("model.pkl")
vectorizer=joblib.load("vectorizer.pkl")

if st.button("CHECK"):  

    if email.strip()=="":
        st.warning("Please enter your email message")


    else:
        message_vector=vectorizer.transform([email])
        prediction=model.predict(message_vector)[0]
        st.write("Prediction:", prediction)
        
        if prediction==0:
            st.error("SPAM")
        else:
            st.success("NOT SPAM")