def calculate_percentage(userskills, projectskills):
    user_set = set(userskills)
    project_set = set(projectskills)
    if len(project_set) == 0: 
        return 0.0
    
    intersection = user_set.intersection(project_set)

    return len(intersection) / len(project_set)
