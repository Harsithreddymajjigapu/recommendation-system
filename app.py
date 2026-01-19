import streamlit as st
import requests

st.set_page_config(page_title="Skill Matcher AI", page_icon="🤖")

st.title("🤖 AI Project Recommender")
st.markdown("Type your skills below to find the perfect project match.")

skills_input = st.text_input("Enter your skills (comma separated):", placeholder="e.g. Python, React, SQL")

if st.button("Find Matches 🔍", type="primary"):
    if skills_input:
        with st.spinner("Analyzing your skills..."):
            try:
                api_url = f"http://127.0.0.1:8000/recommend_by_skills/{skills_input}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    data = response.json()
                    
                    st.success(f" Analyzing for: **{', '.join(data['user_skills'])}**")
                    st.markdown("---")
                    
                    if not data['recommended_projects']:
                        st.warning("No matching projects found. Try adding more skills!")
                    else:
                        st.subheader(f" Top Recommended Projects")
                        
                        for project in data['recommended_projects']:
                            score_text = project['match_score']
                            score_float = float(score_text.strip('%')) / 100
                            
                            with st.expander(f" {project['project_name']} ({score_text} Match)", expanded=True):
                                col1, col2 = st.columns([3, 1])
                                with col1:
                                    st.write(f"**Matches:** {', '.join(project['matching_skills'])}")
                                    st.progress(score_float)
                                with col2:
                                    st.metric(label="Score", value=score_text)
                else:
                    st.error("Error communicating with the backend.")

            except requests.exceptions.ConnectionError:
                st.error(" Could not connect to the Server. Is uvicorn running?")
    else:
        st.warning(" Please type some skills first.")