from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os

from logic import calculate_percentage

app = FastAPI()
load_dotenv(find_dotenv())
password = os.environ.get("MONGOO_PWB")
connection_string = f"mongodb+srv://majjigapuharsithreddy_db_user:{password}@data.ya5e90s.mongodb.net/"
client = MongoClient(connection_string)

db = client.recommendation_project

@app.get("/")
def Home():
    return {"message": "Server is running! Go to /docs to test the API."}

@app.get("/recommend/{user_name}")
def get_recommendations(user_name: str):
    user=db.users.find_one({"name":user_name})
    if not user:
        raise HTTPException(status_code=404, detail=f"User '{user_name}' not found.")
    user_skills=user.get("skills",[])
    if not user_skills:
        return{
            "user":user_name,
            "message": "No skills found for the user."
        }
    all_projects = list(db.projects.find({}, {"_id": 0}))
    recommendations = []
    for project in all_projects:
        project_skills = project.get("skills", [])
        score = calculate_percentage(user_skills, project_skills)
        if score > 0:
            recommendations.append({
                "project_name": project['name'],
                "match_score": f"{score*100:.1f}%", # Convert 0.75 -> "75.0%"
                "matching_skills": list(set(user_skills).intersection(set(project_skills)))
            })
    recommendations.sort(key=lambda x: float(x['match_score'].strip('%')), reverse=True)
    
    return {
        "user": user_name,
        "user_skills": user_skills,
        "recommended_projects": recommendations
    }



