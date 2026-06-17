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

- `gemma3:4b`
- `gemma3:12b`
- `phi4:14b`
- `llama3.1:8b`
- `deepseek-r1:8b`
- `tinyllama:1.1b`

## 5. Datasets
All avilable datasets are derivative of the CoCoNot dataset available here: https://huggingface.co/datasets/allenai/coconot/
The datasets are structured in a .jsonl format

- `coconot_original_all`: The original dataset, containing 12478 prompts with their classes
- `coconot_original_pl`: The original dataset translated into polish for comparison purposes (translation model used: facebook/nllb-200-distilled-600M)
- `coconot_eng_trimmed`: A reduced dataset containing 1002 prompts from the oiginal with the class ratio remaining the same
- `coconot_pl_trimmed`: As above, but for the translated dataset

- `coconot_trimmed_corrected_eng`: The trimmed English dataset with corrected prompts distro(including subcategory stratificatiobn)
- `coconot_trimmed_corrected_pl`: The trimmed Polish dataset with corrected prompts distro

The purpose of introducing trimmed versions was to limit the load on the testing process (it may be that we don't have enough computational power to analyse that amount of models and judge them on datasets of 12478 prompts).

## 6. Script
### answerer.py
Skrypt służy do generowania odpowiedzi dla zestawu promptów przy użyciu wybranego modelu językowego.
```bash
python run answerer.py
```
Na początku skryptu znajduje się zmienna:
MODEL = "..."
Należy w niej podać nazwę modelu z dostępnych (Models).
W kodzie maina znajduje się zmienna:
out_file = "..."
Należy w niej podać nazwę pliku wyjściowego dla odpowiedzi modelu.

Należy również upewnić się, że poprawna jest nazwa pliku wejściowego oraz prompt (czy zgadza się język).
### judgement.py
Skrypt służy do analizy wyników klasyfikacji zapisanych w plikach znajdujących się w katalogu judgements.
```bash
python run judgement.py
```
Na początku skryptu znajduje się zmienna:
in_file = "..."
Należy w niej podać ścieżkę do analizowanego pliku z katalogu judgements.

