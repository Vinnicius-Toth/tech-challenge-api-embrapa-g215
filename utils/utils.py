from fastapi import HTTPException
from enums.enums import abas_embrapa, url, range_anos_embrapa

# def validar_abas_embrapa(aba: str) -> bool:
#     """
#     Valida se a aba informada na requisição é válida.
#     :param aba: Nome da aba a ser validada.
#     :return: True se a aba for válida, False caso contrário.
#     """
#     try:
#         aba = abas_embrapa[aba]
#         return True
#     except:
#         raise ValueError(f"Aba inválida. Escolha entre: {', '.join(abas_embrapa.keys())}")

def validar_ano(ano: int) -> bool:
    """
    Valida se o ano informado na requisição está dentro do intervalo permitido.
    :param ano: Ano a ser validado.
    :return: True se o ano for válido, False caso contrário.
    """
    if range_anos_embrapa[0] <= ano <= range_anos_embrapa[1]:
        return True
    raise HTTPException(
            status_code=400,
            detail=f"Ano inválido. Escolha um ano entre {range_anos_embrapa[0]} e {range_anos_embrapa[1]}."
        )

def validar_subcategorias(aba: str, subcategoria: str) -> bool:
    """
    Valida se a subcategoria informada na requisição é válida.
    :param aba: Nome da aba a ser validada.
    :param subcategoria: Nome da subcategoria a ser validada.
    :return: True se a subcategoria for válida, False caso contrário.
    """
    try:
        abas_embrapa[aba]["subcategorias"][subcategoria]
        return True
    except KeyError:
        raise HTTPException(
            status_code=400,
            detail=f"Subcategoria inválida. Para a aba: {aba} - Escolha entre: {', '.join(abas_embrapa[aba]['subcategorias'].keys())}"
        )
    
def capturar_url(aba: str, ano: int, subcategoria= None) -> str:
    """
    Captura a URL para a requisição com base na aba, ano e subcategoria informados.
    :param aba: Nome da aba.
    :param ano: Ano da requisição.
    :param subcategoria: Subcategoria da requisição.
    :return: URL formatada para a requisição.
    """
    if subcategoria:
        return url + f"ano={ano}&opcao={abas_embrapa[aba]['codigo']}&subopcao={abas_embrapa[aba]['subcategorias'][subcategoria]}"
    
    else:
        return url + f"ano={ano}&opcao={abas_embrapa[aba]['codigo']}"