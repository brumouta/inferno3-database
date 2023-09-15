import re

from inferno3_database.domain.ports.schemas.items import ItemDto


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
            properties = line.split(":")[1].strip().split(" ")
            item["properties"] = [property for property in properties if property not in ["ENTALHADO"]]
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
            prevents = line.split(":")[1]
            m = re.findall(r"'(.*?)'", prevents)
            item["prevents"] = m
        if line.startswith("Capacidade:"):
            m = re.search(r"\[(?P<value>.+)]", line.split(":")[1])
            item["capacity"] = m.groupdict().get("value")
        if line.startswith("Este VARINHA invoca:"):
            # add wand spell and charges
            item["wand"] = line.split(":")[1].strip()
        if line.startswith("Drop"):
            item["mob"] = line.split(":")[1].strip()
    return ItemDto(**item)
