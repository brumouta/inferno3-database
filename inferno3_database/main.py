from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def items():
    return {
        """Objeto 'O Cinto Prateado de Petrine, a Fada da Ilusão', Tipo: ARMADURA
Habilidades do Item:  MIRROR-IMAGE 
Pode ser usado em: CINTURA 
O item é: AURA SOM NÃO_DOA MÁGICO ABENÇOADO NÃO_VENDE ENTALHADO AUTOENTALHAR LEVE AVENTURA NO_LOCATE
Peso: [1], Valor: [40], Lvl. Min.: [0], Remort Min.: [0]
Aplicação na AC é de [30]
Pode te afetar com :
   Afeta: CON com [2]
   Afeta: MAXMOVE com [50]
   Afeta: MAXVIDA com [200]
   Afeta: MAXMANA com [150]
   Afeta: ACERTO com [8]
   Afeta: DANO com [8]"""
    }
