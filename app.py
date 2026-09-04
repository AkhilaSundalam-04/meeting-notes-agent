import streamlit as st

from utils.summarizer import generate_summary
from utils.extractor import extract_action_items

# Page Configuration
st.set_page_config(
    page_title="Meeting Notes Agent",
    page_icon="📝",
    layout="centered"
)

# App Title
st.title("📝 Meeting Notes Agent")

# File Upload
uploaded_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt"]
)

if uploaded_file is not None:

    # Read file content
    text = uploaded_file.read().decode("utf-8")

    st.success("Transcript processed successfully!")

    # Display Transcript
    st.subheader("📄 Transcript")
    st.write(text)

    # Generate Summary
    summary = generate_summary(text)

    st.subheader("📌 Meeting Summary")
    st.write(summary)

    # Extract Action Items
    action_items = extract_action_items(text)

    # Statistics
    st.metric(
        label="Total Action Items",
        value=len(action_items)
    )

    st.subheader("✅ Action Items")

    # Convert List to DataFrame
    action_df = pd.DataFrame(
        action_items,
        columns=["Action Item"]
    )

    # Start numbering from 1
    action_df.index = action_df.index + 1

    # Display Table
    st.table(action_df)

    # CSV Download
    csv = action_df.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="action_items.csv",
        mime="text/csv"
    )