import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

headers = {
    "User-Agent": "lab07-web-analyzer"
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

# print(soup.prettify())


headings = ["h1", "h2", "h3", "h4", "h5", "h6"]
headers = soup.find_all(headings)
links = soup.find_all("a")
paragraphs = soup.find_all("p")

print(len(headers), len(links), len(paragraphs))

sometext = soup.get_text()
sometext = sometext.lower()

words = re.findall(r'\b\w+\b', sometext)

word_array = []
word_count = []

for i in words:
    if (i in word_array):
        word_found = word_array.index(i)
        word_count[word_found] += 1
    else:
        word_array.append(i)
        word_count.append(1)
    

sorted_word_count = word_count.copy()
sorted_word_count.sort()
   
max_5 = [sorted_word_count[-1], sorted_word_count[-2], sorted_word_count[-3], sorted_word_count[-4], sorted_word_count[-5]]
max_index = []
for i in max_5:
    max_index.append(word_count.index(i))

for i in max_index:
    print(word_array[i], word_count[i])

searched_word = input("Enter a word dumbass: ").lower()
try:    
    print(word_count[word_array.index(searched_word)])
except Exception as error:
    print(error)

longest_paragraph = ""
max_words = 0

for p in paragraphs:
    text = p.get_text().strip()
    words = re.findall(r'\b\w+\b', text)

    if(len(words) >= 5):
        if(len(words) > max_words):
            max_words = len(words)
            longest_paragraph = text

print(longest_paragraph)

labels = ['Headings', 'Links', 'Paragraphs']
values = [len(headers), len(links), len(paragraphs)]
plt.bar(labels, values)
plt.title('Group 27')
plt.ylabel('Count')
plt.savefig('web_analysis_results.png') # Save the figure as an image file
plt.show()