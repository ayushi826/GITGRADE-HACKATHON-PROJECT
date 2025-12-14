class Scorer:

    def calculate_final_score(self, structure, commit_data, languages):
        score = 0
        
        score += structure["structure_score"]               # 30 points
        score += commit_data["commit_score"]                # 10 points

        if len(languages) > 0:
            score += 10                                    # language diversity

        if structure["has_tests"]:
            score += 20

        if structure["has_readme"]:
            score += 30

        return min(score, 100)

    def level(self, score):
        if score >= 80:
            return "Advanced"
        elif score >= 50:
            return "Intermediate"
        return "Beginner"
