class Analyzer:

    def analyze_structure(self, tree_data):
        files = tree_data.get("tree", [])
        file_count = len(files)
        folder_count = len([f for f in files if f["type"] == "tree"])

        has_readme = any("README" in f["path"].upper() for f in files)
        has_tests = any("test" in f["path"].lower() for f in files)

        structure_score = 0
        if folder_count > 2: structure_score += 10
        if has_readme: structure_score += 10
        if has_tests: structure_score += 10

        return {
            "file_count": file_count,
            "folder_count": folder_count,
            "has_readme": has_readme,
            "has_tests": has_tests,
            "structure_score": structure_score
        }

    def analyze_commits(self, commit_list):
        commit_count = len(commit_list)
        consistent = commit_count > 10

        commit_score = 10 if consistent else 5

        return {
            "commit_count": commit_count,
            "consistent": consistent,
            "commit_score": commit_score
        }
