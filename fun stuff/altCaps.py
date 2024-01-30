class AltCaps(object):

    def alt_caps(self, s: str) -> str:
        result = [letter.upper() if i % 2 == 0 else letter.lower() for i, letter in enumerate(s)]
        return ''.join(result)


s = AltCaps()
print(s.alt_caps("hello world"))


# Привет, на просторах интернета вы наверное замечали надписи с чередующимися заглавными и строчными буквами,
# Это alt-caps, писать alt-capsом самостоятельно сложно и неприятно,и так как мы знаем пайтон давайте напишем скрипт,
# который будет переводить текст в alt-caps.