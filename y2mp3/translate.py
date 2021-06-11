from googletrans import Translator

translator = Translator()
result = translator.translate('keep smiling', src='en', dest='ta')

print(result)
print(result.extra_data)
print(result.text)