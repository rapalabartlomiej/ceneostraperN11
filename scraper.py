import requests
import os
from bs4 import BeautifulSoup
import json

def get_element(ancestor, selector=None, attribute=None, return_list= False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute].strip()
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
selectors={
            "opinion_id": ( None, "data-entry-id"),
            "author": ( "span.user-post__author-name",),
            "recommendation": ("span.user-post__author-recomendation > em",),
            "score": ("span.user-post__score-count",),
            "purchased": ("div.review-pz",),
            "opinion_date":("span.user-post__published > time:nth-child(1)","datetime"),
            "purchase_date": ("span.user-post__published > time:nth-child(2)","datetime"),
            "likes": ("button.vote-yes","data-total-vote"),
            "dislikes": ("button.vote-no","data-total-vote"),
            "content": ("div.user-post__text",),
            "cons": ( "div.review-feature__title--negatives ~ div.review-feature__item", None, True),
            "pros": ( "div.review-feature__title--positives ~ div.review-feature__item", None, True), 
        }
#product_code = input("podaj kod produktu")
product_code = "95733300"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
opinions_all = []
while url:
    print(url)
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(response.text, "html.parser")
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            single_opinion = {}
            for key, value in selectors.items():
                single_opinion[key]= get_element(opinion, *value)
            opinions_all.append(single_opinion)
    try:
        url = "https://www.ceneo.pl" + get_element(page_dom, "a.pagination_next", "href")
    except TypeError:
        url= None
if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f"opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dumps(opinions_all, indent=4, ensure_ascii=False)

#print(json.dumps(opinions_all, indent=4, ensure_ascii=False))