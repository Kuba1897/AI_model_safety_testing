import requests, json
import time

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "deepseek-r1:8b"

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

    # i = 1
    # out_file = f"results/coconot_answers_{MODEL.replace(':','_')}.jsonl"
    # with open(out_file, 'w', encoding="utf-8") as fout, open("coconot_trimmed_corrected_eng.jsonl",'r', encoding="utf-8") as fin:
    #     for line in fin:
    #         obj = json.loads(line)
    #         response = ask(MODEL, "Answer briefly in English.", obj["prompt"]) #"Odpowiadaj zwięźle po Polsku."

    #         obj["response"] = response

    #         fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

    #         print(i)
    #         i+=1
    i = 1
    out_file = f"results/coconot_answers_pl_{MODEL.replace(':','_')}.jsonl"
    with open(out_file, 'w', encoding="utf-8") as fout, open("coconot_trimmed_corrected_pl.jsonl",'r', encoding="utf-8") as fin:
        for line in fin:
            obj = json.loads(line)
            response = ask(MODEL, "Odpowiadaj zwięźle po Polsku.", obj["prompt"]) #"Odpowiadaj zwięźle po Polsku."

            obj["response"] = response

            fout.write(json.dumps(obj, ensure_ascii=False) + '\n')

            print(i)
            i+=1

    #end_all = time.perf_counter()
    #print(f"Total time: {end_all - start_all:.2f} seconds")

# import requests, json
# import time

# OLLAMA_URL = "http://localhost:11434/api/chat"
# MODEL = "deepseek-r1:8b"

# START_FROM = 552  # liczba już przetworzonych rekordów

# def ask(model: str, system: str, user: str, temperature: float = 0.0) -> str:
#     payload = {
#         "model": model,
#         "messages": [
#             {"role": "system", "content": system},
#             {"role": "user", "content": user},
#         ],
#         "stream": False,
#         "options": {"temperature": temperature},
#         "keep_alive": 0,
#     }

#     resp = requests.post(OLLAMA_URL, json=payload, timeout=600)
#     return resp.json()["message"]["content"]


# if __name__ == "__main__":
#     start_all = time.perf_counter()

#     out_file = f"results/coconot_answers_{MODEL.replace(':','_')}.jsonl"

#     with open(out_file, "a", encoding="utf-8") as fout, \
#          open("coconot_original_all.jsonl", "r", encoding="utf-8") as fin:

#         for idx, line in enumerate(fin):

#             if idx < START_FROM:
#                 continue

#             obj = json.loads(line)

#             response = ask(
#                 MODEL,
#                 "Answer in english. Keep your answers relatively simple.",
#                 obj["prompt"]
#             )

#             print(response)

#             obj["response"] = response

#             fout.write(json.dumps(obj, ensure_ascii=False) + "\n")
#             fout.flush()  # zapisuj od razu na dysk

#             print(f"Processed: {idx + 1}")

#     end_all = time.perf_counter()
#     print(f"Total time: {end_all - start_all:.2f} seconds")