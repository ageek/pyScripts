import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import sys

# Function to get all links from a page
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    return links

# Function to get PDF links from a page based on href text
def get_pdf_links_with_condition(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if a['href'].lower().endswith('.pdf') and 'full' in a.text.lower()]
    return pdf_links

# Function to download PDFs with a 5-second pause
def download_pdfs(links, folder_name):
    for link in links:
        pdf_links = get_pdf_links_with_condition(link)
        for pdf_link in pdf_links:
            pdf_filename = os.path.basename(pdf_link)
            pdf_path = os.path.join(folder_name, pdf_filename)
            response = requests.get(pdf_link)
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
                print(f'Downloaded: {pdf_path}')
            time.sleep(5)  # Pause for 5 seconds

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <url> <month> <year>")
        sys.exit(1)

    url = sys.argv[1]
    month = sys.argv[2]
    year = sys.argv[3]

    folder_name = f"{month}_{year}"
    os.makedirs(folder_name, exist_ok=True)

    # Get all links from the initial page
    all_links = get_links(url)

    # Download PDFs
    download_pdfs(all_links, folder_name)

