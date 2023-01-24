from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for new in news:
        result.append((new["title"], new["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


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
    """Seu código deve vir aqui"""
