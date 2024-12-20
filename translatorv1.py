from transformers import MarianMTModel, MarianTokenizer

# Language-to-model mapping
LANGUAGE_MODELS = {
    "en-es": "Helsinki-NLP/opus-mt-en-es",  # English to Spanish
    "es-en": "Helsinki-NLP/opus-mt-es-en",  # Spanish to English
    "es-de": "Helsinki-NLP/opus-mt-es-de",  # Spanish to German
    "de-es": "Helsinki-NLP/opus-mt-de-es",  # German to Spanish
    "en-de": "Helsinki-NLP/opus-mt-en-de",  # English to German
    "de-en": "Helsinki-NLP/opus-mt-de-en",  # German to English
#    "en-jap": "Helsinki-NLP/opus-mt-en-jap", #English to Japanese (Not functional, currently)
}

# Load model and tokenizer for a specific language pair
def load_model(language_pair):
    model_name = LANGUAGE_MODELS.get(language_pair)
    if not model_name:
        raise ValueError(f"Language pair '{language_pair}' is not supported.")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Translate the input text
def translate(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    print("Multi-Language AI Translator")
    print("Supported language pairs:")
    for pair in LANGUAGE_MODELS.keys():
        print(f"  - {pair}")
    print("Type 'exit' to quit or 'switch' to change language pair.")

    current_language_pair = "en-es"  # Default language pair
    tokenizer, model = load_model(current_language_pair)
    print(f"Current language pair: {current_language_pair}")

    while True:
        text = input("\nEnter text : ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        elif text.lower() == 'switch':
            print("Supported language pairs:")
            for pair in LANGUAGE_MODELS.keys():
                print(f"  - {pair}")
            new_language_pair = input("Enter new language pair: ")
            try:
                tokenizer, model = load_model(new_language_pair)
                current_language_pair = new_language_pair
                print(f"Switched to language pair: {current_language_pair}")
            except ValueError as e:
                print(e)
        else:
            try:
                translation = translate(text, tokenizer, model)
                print("Translated text:", translation)
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    main()
