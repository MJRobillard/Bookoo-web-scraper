import scrapy
import os
import json

x = 'text'
a = 'author'

x = input("enter a bookoo link to anotate: ")

os.system('cmd /c "scrapy crawl quoc -O Out.json"')

output_file = open('Out.json').read()
output_json = json.loads(output_file)
t = ""


class QuotesSpider(scrapy.Spider):
    name = "quoc"
    start_urls = [
        x,
    ]

    def parse(self, response):
        x = -1
        for quote in response.css('div.price'):
            x += 1
            if quote.css("div.price::text").get() != None:
                a = "0" + quote.css("div.price::text").get()
            else:
                a = "0"
            yield {

                'price': a,
                'title': response.css("div.title").css("div.title::text")[x].get(),
                # 'tags': quote.css('div.tags a.tag::'+x+'').getall(),

            }
        next_page = (response.css('a').xpath('@href')[-16].get()) + "/"
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)




def filter_vowels(letter):
    vowels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","0.","1.","2.","3.","4.","5.","6.","7.","8.","9."]
    return True if letter in vowels else False


def json_to_string_list(output_json,title):
    tester = []
    for i in output_json:
        tester.append((i[title]))  # str as how the json dictionary is stored
    s = ""
    rocky = []
    # print(tester)
    for q in range(len(tester)):
        letters = tester[q]
        x = tuple(letters)
        s = ""
        for l in range(len(x)):
            s += x[l]
        rocky.append((s))
    return (rocky)


def json_to_float_list(output_json, title):
    tester = []
    for i in output_json:
        tester.append((i[title]))  # str as how the json dictionary is stored
    s = ""
    rocky = []
    # print(tester)
    for q in range(len(tester)):
        letters = tester[q]
        x = tuple(filter(filter_vowels, letters))
        s = ""
        for l in range(len(x)):
            s += x[l]
        rocky.append(float(s))
    return rocky


price_list = (json_to_float_list(output_json, "price"))
title_list = (json_to_string_list(output_json, "title"))

l = -1
for x in (price_list):
    l+=1
    a = float(x)
    if a >= 0.0 and a < 35.0:
        print(title_list[l])
        print(price_list[l])