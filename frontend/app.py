import streamlit as st
import requests

st.title("🧠 Autonomous AI Research Assistant")

query = st.text_input(
    "Enter research topic"
)

if st.button("Run Research"):

    if not query.strip():

        st.warning("Please enter a topic")

    else:

        with st.spinner("Research agents working..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/research",
                    json={
                        "query": query
                    },
                    timeout=300
                )

                st.write("STATUS:", response.status_code)

                data = response.json()

                # -----------------------------
                # ERROR HANDLING
                # -----------------------------
                if not data.get("success"):

                    st.error(data.get("error"))

                else:

                    st.subheader("📌 Research Plan")
                    st.write(data.get("plan"))

                    st.subheader("🔍 Analysis")
                    st.write(data.get("analysis"))

                    st.subheader("📄 Final Report")
                    st.write(data.get("report"))

            except Exception as e:

                st.error(str(e))