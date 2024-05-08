import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urljoin

base_url = "http://quotes.toscrape.com/"
current_url = base_url
quotes_data = []

for _ in range(10):
    response = requests.get(current_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        quotes_data.append((text, author, tags))
    
    next_button = soup.find('li', class_='next')
    if next_button:
        next_page = next_button.find('a')['href']
        current_url = urljoin(base_url, next_page)
    else:
        break

authors = Counter([quote[1] for quote in quotes_data])
tags = Counter([tag for quote in quotes_data for tag in quote[2]])
quote_lengths = [len(quote[0]) for quote in quotes_data]


most_common_author = authors.most_common(1)[0]
least_common_author = authors.most_common()[-1]

average_length = sum(quote_lengths) / len(quote_lengths)
longest_quote = max(quotes_data, key=lambda x: len(x[0]))
shortest_quote = min(quotes_data, key=lambda x: len(x[0]))


most_popular_tag = tags.most_common(1)[0]
total_tags_used = sum(tags.values())


print(f"Number of quotes by each author: {dict(authors)}")
print(f"Author with the most quotes: {most_common_author}")
print(f"Author with the least quotes: {least_common_author}")
print(f"Average length of quotes: {average_length}")
print(f"Longest quote: {longest_quote[0]}")
print(f"Shortest quote: {shortest_quote[0]}")
print(f"Most popular tag: {most_popular_tag}")
print(f"Total tags used: {total_tags_used}")
