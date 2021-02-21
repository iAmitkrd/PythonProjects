from googletrans import Translator

translator = Translator()

mystory = "The quick brown fox jumps over the lazy dog. "

out = translator.translate(mystory, dest="hi")

print(out.text)
