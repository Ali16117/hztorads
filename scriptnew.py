import os
from bs4 import BeautifulSoup

# Specify the directory you want to start from
rootDir = '.'

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith('.html'):
            with open(os.path.join(dirName, fname), 'r+') as file:
                soup = BeautifulSoup(file, 'html.parser')

                # Find all link tags with rel="canonical"
                canonical_links = soup.find_all("link", rel="canonical")
                for link in canonical_links:
                    old_url = link['href']
                    new_url = 'https://hztorad.com/' + old_url
                    link['href'] = new_url
                
                file.seek(0)  # Go back to the start of the file
                file.write(str(soup))
                file.truncate()  # Remove any old, unneeded content
