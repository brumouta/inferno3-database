import re


def parse_items(text: str):
    separated_texts = []
    indices_object = re.finditer(pattern="Objeto", string=text)
    indices = [index.start() for index in indices_object]
    for index in range(len(indices)):
        start = indices[index]
        end = indices[index + 1] if len(indices) > index + 1 else len(text)
        chunk = text[start:end]
        search = re.search(r"(Este objeto pode paralisar.+\')", chunk)
        if search:
            last_line = search.group(0)
        else:
            last_line = re.findall(r"Afeta:.+]", chunk)[-1]
        separated_texts.append(chunk[: chunk.rfind(last_line) + len(last_line)])
    return separated_texts
