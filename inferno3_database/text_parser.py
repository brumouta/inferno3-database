import re
from operator import itemgetter


def parse_items(text: str):
    separated_texts = []
    indices_object = re.finditer(pattern="Objeto", string=text)
    indices = [index.start() for index in indices_object]
    for index in range(len(indices)):
        start = indices[index]
        end = indices[index + 1] if len(indices) > index + 1 else len(text)
        chunk = text[start:end]
        lines = [
            (search.span()[1], search.group(0))
            for regex in [
                r"Room:.+?\n",
                r"Drop:.+?\n",
                r"Capacidade:.+?]\n",
                r"Este objeto pode paralisar.+'\n",
                r"Afeta:.+]",
            ]
            if (search := re.search(regex, chunk))
        ]

        last_line = max(lines, key=itemgetter(0))[1]
        separated_texts.append(chunk[: chunk.rfind(last_line) + len(last_line)])
    return separated_texts
