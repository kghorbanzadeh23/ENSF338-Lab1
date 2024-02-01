import json

if __name__ == "__main__":
    with open("large-file.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        i["payload"]["size"] = 35
        
    with open("output.2.3.json", "w") as of:
        json.dump(data[::-1],of, indent=4)
