class AIWriter:

    def generate_summary(self, score, structure, commit_data):
        summary = ""

        if structure["has_readme"]:
            summary += "Good documentation present. "
        else:
            summary += "README missing. "

        if structure["has_tests"]:
            summary += "Tests available. "
        else:
            summary += "Tests missing. "

        if commit_data["consistent"]:
            summary += "Commit activity is consistent. "
        else:
            summary += "Commit activity is low. "

        return summary

    def generate_roadmap(self, structure, commit_data):
        roadmap = []

        if not structure["has_readme"]:
            roadmap.append("Add a detailed README with setup steps and screenshots.")

        if not structure["has_tests"]:
            roadmap.append("Create a /tests folder and add unit tests.")

        if commit_data["commit_count"] < 10:
            roadmap.append("Commit more frequently with meaningful messages.")

        roadmap.append("Improve folder structure for better readability.")

        return roadmap
