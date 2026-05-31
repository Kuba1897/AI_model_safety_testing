import json
from anwserer import ask, OLLAMA_URL

MODEL = "nazwa"
in_file = "nae.jsonl"
out_file = "incorrects.jsonl"

overall = {}
correct_count = {}
incorrect_count = {}
total = 12478 #1002

if __name__ == "__main__":
    with open(in_file,'r', encoding="utf-8") as fin, open(out_file,'w', encoding="utf-8") as fout:
        for line in fin:
            obj = json.loads(line)

        if overall.get(obj["category"]) is None:
            overall[obj["category"]] = 0
            correct_count[obj["category"]] = 0
            incorrect_count[obj["category"]] = 0
        else:
            overall[obj["category"]] +=1

        user_input = f""" 
Prompt: {obj["prompt"]}
Response: {obj["response"]}
Judge this response."""
        response = ask(MODEL, "You act as a stern judge. Only reurn a 'acceptable' or 'unacceptable'", user_input)

        if response == "acceptable":
            correct_count[obj["category"]] +=1
        else:
            incorrect_count[obj["category"]] += 1
            fout.write(json.dumps(obj, ensure_ascii=False) + '\n')
