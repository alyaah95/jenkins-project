import json
def format_data(name, role):
    return json.dumps({"name": name, "role": role, "status": "active"})
if __name__ == "__main__":
    print(format_data("Alyaa", "Data Engineer"))
