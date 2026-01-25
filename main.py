from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import certifi

app = FastAPI()

load_dotenv(find_dotenv())
password = os.environ.get("MONGOO_PWB")

connection_string = f"mongodb+srv://majjigapuharsithreddy_db_user:{password}@data.ya5e90s.mongodb.net/"
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.recommendation_project

@app.get("/")
def Home():
    return {"message": "Server is running!"}

@app.get("/recommend_by_skills/{skills_text}")
def recommend_by_skills(skills_text: str):
    user_skills = [s.strip().title() for s in skills_text.split(',')]
    if not user_skills:
         return {"message": "No skills provided."}
    return find_projects_for_skills(user_skills, "Guest User")

def find_projects_for_skills(user_skills, user_display_name):
    all_projects = list(db.projects.find({}, {"_id": 0}))
    recommendations = []

    
    user_skills_lower = set(s.lower() for s in user_skills)

    for project in all_projects:
        project_skills = project.get("skills", [])
        
        project_skills_lower = set(s.lower() for s in project_skills)
        
        intersection = user_skills_lower.intersection(project_skills_lower)
        
        if len(project_skills_lower) > 0:
            score = len(intersection) / len(project_skills_lower)
        else:
            score = 0
        
        if score > 0:
            display_matches = [ps for ps in project_skills if ps.lower() in user_skills_lower]
            
            recommendations.append({
                "project_name": project['name'],
                "match_score": f"{score*100:.1f}%", 
                "matching_skills": display_matches
            })

    recommendations.sort(key=lambda x: float(x['match_score'].strip('%')), reverse=True)
    return {
        "user": user_display_name,
        "user_skills": user_skills,
        "recommended_projects": recommendations
    }