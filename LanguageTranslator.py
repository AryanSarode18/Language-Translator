from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    print("Language Translator")

    source_language = input("Enter the source language: ")
    target_language = input("Enter the target language: ")
    text = input("Enter the text to translate: ")

    translated_text = translate_text(text, target_language)
    print(f"Translated text ({target_language}): {translated_text}")

if __name__ == "__main__":
    main()
