import requests
from bs4 import BeautifulSoup
import texttable


urls = {
    "https://item.rakuten.co.jp/a-price/4571495430840",
    "https://item.rakuten.co.jp/ya-man/r2110a",
    "https://item.rakuten.co.jp/dyson/244396-01",
    
}

data = []
for url in urls:
    
    response = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'lxml')


    item_number = soup.find("span", class_= "item_number").get_text()
    name = soup.find("span", class_ = "item_name").get_text()
    price = int(soup.find("span", class_="price2", itemprop="price").get("content"))



    description = soup.find("meta", itemprop="description").get("content")
    try:
        review_count = soup.find("meta", itemprop="reviewCount").get("content")
    except:
        review_count = "0"

    try:
        review_score = soup.find("meta", itemprop="ratingValue").get("content")
        review_score = float(review_score)
    except:
        review_score = "0"

    image = soup.find("meta", itemprop="image").get("content")

    #append without sorting
    data.append([name.strip()[:24], item_number, price, review_count, review_score])

# Creating table
table = texttable.Texttable()
  
# Creating columns
table.set_cols_dtype(["t", "i", "i", "i", "t"])
table.set_cols_align(["c", "c", "c", "c", "c"])
# add more space to the "Name cells"
table.set_cols_width([50, 15, 10, 8, 8])



# Creating rows
table.add_row(['Name', 'Item Nº', 'Price', 'Reviews', 'Rating'])

table.add_rows(
    data,
    header=False
)
print(table.draw())