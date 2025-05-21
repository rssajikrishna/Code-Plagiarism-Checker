import streamlit as st
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import io

# --- App Header ---
st.title("🔍 HackerRank Plagiarism Checker")
st.markdown("Dual-mode: Upload Code OR View Simulated Contest Use Case")

# --- Mode Switcher ---
mode = st.selectbox("Choose Mode", ["Upload Code File", "Simulated Contest Data"])

# --- Similarity Functions ---
def check_similarity(codes):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(codes)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def detect_plagiarism(sim_matrix, labels, threshold=0.85):
    flagged = []
    n = len(labels)
    for i in range(n):
        for j in range(i + 1, n):
            if sim_matrix[i][j] >= threshold:
                flagged.append((labels[i], labels[j], sim_matrix[i][j]))
    return flagged

def show_heatmap(sim_matrix, labels):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(sim_matrix, xticklabels=labels, yticklabels=labels, cmap='YlOrRd', annot=True, fmt=".2f", linewidths=.5, ax=ax)
    st.pyplot(fig)

# --- Similarity Threshold ---
threshold = st.slider("🔧 Set Similarity Threshold", min_value=0.5, max_value=1.0, value=0.85, step=0.01)

# =====================
# 1️⃣ Upload Code File
# =====================
if mode == "Upload Code File":
    uploaded_files = st.file_uploader("Upload code files", accept_multiple_files=True, type=["py", "txt", "cpp", "java"])

    if uploaded_files and len(uploaded_files) > 1:
        filenames = []
        codes = []
        for file in uploaded_files:
            code = file.read().decode("utf-8")
            filenames.append(file.name)
            codes.append(code)

        st.success("Files uploaded successfully. Now comparing...")
        sim_matrix = check_similarity(codes)

        df = pd.DataFrame(sim_matrix, index=filenames, columns=filenames)
        st.subheader("🔬 Similarity Matrix")
        st.dataframe(df.style.background_gradient(cmap='YlOrRd'))

        st.subheader("📊 Heatmap View")
        show_heatmap(sim_matrix, filenames)

        plagiarized = detect_plagiarism(sim_matrix, filenames, threshold)
        if plagiarized:
            st.subheader("🚨 Potential Plagiarism Detected")
            for u1, u2, score in plagiarized:
                st.markdown(f"**{u1}** and **{u2}** → Similarity: `{score:.2f}` ❗")
        else:
            st.success("🎉 No high similarity detected. No plagiarism suspected.")

        csv = df.to_csv()
        st.download_button("Download Similarity Matrix", csv, "upload_similarity.csv", "text/csv")

    elif uploaded_files:
        st.warning("Please upload **at least 2** code files to compare.")

# ===============================
# 2️⃣ Simulated Contest Data
# ===============================
elif mode == "Simulated Contest Data":
    st.info("Fetching mock submissions from FastAPI backend...")
    response = requests.get("http://127.0.0.1:8000/submissions")

    if response.status_code == 200:
        data = response.json()
        usernames = [item['username'] for item in data]
        codes = [item['source_code'] for item in data]
        links = [item['srclink'] for item in data]

        sim_matrix = check_similarity(codes)
        df = pd.DataFrame(sim_matrix, index=usernames, columns=usernames)

        st.subheader("👨‍💻 Similarity Matrix (Mock Submissions)")
        st.dataframe(df.style.background_gradient(cmap='Blues'))

        st.subheader("📊 Heatmap View")
        show_heatmap(sim_matrix, usernames)

        plagiarized = detect_plagiarism(sim_matrix, usernames, threshold)
        if plagiarized:
            st.subheader("🚨 Potential Plagiarism Detected")
            for u1, u2, score in plagiarized:
                st.markdown(f"**{u1}** and **{u2}** → Similarity: `{score:.2f}` ❗")
        else:
            st.success("🎉 No high similarity detected. No plagiarism suspected.")

        st.subheader("📌 Submission Links")
        for i, user in enumerate(usernames):
            st.markdown(f"**{user}** → [Link]({links[i]})")

        csv = df.to_csv()
        st.download_button("Download Similarity Matrix", csv, "simulated_similarity.csv", "text/csv")

    else:
        st.error("Failed to fetch simulated data. Is your FastAPI running?")
