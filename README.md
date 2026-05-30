# AI_model_safety_testing
Jakub Ledwoń, Piotr Nowak, Przemysław Bukała

## 1. Install Ollama

Install Ollama from official website or via command line
https://ollama.com

## 2. Pull

Before running inference, download the model:

```bash
ollama pull <model_name>

## 3. Run

ollama run <nazwa>

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

##5. Script

python run answerer.py
