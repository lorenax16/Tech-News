from tech_news.database import search_news
from datetime import date as data

# Requisito 6


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for new in news:
        result.append((new["title"], new["url"]))
    return result


# Requisito 7
def search_by_date(date):
    try:
        formatar_data = data.fromisoformat(date).strftime("%d/%m/%Y")
        nova_lista = search_news({"timestamp": formatar_data})
        lista = []

        for nova in nova_lista:
            lista.append((nova["title"], nova["url"]))

        return lista
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    lista_resultado = []
    nova_lista = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for nova in nova_lista:
        list = (nova["title"], nova["url"])
        lista_resultado.append(list)
    return lista_resultado


# Requisito 9
def search_by_category(category):
    nova_lista = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    lista = []

    for nova in nova_lista:
        lista.append((nova["title"], nova["url"]))
    return lista
