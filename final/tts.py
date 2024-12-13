from text_to_speech import save

def speak(string):
    text = string
    language = "en"  # Specify the language (IETF language tag)
    output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

    save(text, language, file=output_file)
