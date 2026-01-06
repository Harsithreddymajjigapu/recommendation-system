# logic.py - THE CLEAN VERSION

def calculate_percentage(userskills, projectskills):
    # Convert to sets to do math easily
    user_set = set(userskills)
    project_set = set(projectskills)
    
    # 1. Safety check: If project has NO skills, match is 0%
    if len(project_set) == 0: 
        return 0.0
    
    # 2. Find matching skills
    intersection = user_set.intersection(project_set)
    
    # 3. Calculate percentage (Matches / Total Needed)
    return len(intersection) / len(project_set)