import os

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            if not content:
                # If folder is empty, create a placeholder file
                with open(os.path.join(path, ".gitkeep"), 'w') as f:
                    pass
            else:
                create_structure(path, content)
        else:
            # Create file and write content (empty string if no content)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)

# Define the folder and file structure
structure = {
    "op-monitoring-app": {
        "backend": {
            "app": {
                "main.py": "",
                "routes": {
                    "__init__.py": "",
                    "monitoring.py": "",
                    "reports.py": ""
                },
                "services": {
                    "dynatrace_service.py": "",
                    "op_service.py": ""
                }
            },
            "requirements.txt": ""
        },
        "frontend": {
            "public": {},  # empty folder, we'll create a `.gitkeep`
            "src": {
                "components": {
                    "Navbar.jsx": "",
                    "HomePage.jsx": ""
                },
                "App.jsx": "",
                "index.js": ""
            },
            "package.json": ""
        },
        "README.md": ""
    }
}

if __name__ == "__main__":
    base_path = "."  # Current directory
    create_structure(base_path, structure)
    print("Folder structure created successfully!") 