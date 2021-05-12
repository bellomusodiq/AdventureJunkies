from typing import Optional

import requests

import bs4

from schema import (
    AggregateRating, Offer, PageAnnotation, BestSellers, CategoryOverview,
    Product, ProductAttribute, ProductAttributeValue, Question, Review, SearchAttribute, Taxonomy
)

import logging

import re


def get_questions(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    return None


def remove_tags(p):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', p.get_text())


def annotate(
    url: str, soup: bs4.BeautifulSoup, raw_body: str
) -> Optional[PageAnnotation]:
    """
    Required implementation.
    - url: Is the URL of the page to annotate.
    - soup: Is the parsed representation of the body of the page.
    - raw_body: Is raw html of the page.
    """
    
    products = []
    product_rows = soup.find_all("div", class_="sc-review-wrap-outer snow-review")
    product_from_table = soup.select("tbody tr")
    product_zip = zip(product_rows, product_from_table)
    product_name = None
    product_image = None
    product_callout = None
    product_description_list = []
    rating = None
    product_reviews = []
    product_offers = []
    product_specs = []
    for product_soup, table_products_soup in product_zip:
        try:
            product_name = product_soup.find("h3", class_="sc-review-item-title").get_text()
        except:
            pass
        try:
            product_image = product_soup.find("img").get("src").split("?")[0]
        except Exception as e:
            logging.error(e)
        try:
            product_callout = product_soup.find("div", class_="sc-rev-text").h4.span.get_text()
        except Exception as e:
            logging.error(e)
        try:
            product_p = product_soup.find("div", class_="sc-rev-text").find_all("p")
            product_description_list = list(map(remove_tags, product_p))
        except Exception as e:
            logging.error(e)
        try:
            rating = AggregateRating(rating_value=table_products_soup.find_all("td")[-1].get_text())
        except Exception as e:
            logging.error(e)
        try:
            product_r = product_soup.find("div", class_="featwrap").find_all("li")
            product_reviews = list(map(remove_tags, product_r))
            product_reviews = [Review(summary=item) for item in product_reviews]
        except Exception as e:
            logging.error(e)
        try:
            offers = product_soup.select("div.sc-rev-btns > div")
            for offer in offers:
                offers_obj = Offer(url=offer.a.get("href"), seller=offer.span.span.get_text())
                product_offers.append(offers_obj)
        except Exception as e:
            logging.error(e)
        try:
            product_s = product_soup.find("div", class_="specwrap").find_all("li")
            product_s = list(map(remove_tags, product_s))
            for spec in product_s:
                spec_values = spec.split(": ")[1].split(",")
                spec_values = list(map(lambda x: ProductAttributeValue(name=x.replace("&", "").strip()), spec_values))
                product_specs.append(ProductAttribute(
                    type="Specification",
                    name=spec.split(": ")[0],
                    values=spec_values
                ))
        except Exception as e:
            logging.error(e)
        product_obj = Product(
            aggregate_rating=rating,
            name=product_name,
            callout=product_callout,
            image_url=product_image,
            description_list=product_description_list,
            reviews=product_reviews,
            offers=product_offers,
            attributes=product_specs
        )
        products.append(product_obj)
    return PageAnnotation(products=products)
