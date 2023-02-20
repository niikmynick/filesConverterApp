import re
import os


def to_xml(filepath):
    slash = userInput.rfind("\\")

    path = userInput[:slash + 1]
    name = userInput[slash + 1:userInput.rfind(".")]

    with open(filepath, 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]
    count = 0
    tmp = []

    with open(path + name + '.xml', 'w', encoding='utf8') as file:
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                tmp.append(text[i])
                file.write('     ' * count + f'<{tag}> \n')
                count += 1
            elif ':' in text[i]:
                tag = re.search(r'"(-\w*)":', text[i])[0][2:-2]
                info = re.search(r'": "([\S\s]*)"', text[i])[0][4:-1]

                file.write('     ' * count + f'<{tag}> {info} </{tag}> \n')
            elif '}' in text[i]:
                count -= 1
                tag = re.search(r'"(\w*)":', tmp.pop())[0][1:-2]
                file.write('     ' * count + f'</{tag}> \n')


def to_wml(filepath):
    slash = userInput.rfind("\\")

    path = userInput[:slash + 1]
    name = userInput[slash + 1:userInput.rfind(".")]

    with open(filepath, 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]
    count = 1
    tmp = []

    with open(path + name + '.wml', 'w', encoding='utf8') as file:
        file.write('<wml> \n')
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                tmp.append(text[i])
                file.write('     ' * count + f'<{tag}> \n')
                count += 1
            elif ':' in text[i]:
                tag = re.search(r'"(-\w*)":', text[i])[0][2:-2]
                info = re.search(r'": "([\S\s]*)"', text[i])[0][4:-1]

                file.write('     ' * count + f'<{tag}> {info} </{tag}> \n')
            elif '}' in text[i]:
                count -= 1
                tag = re.search(r'"(\w*)":', tmp.pop())[0][1:-2]
                file.write('     ' * count + f'</{tag}> \n')
        file.write('</wml>')


def to_tsv(filepath):
    slash = userInput.rfind("\\")

    path = userInput[:slash + 1]
    name = userInput[slash + 1:userInput.rfind(".")]

    with open(filepath, 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]

    with open(path + name + '.tsv', 'w', encoding='utf8') as file:
        tags = []
        infos = []
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                file.write(f'{tag}\n')
            elif ':' in text[i]:
                tags.append(re.search(r'"(-\w*)":', text[i])[0][2:-2])
                infos.append(re.search(r'": "([\S\s]*)"', text[i])[0][4:-1])
            elif '}' in text[i]:
                for j in tags:
                    file.write(j + '    ')
                file.write('\n')
                for k in infos:
                    file.write(k + '    ')
                file.write('\n')


def to_csv(filepath):
    slash = userInput.rfind("\\")

    path = userInput[:slash + 1]
    name = userInput[slash + 1:userInput.rfind(".")]

    with open(filepath, 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]

    with open(path + name + '.csv', 'w', encoding='utf8') as file:
        tags = []
        infos = []
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                file.write(f'{tag}\n')
            elif ':' in text[i]:
                tags.append(re.search(r'"(-\w*)":', text[i])[0][2:-2])
                infos.append(re.search(r'": "([\S\s]*)"', text[i])[0][4:-1])
            elif '}' in text[i]:
                for j in tags:
                    file.write(j + ',')
                file.write('\n')
                for k in infos:
                    file.write(k + ',')
                file.write('\n')


def to_yaml(filepath):
    slash = userInput.rfind("\\")

    path = userInput[:slash + 1]
    name = userInput[slash + 1:userInput.rfind(".")]

    with open(filepath, 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]
    count = 0

    with open(path + name + '.yml', 'w', encoding='utf8') as file:
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                file.write('     ' * count + f'{tag}: \n')
                count += 1
            elif ':' in text[i]:
                tag = re.search(r'"(-\w*)":', text[i])[0][2:-2]
                info = re.search(r'": "([\S\s]*)"', text[i])[0][4:-1]

                file.write('     ' * count + f'{tag}: {info} \n')


console = {
    'xml': to_xml,
    'wml': to_wml,
    'tsv': to_tsv,
    'csv': to_csv,
    'yaml': to_yaml
}

userInput = input('Укажите абсолютный путь к файлу json: ')
while not os.path.isfile(userInput):
    userInput = input('Такого файла не существует, попробуйте снова: ')

newFormat = input('Введите формат нового файла: ')

if __name__ == '__main__':
    console[newFormat](userInput)
