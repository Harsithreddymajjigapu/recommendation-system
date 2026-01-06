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

def Home():
    return {"message": "Server is running! Go to /docs to test the API."}
def get_recommendations(user_skills: str):
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



