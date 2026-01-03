from deep_translator import GoogleTranslator
import re
import time

input_file = ""    #input_file name for example winadadebebi.txt
output_file = ""   #output_file name for example GE-winadadebebi.txt

translator = GoogleTranslator(source="en", target="ka")

def translate_text(text):
    # for API
    max_len = 4500
    parts = [text[i:i+max_len] for i in range(0, len(text), max_len)]
    translated = []
    for part in parts:
        translated.append(translator.translate(part))
        time.sleep(0.3)
    return "".join(translated)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Recital
recitals = re.split(r"(=+\nGDPR RECITAL – NO \d+[\s\S]*?=+\n)", content)
recitals = [r for r in recitals if r.strip()]

with open(output_file, "w", encoding="utf-8") as out:

    for block in recitals:
        if block.startswith("="):
            out.write(block + "\n")
            continue

        print("🔄 translat")
        translated_text = translate_text(block)
        out.write(translated_text + "\n\n")

print("✔ translated ")
print(f"📄 file location: {output_file}")
