import json


def load_candidates(filename="candidates.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        candidates = json.loads(file.read())
        return candidates


def get_all(function):
    return function


def get_by_pk(pk):
    return load_candidates()[pk - 1]


def get_by_skill(skill_name):
    appropriate_candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            appropriate_candidates.append(candidate)
    return appropriate_candidates
