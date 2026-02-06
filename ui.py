import streamlit as st
import requests

st.title("AI Operations Assistant")

task = st.text_area("Enter your task")

if st.button("Run Task"):
    try:
        res = requests.post("http://127.0.0.1:8000/run-task", json={"task": task})

        st.write("Status Code:", res.status_code)

        try:
            st.json(res.json())
        except:
            st.error("Backend returned non-JSON response:")
            st.text(res.text)

    except Exception as e:
        st.error(f"Backend not running: {e}")
