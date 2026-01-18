from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import certifi  # Needed for the SSL fix

# Import your logic function
from logic import calculate_percentage

# 1. SETUP - This must happen BEFORE any @app functions
app = FastAPI()

load_dotenv(find_dotenv())
password = os.environ.get("MONGOO_PWB")

# Database Connection
connection_string = f"mongodb+srv://majjigapuharsithreddy_db_user:{password}@data.ya5e90s.mongodb.net/"
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.recommendation_project

# 2. ROUTES
@app.get("/")
def Home():
    return {"message": "Server is running! Go to /docs to test the API."}

# Route A: Recommend by Name (The one we built first)
@app.get("/recommend/{user_name}")
def get_recommendations(user_name: str):
    user = db.users.find_one({"name": user_name})
    if not user:
        raise HTTPException(status_code=404, detail=f"User '{user_name}' not found.")
    
    user_skills = user.get("skills", [])
    
    # Re-use the helper function below to avoid duplicate code
    return find_projects_for_skills(user_skills, user_name)

# Route B: Recommend by Skills (The NEW one you wanted)
@app.get("/recommend_by_skills/{skills_text}")
def recommend_by_skills(skills_text: str):
    # Convert "Python, sql" -> ["Python", "SQL"]
    user_skills = [s.strip().title() for s in skills_text.split(',')]
    
    if not user_skills:
         return {"message": "No skills provided."}

    # Use the same logic helper
    return find_projects_for_skills(user_skills, "Guest User")

# 3. LOGIC HELPER (Keeps code clean)
def find_projects_for_skills(user_skills, user_display_name):
    all_projects = list(db.projects.find({}, {"_id": 0}))
    recommendations = []

    for project in all_projects:
        project_skills = project.get("skills", [])
        score = calculate_percentage(user_skills, project_skills)
        
        if score > 0:
            recommendations.append({
                "project_name": project['name'],
                "match_score": f"{score*100:.1f}%", 
                "matching_skills": list(set(user_skills).intersection(set(project_skills)))
            })

    recommendations.sort(key=lambda x: float(x['match_score'].strip('%')), reverse=True)
    
    return {
        "user": user_display_name,
        "user_skills": user_skills,
        "recommended_projects": recommendations
    }