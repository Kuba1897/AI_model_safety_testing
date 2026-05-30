import requests, json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:4b"

def ask(model: str, system: str, user: str, temperature: float = 0.0) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "options": {"temperature": temperature,},
        "keep_alive": 0,
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=600)
    return resp.json()["message"]["content"]

if __name__ == "__main__":
    #for test purposes capping at 10
    i = 1
    out_file = f"results/coconot_answers_{MODEL.replace(':','_')}.jsonl"
    with open(out_file, 'w', encoding="utf-8") as fout, open("coconot_original_all.jsonl",'r', encoding="utf-8") as fin:
        for line in fin:
            obj = json.loads(line)
            response = ask(MODEL, "Answer in english. Keep your answers relatively simple.", obj["prompt"])
            print(response)
            obj["response"] = response

            fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

            print(i)
            i+=1
            if i>9:
                break