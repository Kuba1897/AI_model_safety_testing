# AI_model_safety_testing
Jakub Ledwoń, Piotr Nowak, Przemysław Bukała

## 1. Install Ollama

Install Ollama from official website or via command line
https://ollama.com

## 2. Pull

Before running inference, download the model:

```bash
ollama pull <model_name>
```

## 3. Run

```bash
ollama run <nazwa>
```

## 4. Models
All models listed below are compatible with Ollama:

- `qwen3:8b`
- `gemma3:4b`
- `gemma3:12b`
- `phi4:14b`
- `llama3.1:8b`
- `llama3.3:70b`
- `deepseek-r1:8b`
- `tinyllama:1.1b`
- `gemma2:2b`
- `phi3:mini-4k`
- `qwen2.5:3b-instruct`

## 5. Datasets
All avilable datasets are derivative of the CoCoNot dataset available here: https://huggingface.co/datasets/allenai/coconot/
The datasets are structured in a .jsonl format

- `coconot_original_all`: The original dataset, containing 12478 prompts with their classes
- `coconot_original_pl`: The original dataset translated into polish for comparison purposes (translation model used: facebook/nllb-200-distilled-600M)
- `coconot_eng_trimmed`: A reduced dataset containing 1002 prompts from the oiginal with the class ratio remaining the same
- `coconot_pl_trimmed`: As above, but for the translated dataset

The puropse of introducing trimmed versions was to limit the load on the testing process (It may be possible we don't have enough computational power to analyse 6 models and judge them on 2 datasets of 12478 prompts).

## 6. Script

```bash
python run answerer.py
```
