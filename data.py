from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())
password = os.environ.get("MONGOO_PWB")
connection_string = f"mongodb+srv://majjigapuharsithreddy_db_user:XzaxXuZBdOFMVlYn@data.ya5e90s.mongodb.net/"
client = MongoClient(connection_string)
db = client.recommendation_project
projects_collection = db.projects

def insert_projects_with_loop():
    project_names = [
        "AI Customer Support Chatbot",
        "E-Commerce Website Frontend",
        "Stock Market Predictor",
        "Employee Management System",
        "Portfolio Website",
        "Android Fitness App",
        "Data Visualization Dashboard",
        "Blockchain Voting System",
        "Social Media Backend API",
        "Weather Forecasting Tool",
        "Automated Email Script",
        "IOS To-Do List",
        "Cybersecurity Network Scanner",
        "Machine Learning Image Classifier",
        "Real-time Chat App"
    ]

    skills_list = [
        ["Python", "NLP", "TensorFlow", "MongoDB"],
        ["HTML", "CSS", "JavaScript", "React"],
        ["Python", "Pandas", "Scikit-Learn", "Matplotlib"],
        ["Java", "Spring Boot", "MySQL", "Hibernate"],
        ["HTML", "CSS", "Bootstrap"],
        ["Kotlin", "Android Studio", "Firebase", "XML"],
        ["Python", "Streamlit", "SQL", "Plotly"],
        ["Solidity", "Ethereum", "JavaScript", "Web3.js"],
        ["Node.js", "Express", "MongoDB", "JWT"],
        ["Python", "APIs", "JSON", "Tkinter"],
        ["Python", "SMTP", "Scripting"],
        ["Swift", "iOS", "CoreData"],
        ["Python", "Networking", "Linux", "Wireshark"],
        ["Python", "PyTorch", "OpenCV", "Deep Learning"],
        ["JavaScript", "Socket.io", "Node.js", "HTML"]
    ]

    docs_to_insert = []
    for name, skills in zip(project_names, skills_list):
        project_document = {
            "name": name,
            "skills": skills
        }
        docs_to_insert.append(project_document)

    projects_collection.delete_many({}) 
    result = projects_collection.insert_many(docs_to_insert)
    print(f"Success! Inserted {len(result.inserted_ids)} projects into the database")

if __name__ == "__main__":
    insert_projects_with_loop()

