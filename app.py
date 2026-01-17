import streamlit as st
import requests

# 1. Configure the Page
st.set_page_config(
    page_title="Skill Matcher AI",
    page_icon="🤖",
    layout="centered"
)

# 2. Title and Description
st.title("🤖 AI Project Recommender")
st.markdown("Enter a developer's name to find the **perfect** project match based on their skills.")

# 3. Input Section
with st.container():
    user_name = st.text_input("👤 Enter Developer Name:", placeholder="e.g. Harsith Developer")
    search_button = st.button("Find Matches 🔍", type="primary")

# 4. Logic: What happens when you click the button
if search_button:
    if user_name:
        with st.spinner(f"Analyzing skills for {user_name}..."):
            try:
                # ---------------------------------------------------------
                # CONNECT TO YOUR BACKEND API HERE
                # ---------------------------------------------------------
                # This line sends the name to your FastAPI server
                api_url = f"http://127.0.0.1:8000/recommend/{user_name}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    data = response.json()
                    
                    # --- SECTION 1: USER INFO ---
                    st.success(f"User Found: **{data['user']}**")
                    st.write("🛠️ **Skills identified:**")
                    
                    # Display skills as little tags
                    skill_html = ""
                    for skill in data['user_skills']:
                        skill_html += f"<span style='background-color:#e0f7fa; color:#006064; padding:5px 10px; border-radius:5px; margin-right:5px;'>{skill}</span>"
                    st.markdown(skill_html, unsafe_allow_html=True)
                    
                    st.markdown("---")
                    st.subheader(f"🎯 Top Recommended Projects")

                    # --- SECTION 2: PROJECTS ---
                    for project in data['recommended_projects']:
                        # Calculate the number for the progress bar (50% -> 0.5)
                        score_text = project['match_score']  # "50.0%"
                        score_float = float(score_text.strip('%')) / 100
                        with st.expander(f"📌 {project['project_name']} ({score_text} Match)", expanded=True):
                            
                            col1, col2 = st.columns([3, 1])
                            
                            with col1:
                                st.write("**Why this matches:**")
                                st.write(f"You have: {', '.join(project['matching_skills'])}")
                                st.progress(score_float)
                            
                            with col2:
                                st.metric(label="Match Score", value=score_text)

                else:
                    st.error(" User not found in the database.")
                    st.info("Try adding the user via your seed_data.py script first.")

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the Server.")
                st.warning("Is your FastAPI backend running? Run 'uvicorn main:app' in a separate terminal.")
    else:
        st.warning(" Please enter a name first.")