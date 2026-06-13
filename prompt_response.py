import sys
import fileinput as fi
import json

res_name = sys.argv[2]
judg_name = sys.argv[2]

if sys.argv[2] == "deepseek":
    res_name = "deepseek-r1_8b"
    judg_name = "deepseek1_1"

if sys.argv[2] == "llama":
    res_name = "llama3.1_8b"
    judg_name = "llama3_8b"

if sys.argv[2] == "tinyllama":
    res_name = "tinyllama_11b"
    judg_name = "tinyllama"

with open(f"judgements/{judg_name}_{sys.argv[1]}_judgement.txt", 'r', encoding="utf-8") as f:
    data = json.load(f)

i = 0
with open(f"results/coconot_answers_{sys.argv[1]}_{res_name}.jsonl", 'r', encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        if obj["id"] == sys.argv[3]:
            print("Prompt:\n "+obj["prompt"])
            print("-----------------------")
            print("Response:\n "+obj["response"])
            print("---------------------")
            print("Klasyfikacja:\n")
            print(data[i])
            break
        else:
            i += 1
        