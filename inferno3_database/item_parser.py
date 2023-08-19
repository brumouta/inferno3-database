import re


def parse_item(item_text: str):
    effects = {}
    item = {"effects": effects}
    for line in item_text.split("\n"):
        line = line.strip()
        if line.startswith("Objeto"):
            m = re.match(r"Objeto '(?P<name>.+)', Tipo: (?P<type>.+)", line)
            item["name"] = m.groupdict().get("name")
            item["type"] = m.groupdict().get("type").capitalize()
        if line.startswith("Habilidades"):
            item["abilities"] = line.split(":")[1].strip().split(" ")
        if line.startswith("O item"):
            item["properties"] = line.split(":")[1].strip().split(" ")
        if line.startswith("Peso:"):
            for key, chunk in zip(
                ["weight", "value", "level", "remort"], line.split(",")
            ):
                item[key] = int(re.search(r"(?<=\[).+?(?=])", chunk).group(0))
        if line.startswith("Aplicação na AC"):
            item["armor"] = -int(re.search(r"(?<=\[).+?(?=])", line).group(0))
        if line.startswith("Afeta:"):
            m = re.match(r"Afeta: (?P<effect>.+) com \[(?P<value>.+)]", line)
            effect = m.groupdict().get("effect")
            value = int(m.groupdict().get("value"))
            if effect != "ARMADURA":
                effects[m.groupdict().get("effect")] = value
            else:
                item["armor"] += value
        if line.startswith("Este objeto pode"):
            item["prevents"] = line.split(":")[1].replace("'", "").strip().split(" ")
    return item
