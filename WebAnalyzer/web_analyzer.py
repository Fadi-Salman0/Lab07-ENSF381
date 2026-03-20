import requests
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup 

url = "https://en.wikipedia.org/wiki/University_of_Calgary" 

headers = { 
"User-Agent": "lab07-web-analyzer" 
} 

try: 
    response = requests.get(url, headers=headers) 
    response.raise_for_status()  # Ensures the request was successful 
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(f"Successfully fetched content from {url}") 
except Exception as e: 
    print(f"Error fetching content: {e}")

print(soup.prettify())

header_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
headings_count = len(soup.find_all(header_tags))

print(f"\nTotal number of headers: {headings_count}\n")

links_count = len(soup.find_all('a'))

print(f"Total number of links: {links_count}\n")

paragraphs = soup.find_all('p')
paragraphs_count = len(paragraphs)

print(f"Total number of paragraphs: {paragraphs_count}\n")

bsText = soup.get_text().lower()
splitText = re.findall(r'\b\w+\b', bsText)

wordFrequency = {}
for word in splitText:
    if word in wordFrequency:
        wordFrequency[word] += 1
    else:
        wordFrequency[word] = 1

sortedWordFrequency = dict(sorted(wordFrequency.items(), key=lambda item: item[1], reverse=True))

print("Top 5 most common words:")
for i, (word, freq) in enumerate(sortedWordFrequency.items()):
    if i < 5:
        print(f"{word}: {freq}")
    else:
        break

searchWord = input("\nEnter a keyword to search for: ").lower()

if searchWord in wordFrequency:
    print(f"The word '{searchWord}' appears {wordFrequency[searchWord]} times.\n")
else:
    print(f"The word '{searchWord}' does not appear.\n")

longestParagraph = ""
longestCount = 4

for paragraph in paragraphs:
    text = paragraph.get_text().strip()
    wordCount = len(re.findall(r'\b\w+\b', text))
    if wordCount > longestCount:
        longestCount = wordCount
        longestParagraph = text

if longestCount == 4:
    print("No paragraphs found with at least 5 words.\n")
else:
    print(f"Longest paragraph ({longestCount} words):\n{longestParagraph}\n")

labels = ['Headings', 'Links', 'Paragraphs'] 
values = [headings_count, links_count, paragraphs_count] 
plt.bar(labels, values) 
plt.title('Group 27') 
plt.ylabel('Count')  
plt.show() 