from pathlib import Path


class RepositoryExplorer:
    IGNORE_DIRS = {
        ".git",
        "node_modules",
        "__pycache__",
        ".idea",
        ".vscode",
        "dist",
        "build"
    }

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)

    def explore(self):
        important_files = {
            "entry_points": [],
            "models": [],
            "controllers": [],
            "routes": [],
            "configs": [],
            "package": []
        }

        for path in self.repo_path.rglob("*"):
            if any(part in self.IGNORE_DIRS for part in path.parts):
                continue

            if not path.is_file():
                continue
            relative = path.relative_to(self.repo_path)

            # package.json
            if path.name == "package.json":
                important_files["package"].append(relative)

            # server.js or app.js
            elif path.name in ["server.js", "app.js", "index.js"]:
                important_files["entry_points"].append(relative)

            # folders
            elif "models" in path.parts:
                important_files["models"].append(relative)

            elif "controllers" in path.parts:
                important_files["controllers"].append(relative)

            elif "routes" in path.parts:
                important_files["routes"].append(relative)

            elif "config" in path.parts:
                important_files["configs"].append(relative)

        return important_files

    def print_tree(self):
        for path in sorted(self.repo_path.rglob("*")):

            if any(part in self.IGNORE_DIRS for part in path.parts):
                continue

            print(path.relative_to(self.repo_path))
