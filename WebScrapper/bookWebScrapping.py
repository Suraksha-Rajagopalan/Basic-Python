import bs4
import requests

# Create a url without page number
basic_url = 'http://books.toscrape.com/catalogue/page-{}.html'

#List of 4 or 5 star titles
high_rated_titles = []

#Iterate pages
for p in range(1, 51):

    # Create soup on each page
    results = requests.get(basic_url.format(p))
    soup = bs4.BeautifulSoup(results.text, 'html.parser')

    #Select data of books
    books = soup.select('.product_pod')

    # Iterate books
    for book in books:

        #Check if they are 4 or 5 stars books
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            #Store title
            book_title = book.select('a')[1]['title']

            #add book to list
            high_rated_titles.append(book_title)

for b in high_rated_titles:
    print(b)
