import unittest

from inferno3_database import item_parser


class TestItemParser(unittest.TestCase):
    def test_parse(self):
        item_text = """Você se sente informado:
Objeto 'O Anel de Safira de Elrond', Tipo: ARMADURA
Habilidades do Item:  DET-ALIGN DET-MAGIC SENSE-LIFE FORBIDDEN_SANCTUARY
O item é: AURA NÃO_DOA INVISÍVEL MÁGICO ABENÇOADO ANTI_MAU ANTI_ANÃO ANTI_CORSÁRIO NO_LOCATE
Peso: [1], Valor: [2000000], Lvl. Min.: [90], Remort Min.: [50]
Aplicação na AC é de [10]
Pode te afetar com :
Afeta: MAXMANA com [100]
Afeta: MAXVIDA com [200]
Afeta: MAXMOVE com [300]
Afeta: ACERTO com [21]
Afeta: DANO com [42]
Afeta: FOR com [1]
Afeta: DES com [2]
Afeta: INT com [3]
Afeta: SAB com [4]
Afeta: CON com [5]
Afeta: CAR com [6]
Afeta: ARMADURA com [-50]
Este objeto pode paralisar as habilidades:  'curse' 'poison' 'blindness' 'fireball'"""

        item = {
            "name": "O Anel de Safira de Elrond",
            "type": "Armadura",
            "abilities": [
                "DET-ALIGN",
                "DET-MAGIC",
                "SENSE-LIFE",
                "FORBIDDEN_SANCTUARY",
            ],
            "properties": [
                "AURA",
                "NÃO_DOA",
                "INVISÍVEL",
                "MÁGICO",
                "ABENÇOADO",
                "ANTI_MAU",
                "ANTI_ANÃO",
                "ANTI_CORSÁRIO",
                "NO_LOCATE",
            ],
            "level": 90,
            "remort": 50,
            "value": 2000000,
            "weight": 1,
            "armor": -60,
            "effects": {
                "MAXMANA": 100,
                "MAXVIDA": 200,
                "MAXMOVE": 300,
                "ACERTO": 21,
                "DANO": 42,
                "FOR": 1,
                "DES": 2,
                "INT": 3,
                "SAB": 4,
                "CON": 5,
                "CAR": 6,
            },
            "prevents": ["curse", "poison", "blindness", "fireball"],
        }

        self.assertEqual(item_parser.parse_item(item_text), item)


if __name__ == "__main__":
    unittest.main()
