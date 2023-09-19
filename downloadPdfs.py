import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


# Function to get all links from a page
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    return links

# Function to get PDF links from a page
def get_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]
    return pdf_links

# Function to download PDFs with a 5-second pause
def download_pdfs(links):
    for link in links:
        pdf_links = get_pdf_links(link)
        for pdf_link in pdf_links:
            pdf_filename = os.path.basename(pdf_link)
            response = requests.get(pdf_link)
            with open(pdf_filename, 'wb') as f:
                f.write(response.content)
                print(f'Downloaded: {pdf_filename}')
            time.sleep(5)  # Pause for 5 seconds

# URL of the initial page
initial_page_url = 'https://nopr.niscpr.res.in/handle/123456789/61096'  # Replace with the actual URL

# Get all links from the initial page
all_links = get_links(initial_page_url)

# Download PDFs
download_pdfs(all_links)
