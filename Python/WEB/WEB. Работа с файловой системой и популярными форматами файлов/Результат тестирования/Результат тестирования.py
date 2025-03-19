import json
import sys


with open("scoring.json", "r", encoding="utf-8") as file:
    scoring_data = json.load(file)["scoring"]

test_points = {}
for group in scoring_data:
    points_per_test = group["points"] / len(group["required_tests"])
    for test in group["required_tests"]:
        test_points[test] = points_per_test

verdicts = sys.stdin.readlines()

result = 0
for i, verdict in enumerate(verdicts, start=1):
    if verdict.rstrip('\n') == "ok" and i in test_points:
        result += test_points[i]

print(int(result))
