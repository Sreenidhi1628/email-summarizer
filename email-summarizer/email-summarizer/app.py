import streamlit as st
from summarizer import summarize_email

# Page config
st.set_page_config(
    page_title="Email Summarizer",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 Email Summarizer")
st.write("Paste your email below and get a quick, clear summary!")

st.divider()

# Input
email_input = st.text_area(
    "📩 Paste your email here:",
    height=250,
    placeholder="Dear John, I wanted to follow up on our meeting last week..."
)

# Word count
if email_input:
    word_count = len(email_input.split())
    st.caption(f"Word count: {word_count}")

st.divider()

# Summary length option
summary_length = st.radio(
    "Summary Length:",
    ["Short", "Medium", "Detailed"],
    horizontal=True
)

# Summarize button
if st.button("✨ Summarize Email", use_container_width=True):
    if email_input.strip() == "":
        st.warning("⚠️ Please paste an email first!")
    else:
        with st.spinner("Summarizing your email..."):
            try:
                summary = summarize_email(email_input, summary_length)
                st.success("✅ Summary Ready!")
                st.divider()
                st.subheader("📋 Summary")
                st.write(summary)

                # Copy button
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="email_summary.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Check your API key in the .env file")

st.divider()
st.caption("Built with Streamlit & Gemini AI")