import shutil
import subprocess
from pathlib import Path


class GitManager:

    def __init__(self, workspace="workspace"):
        self.workspace = Path(workspace)

    def clone_repo(self, repo_url):
        # Delete existing workspace if it exists
        if self.workspace.exists():
            shutil.rmtree(self.workspace)

        print(f"Cloning {repo_url}...")

        subprocess.run(
            ["git", "clone", repo_url, str(self.workspace)],
            check=True
        )

        print("Repository cloned successfully!")

        return self.workspace