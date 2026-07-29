import json
from git_manager import GitManager
from explorer import RepositoryExplorer
from planner import Planner
from modifier import Modifier
repo_url = "https://github.com/callicoder/node-easy-notes-app.git"

git_manager = GitManager()

repo_path = git_manager.clone_repo(repo_url)

explorer = RepositoryExplorer(repo_path)

result = explorer.explore()

print("\n========== AI CODING AGENT REPORT ==========\n")
print("Repository:")
print(repo_url)



repository_summary = ""

for category, files in result.items():
    #print(category.upper())

    repository_summary += f"{category}:\n"

    for file in files:
        #print(f"   {file}")
        repository_summary += f" - {file}\n"

    #print()

planner = Planner()
user_request = "Improve the application so users can better organise and search their notes."
print("User Request:")
print(user_request)
plan= planner.create_plan(
    repository_summary,
    user_request
)
#print('responsefrom method',plan)
print("Feature Selected:")
print(plan["feature"])
print("Reason:")
print(plan["reason"])
print("Files Modified:")

#print("\n========== EXECUTION PLAN ==========\n")
#print(plan)
modifier = Modifier()
for file in plan["files_to_modify"]:          
    modifier.modify_file(repo_path / file,plan,user_request)
print("Steps:")
i=1
for step in plan["steps"]:
    print(i,".",step)
    i+=1
    
