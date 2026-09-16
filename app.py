import requests

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def get_octocat_fact():
    response = requests.get("https://api.github.com/octocat")
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 2))
    print(get_octocat_fact())
