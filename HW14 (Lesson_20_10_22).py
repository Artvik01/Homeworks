import requests
import json
import random


def sort_quotes_by_name(item):
    surname = item["quoteAuthor"].split()[-1]
    return surname


class Quotes:
    def __init__(self, quotes_count, filename, format):
        self.quotes_count = quotes_count
        self.filename = f"{filename}.{format}"
        self.format = format
        self.url = "http://api.forismatic.com/api/1.0/"
        self.quotes_list = []

    def get_quote(self):
        params = {"method": "getQuote", "format": self.format, "key": random.randint(0, 999999), "lang": "en"}
        response = requests.get(self.url, params=params)
        try:
            if response.json()["quoteAuthor"] != "":
                return response.json()
            else:
                return self.get_quote()
        except json.decoder.JSONDecodeError:
            return self.get_quote()

    def get_quotes(self):
        for quote_num in range(self.quotes_count):
            self.quotes_list += [self.get_quote()]

    def print_quotes(self):
        for quote in self.quotes_list:
            quote_text = quote["quoteText"][:-2]
            quote_author = quote["quoteAuthor"]
            print(f"\"{quote_text}\" {quote_author}")

    def save_quotes(self):
        with open(self.filename, "w") as json_file:
            json.dump(sorted(self.quotes_list, key=sort_quotes_by_name), json_file)
