import json
from pandas import Timestamp

def convertJson(lista):
    # Converte os valores Timestamp para strings
    for item in lista:
        if isinstance(item.get("VALIDADE"), Timestamp):
            item["VALIDADE"] = item["VALIDADE"].isoformat()

    # Converte a lista para JSON
    convert = json.dumps(lista, indent=4, ensure_ascii=False)

    # Salva o JSON em um arquivo
    with open("Insumos.json", "w+", encoding="utf-8") as file:
        file.write(convert)