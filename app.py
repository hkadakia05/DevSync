import streamlit as st
import tempfile
from orchestrator import get_orchestrator
from prompts import CODE_REVIEW_PROMPT, AUDIO_TRANSCRIBER_PROMPT, EMAIL_ANALYZER_PROMPT, SUMMARY_PROMPT

agent = get_orchestrator()

st.set_page_config(page_title="DevSync AI", layout="wide")
st.title("🚀 DevSync AI – Multi-Agent Developer Assistant")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a feature:", ["Code Review", "Meeting Audio", "Email Analyzer", "Dashboard"])

# --- CODE REVIEW ---
if page == "Code Review":
    st.header("Code Review Agent")
    repo_url = st.text_input("GitHub Repo URL (optional):")
    code_input = st.text_area("Paste your Python code here:")
    uploaded_file = st.file_uploader("Or upload a Python file:", type=["py"])

    if st.button("Run Code Review"):
        st.info("Analyzing code...")
        if repo_url:
            query = f"{CODE_REVIEW_PROMPT}\nAnalyze GitHub repository: {repo_url}"
        elif code_input:
            with open("temp.py", "w") as f:
                f.write(code_input)
            query = f"{CODE_REVIEW_PROMPT}\nReview the code in temp.py"
        elif uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name
            query = f"{CODE_REVIEW_PROMPT}\nReview the code in {tmp_path}"
        else:
            st.error("Please provide code or repo URL.")
            query = None

        if query:
            response = agent.run(query)
            st.subheader("Analysis Result")
            st.write(response)

# --- MEETING AUDIO ---
elif page == "Meeting Audio":
    st.header("Meeting Audio → Transcript → Action")
    audio_file = st.file_uploader("Upload meeting audio (.wav/.mp3):", type=["wav", "mp3"])

    if audio_file and st.button("Transcribe & Analyze"):
        st.info("Processing audio...")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            tmp_path = tmp.name
        query = f"{AUDIO_TRANSCRIBER_PROMPT}\nTranscribe and analyze: {tmp_path}"
        response = agent.run(query)
        st.subheader("Meeting Analysis")
        st.write(response)

# --- EMAIL ANALYZER ---
elif page == "Email Analyzer":
    st.header("Email Analyzer")
    email_text = st.text_area("Paste email content:")
    if st.button("Analyze Email"):
        query = f"{EMAIL_ANALYZER_PROMPT}\nAnalyze this email: {email_text}"
        response = agent.run(query)
        st.subheader("Email Analysis")
        st.write(response)

# --- DASHBOARD ---
elif page == "Dashboard":
    st.header("Developer Dashboard")
    summary_query = f"{SUMMARY_PROMPT}\nSummarize recent actions."
    summary = agent.run(summary_query)
    st.subheader("Daily Summary")
    st.write(summary)
