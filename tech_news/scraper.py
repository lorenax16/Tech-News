from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    time.sleep(1)
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=header)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2


def scrape_updates(html_content):
    selector = Selector(html_content)
    noticias = selector.css("h2.entry-title a::attr(href)").getall()
    return noticias


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    paginacao = selector.css("a.next.page-numbers::attr(href)").get()
    return paginacao


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = selector.css("ol.comment-list li").get() or 0

    summary = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()

    tags = selector.css("section.post-tags li a::text").getall()
    category = selector.css("a.category-style .label::text").get()

    info_completa = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }

    return info_completa


# O programa abaixo ilustra o funcionamento do método join():
# list1 = ['1','2','3','4']
# s = "-"
# s = s.join(list1)
# print(s)
# Resultado:
# 1-2-3-4

# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
