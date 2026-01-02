import dill
def calculate_percentage(userskills,projectskills):
    user_set=set(userskills)
    project_set=set(projectskills)
    if len(user_set)==0:
        return 0.0
    intersection=user_set.intersection(project_set)
    count=len(intersection)
    probability=count/len(project_set)
    return probability
def recommend_projects(userskills,allprojects):
    recommendations={}
    for project in allprojects:
        score=calculate_percentage(userskills,project['skills'])
        if score>0.6:
            recommendations.append({"name":project['name'],"score":score})
    recommendations.sort(key=lambda x:x['score'],reverse=True)
    return recommendations
if __name__ == "__main__":
    with open('my_recommender.pkl', 'wb') as f:
        dill.dump(recommend_projects, f)








    















