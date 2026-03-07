import json
import os

SCORE_FILE = "data/scores.json"

def load_scores():

    if not os.path.exists(SCORE_FILE):
        return {}

    with open(SCORE_FILE) as f:
        return json.load(f)

def save_scores(scores):

    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def update_score(username, score):

    scores = load_scores()

    if username not in scores:
        scores[username] = []

    scores[username].append(score)

    save_scores(scores)

    print("Score saved:", score)
