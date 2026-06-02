import requests, json
import time

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:12b"

def ask(model: str, system: str, user: str, temperature: float = 0.0) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "options": {"temperature": temperature,},
        "keep_alive": "10m",
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=600)
    return resp.json()["message"]["content"]

if __name__ == "__main__":
    #start_all = time.perf_counter()

    i = 1
    out_file = f"results/coconot_answers_{MODEL.replace(':','_')}.jsonl"
    with open(out_file, 'w', encoding="utf-8") as fout, open("coconot_eng_trimed.jsonl",'r', encoding="utf-8") as fin:
        for line in fin:
            obj = json.loads(line)
            response = ask(MODEL, "Answer briefly in English.", obj["prompt"])

            obj["response"] = response

            fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

            print(i)
            i+=1

    #end_all = time.perf_counter()
    #print(f"Total time: {end_all - start_all:.2f} seconds")