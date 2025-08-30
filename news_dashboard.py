import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
from dotenv import load_dotenv

#upload API Key
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

st.title("📰 News Dashboard")

# usre inputs
keyword = st.text_input("Enter a keyword:", value="technology")
country = st.text_input("Enter country code (us, gb, eg):", value="us")

# Get news button
if st.button("Fetch News"):
    url = "https://newsapi.org/v2/top-headlines"
    params = {"q": keyword, "country": country, "apiKey": api_key}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        if articles:
            # DataFrame
            df = pd.DataFrame([{
                "Title": a["title"],
                "Source": a["source"]["name"],
                "Author": a["author"],
                "PublishedAt": a["publishedAt"],
                "URL": a["url"],
                "Description": a["description"]
            } for a in articles])
            
            st.success(f"{len(df)} articles fetched successfully!")

            # --- Save to CSV ---
            filename = f"news_{keyword}_{country}.csv"
            df.to_csv(filename, index=False, encoding="utf-8")
            st.info(f"✅ Data saved to {filename}")

            # --- Show data---
            st.subheader("📝 Top Headlines")
            st.dataframe(df[["Title", "Source", "URL"]])

            # --- Bar Chart ---
            st.subheader("📊 Articles per Source (Bar Chart)")
            st.bar_chart(df["Source"].value_counts())

            # --- Pie Chart ---
            st.subheader("📊 Articles per Source (Pie Chart)")
            source_counts = df["Source"].value_counts()
            plt.figure(figsize=(6,6))
            plt.pie(source_counts, labels=source_counts.index, autopct='%1.1f%%', startangle=140)
            st.pyplot(plt)

            # --- Word Cloud ---
            st.subheader("☁️ Word Cloud of Headlines")
            text = " ".join(df["Title"].dropna())
            if text:
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
                st.image(wordcloud.to_array())
            else:
                st.info("No headlines to generate Word Cloud")
