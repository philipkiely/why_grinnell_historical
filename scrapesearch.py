import urllib3
from bs4 import BeautifulSoup


def get_link(line):
    """extracts the alumni name and gets a link based on it"""
    name = line.split(",")[1]
    name = name.replace(" ", "%5C%20")
    url = "https://digital.grinnell.edu/islandora/search/catch_all_fields_mt%3A%28"
    url += name + "%29"
    return url


def search_count(url):
    """A function that, given a url for a search, returns the number of search results"""
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    if req.status != 200:
        print("Error: ", req.status, " skipping page")
        return None #dead link
    page = req.data
    soup = BeautifulSoup(page, 'lxml')
    count = soup.find('div', {'id': 'islandora-solr-result-count'})
    print(count, url)


if __name__ == "__main__":
    links = []
    csv = open('alumni.csv', 'r')
    for line in csv:
        links.append(get_link(line))
    for link in links:
        search_count(link)
    print("done")
