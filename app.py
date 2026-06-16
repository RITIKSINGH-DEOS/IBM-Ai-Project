import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os



load_dotenv()



genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

#Page Config

st.set_page_config(
    page_title="AI Content Creator Assistant",
    page_icon="🎬",
    layout="wide"
)

#Sidebar Navigation

st.sidebar.title("📂 Navigation")


page = st.sidebar.radio(
    "Select Feature",
    [
        "Script Generator",
        "Description Generator",
        "Hashtag Generator",
        "Thumbnail Analyzer"
    ]
)

#Script Generator

if page == "Script Generator":

    st.title("🎬 AI Content Creator Assistant")

    st.write("Generate professional YouTube scripts using AI.")

    topic = st.text_input(
        "Enter Video Topic"
    )

    video_length = st.selectbox(
        "Video Length",
        [
            "30 Seconds",
            "45 Seconds",
            "60 Seconds",
            "2 Minutes",
            "3 Minutes",
            "5 Minutes",
            "8 Minutes",
            "10 Minutes",
            "Custom"
        ]
    )

    custom_length = ""

    if video_length == "Custom":
        custom_length = st.text_input(
            "Enter Custom Duration",
            placeholder="Example: 90 seconds, 7 minutes"
        )

    if video_length in ["30 Seconds", "45 Seconds", "60 Seconds"]:
        content_type = "YouTube Short"
    else:
        content_type = "YouTube Long Video"

    st.success(f"Content Type: {content_type}")

    audience = st.text_input(
        "Target Audience",
        placeholder="Example: Students, Car Enthusiasts, History Lovers, Investors"
    )

    language = st.selectbox(
        "Script Language",
        [
            "English",
            "Hinglish"
        ]
    )

    if st.button("Generate Script"):

        final_duration = custom_length if video_length == "Custom" else video_length

        if not topic:
            st.warning("Please enter a topic.")
            st.stop()

        if not audience:
            st.warning("Please enter target audience.")
            st.stop()

        if video_length == "Custom" and not custom_length:
            st.warning("Please enter custom duration.")
            st.stop()

        prompt = f"""
You are a professional YouTube content strategist and script writer.

Create a high-retention YouTube script.

TOPIC:
{topic}

VIDEO DURATION:
{final_duration}

CONTENT TYPE:
{content_type}

TARGET AUDIENCE:
{audience}

LANGUAGE:
{language}

IMPORTANT RULES:

- Stay strictly focused on the provided topic.
- Do not change the topic.
- Do not assume a different angle.
- If the topic is unclear, interpret it literally.
- Generate the script only around the exact topic given by the user.

30 Seconds = Maximum 75 words
45 Seconds = Maximum 110 words
60 Seconds = Maximum 150 words
2 Minutes = 300 words
3 Minutes = 450 words
5 Minutes = 700 words
8 Minutes = 1000 words
10 Minutes = 1300 words

If language is Hinglish:
- Generate ONLY Hinglish
- No English translations

If language is English:
- Generate only English

Generate output in this format:

# Title

# Hook

# Full Script

# CTA
"""

        with st.spinner("Generating Script..."):

            response = model.generate_content(prompt)

            st.markdown(response.text)

#Thumbnail Analyzer

if page == "Thumbnail Analyzer":

    st.title("🖼️ Thumbnail Analyzer")


    uploaded_image = st.file_uploader(
        "Upload Thumbnail",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image is not None:

        image = Image.open(uploaded_image)

        st.image(
            image,
            caption="Uploaded Thumbnail",
            use_container_width=True
        )

        if st.button("Analyze Thumbnail"):

            with st.spinner("Analyzing Thumbnail..."):

                prompt = f"""
You are a professional YouTube growth expert.

Analyze this YouTube thumbnail.

FIRST provide ratings in table format:

Overall Score: X/10
Text Readability: X/10
Color Contrast: X/10
Attention Grabbing: X/10
CTR Potential: High / Medium / Low

Then provide:

# Strengths

# Weaknesses

# Improvement Suggestions

Give 3 practical suggestions to improve CTR.

Keep response concise and practical.
"""

                try:

                    response = model.generate_content(
                        [prompt, image]
                    )

                    st.markdown(response.text)

                except Exception as e:

                    st.error(f"Error: {str(e)}")


                   
                   
#Description Generator

if page == "Description Generator":

    st.title("📝 Description Generator")

    description_topic = st.text_input(
        "Enter Video Topic"
    )

    if st.button("Generate Description"):

        if not description_topic:

            st.warning("Please enter a topic.")

        else:

            with st.spinner("Generating Description..."):

                prompt = f"""
You are a professional YouTube SEO expert and content strategist.

Generate a highly engaging, SEO-optimized YouTube description.

Video Topic:
{description_topic}

Requirements:

1. Start with a strong attention-grabbing hook.
2. Write like a real YouTube creator, not like an article.
3. Keep the tone engaging, conversational, and audience-focused.
4. Naturally include important SEO keywords related to the topic.
5. Include a clear Call To Action (Like, Comment, Subscribe).
6. Keep the description between 120 and 180 words.
7. Avoid keyword stuffing.
8. Make it ready to copy-paste directly into YouTube.
9. Generate 10 highly relevant hashtags.
10. Put each hashtag on a separate line.

Format EXACTLY like this:

📌 Description

(SEO optimized description)

🔍 Keywords

(keyword1, keyword2, keyword3, keyword4, keyword5)

 Hashtags

#Hashtag1
#Hashtag2
#Hashtag3
#Hashtag4
#Hashtag5
#Hashtag6
#Hashtag7
#Hashtag8
#Hashtag9
#Hashtag10

Return only the final result. Do not include explanations or notes.

"""

                try:

                    response = model.generate_content(prompt)

                    st.markdown(response.text)

                except Exception as e:

                    st.error(f"Error: {str(e)}")


#Hashtag Generator

if page == "Hashtag Generator":

    st.title("🏷️ Hashtag Generator")

    hashtag_topic = st.text_input(
        "Enter Topic For Hashtags"
    )

    if st.button("Generate Hashtags"):

        if not hashtag_topic:

            st.warning("Please enter a topic.")

        else:

            with st.spinner("Generating Hashtags..."):

                prompt = f"""
Generate 20 viral YouTube hashtags for:

{hashtag_topic}

Rules:

- Return only hashtags
- No explanations
- No numbering
- Mix broad and niche hashtags
- Suitable for YouTube SEO
"""

                try:

                    response = model.generate_content(prompt)

                    st.markdown(response.text)

                except Exception as e:

                    st.error(f"Error: {str(e)}")            