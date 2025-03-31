# 🌍 Multi-Language AI Translator (HuggingFace Transformers)

This command-line application uses [HuggingFace Transformers](https://huggingface.co/docs/transformers/) to provide fast and accurate language translation between multiple language pairs using pretrained MarianMT models.

---

## 🚀 Features

- Translate text interactively between language pairs
- Supports switching languages during runtime
- Uses high-quality pretrained MarianMT models from Helsinki-NLP
- Easy-to-run Python script

---

## 🗣️ Supported Language Pairs

- English → Spanish (`en-es`)
- Spanish → English (`es-en`)
- English → German (`en-de`)
- German → English (`de-en`)
- Spanish → German (`es-de`)
- German → Spanish (`de-es`)

> ✅ *Support can be extended by adding more MarianMT models to the `LANGUAGE_MODELS` dictionary.*

---

## 📦 Requirements

This project requires:

- Python 3.7+
- [`transformers`](https://pypi.org/project/transformers/)
- [`torch`](https://pypi.org/project/torch/)

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the translator in your terminal

```bash
python translator.py
```

### CLI Options:
- Type any text to translate it.

- Type switch to change the language pair.

- Type exit to quit.

## 🧠 Example Session

```bash
Multi-Language AI Translator
Supported language pairs:
  - en-es
  - es-en
  - es-de
  - de-es
  - en-de
  - de-en
Type 'exit' to quit or 'switch' to change language pair.
Current language pair: en-es

Enter text : Hello, how are you?
Translated text: Hola, ¿cómo estás?

Enter text : switch
Supported language pairs:
  - en-es
  - es-en
  - es-de
  - de-es
  - en-de
  - de-en
Enter new language pair: en-de
Switched to language pair: en-de

Enter text : This is a powerful tool.
Translated text: Dies ist ein leistungsstarkes Werkzeug.
```
## 🔧 Extending Support

To add more translation directions, just add to the LANGUAGE_MODELS dictionary:

```python
LANGUAGE_MODELS = {
    ...
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",  # English to French
}

```

Find more models here: [Helsinki-NLP on HuggingFace](https://huggingface.co/Helsinki-NLP)


## 📄 License

This project is open-source and available under the MIT License.
