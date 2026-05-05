import requests
import json
import os

LEETCODE_API = "https://leetcode.com/api/problems/all/"

def fetch_problems():
    response = requests.get(LEETCODE_API)
    data = response.json()
    return data["stat_status_pairs"]

def save_problems(problems):
    os.makedirs("leetcode", exist_ok=True)

    solved = [p for p in problems if p["status"] == "ac"]

    with open("leetcode/solved.json", "w") as f:
        json.dump(solved, f, indent=2)

if __name__ == "__main__":
    problems = fetch_problems()
    save_problems(problems)
