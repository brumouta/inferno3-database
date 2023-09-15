import unittest

from inferno3_database import text_parser


class TestTextParse(unittest.TestCase):
    def test_parse(self):
        text = """Você se sente informado:
Objeto 'O Divino Cinturão de Aquário', Tipo: ARMADURA
Pode ser usado em: CINTURA 
O item é: AURA SOM MÁGICO ABENÇOADO ENTALHADO AUTOENTALHAR NO_LOCATE NO_PEEK 
Peso: [15], Valor: [4000000], Lvl. Min.: [60], Remort Min.: [3]
Aplicação na AC é de [40]
Pode te afetar com :
   Afeta: DANO com [6]
   Afeta: ACERTO com [7]
   Afeta: MAXMANA com [100]
   Afeta: MAXVIDA com [250]
   Afeta: MAXMOVE com [50]
   Afeta: CON com [3]

(Prox Level: 66.17M) 9.75KHp 9.04KMn 4.72KMv   >
ide arie
Isso deve ser um erro... Se não for, tente elaborar mais um pouco.

(Prox Level: 66.17M) 9.75KHp 9.04KMn 4.72KMv   >
iden ari
Você pronuncia as palavras mágicas, 'Dignosco'
Você se sente informado:
Objeto 'Os Divinos Chifres de Áries', Tipo: ARMADURA
Habilidades do Item:  SANCT SNEAK 
Pode ser usado em: PESCOÇO 
O item é: AURA SOM MÁGICO ABENÇOADO ENTALHADO AUTOENTALHAR NO_LOCATE NO_PEEK 
Peso: [1], Valor: [10000000], Lvl. Min.: [60], Remort Min.: [3]
Aplicação na AC é de [0]
Pode te afetar com :
   Afeta: DANO com [8]
   Afeta: ACERTO com [8]
   Afeta: MAXMANA com [100]
   Afeta: MAXVIDA com [100]
   Afeta: MAXMOVE com [50]
   Afeta: IDADE com [40]
Este objeto pode paralisar a habilidade:  'curse'

(Prox Level: 66.17M) 9.75KHp 9.02KMn 4.72KMv   >
[Dragons][Grande Bahamut]Saibot: itens de infernais eu nem deixo em casa, sei lá, prefiro deixar em
bolsa

(Prox Level: 66.17M) 9.75KHp 9.02KMn 4.72KMv   >
iden curt
Você perde sua concentração!

(Prox Level: 66.17M) 9.75KHp 9.01KMn 4.72KMv   >
iden dourado
Você pronuncia as palavras mágicas, 'Dignosco'
Você se sente informado:
Objeto 'um medalhão Dourado', Tipo: ARMADURA
Habilidades do Item:  DET-INVIS DET-MAGIC SANCT 
Pode ser usado em: PESCOÇO 
O item é: AURA SOM NÃO_DOA MÁGICO NÃO_VENDE ENTALHADO AUTOENTALHAR LEVE NO_LOCATE 
Peso: [6], Valor: [2000000], Lvl. Min.: [1], Remort Min.: [2]
Aplicação na AC é de [10]
Pode te afetar com :
   Afeta: DANO com [3]
   Afeta: ACERTO com [4]
   Afeta: FOR com [1]
   Afeta: DES com [1]"""

        items = [
            """Objeto 'O Divino Cinturão de Aquário', Tipo: ARMADURA
Pode ser usado em: CINTURA 
O item é: AURA SOM MÁGICO ABENÇOADO ENTALHADO AUTOENTALHAR NO_LOCATE NO_PEEK 
Peso: [15], Valor: [4000000], Lvl. Min.: [60], Remort Min.: [3]
Aplicação na AC é de [40]
Pode te afetar com :
   Afeta: DANO com [6]
   Afeta: ACERTO com [7]
   Afeta: MAXMANA com [100]
   Afeta: MAXVIDA com [250]
   Afeta: MAXMOVE com [50]
   Afeta: CON com [3]""",
            """Objeto 'Os Divinos Chifres de Áries', Tipo: ARMADURA
Habilidades do Item:  SANCT SNEAK 
Pode ser usado em: PESCOÇO 
O item é: AURA SOM MÁGICO ABENÇOADO ENTALHADO AUTOENTALHAR NO_LOCATE NO_PEEK 
Peso: [1], Valor: [10000000], Lvl. Min.: [60], Remort Min.: [3]
Aplicação na AC é de [0]
Pode te afetar com :
   Afeta: DANO com [8]
   Afeta: ACERTO com [8]
   Afeta: MAXMANA com [100]
   Afeta: MAXVIDA com [100]
   Afeta: MAXMOVE com [50]
   Afeta: IDADE com [40]
Este objeto pode paralisar a habilidade:  'curse'""",
            """Objeto 'um medalhão Dourado', Tipo: ARMADURA
Habilidades do Item:  DET-INVIS DET-MAGIC SANCT 
Pode ser usado em: PESCOÇO 
O item é: AURA SOM NÃO_DOA MÁGICO NÃO_VENDE ENTALHADO AUTOENTALHAR LEVE NO_LOCATE 
Peso: [6], Valor: [2000000], Lvl. Min.: [1], Remort Min.: [2]
Aplicação na AC é de [10]
Pode te afetar com :
   Afeta: DANO com [3]
   Afeta: ACERTO com [4]
   Afeta: FOR com [1]
   Afeta: DES com [1]""",
        ]

        self.assertEqual(
            items,
            text_parser.parse_items(text),
        )


if __name__ == "__main__":
    unittest.main()
