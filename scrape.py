import urllib3
from bs4 import BeautifulSoup


def get_links(url):
    ret = []
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    if req.status != 200:
        print("Error: ", req.status, " skipping page")
        return None #don't index dead links
    page = req.data
    soup = BeautifulSoup(page, 'lxml')
    links = soup.find('div', {'class': 'view-content'})
    links = links.find_all("div", {'class': 'left'})
    for link in links:
        ret.append(link.find('a')['href'])
    return ret


def get_page(url):
    """A function that, given a url from an alumni oral history, gets the transcript"""
    http = urllib3.PoolManager()
    req = http.request('GET', "https://digital.grinnell.edu/" + url)
    if req.status != 200:
        print("Error: ", req.status, " skipping page")
        return None #don't index dead links
    page = req.data
    soup = BeautifulSoup(page, 'lxml')
    transcript = soup.find('ul', {'class': 'list-group'})
    transcript = transcript.find_all("li")
    file_name = "output/" + url.split("/")[-1] + ".txt"
    file = open(file_name, "w")
    for entry in transcript:
        for line in entry.find_all('span', {'class': "oh_speaker_text"}):
            file.write(entry.find('span', {'class': "speaker-display active"}).text + ":: " + line.text + "\n")
    file.close()


if __name__ == "__main__":
    links = get_links("https://digital.grinnell.edu/islandora/object/grinnell%3Aalumni-oral-histories")
    for link in links:
        try:
            get_page(link)
        except:
            print(link)
    for i in range(1, 8):
        url = "https://digital.grinnell.edu/islandora/object/grinnell%3Aalumni-oral-histories?page=" + str(i)
        try:
            links = get_links(url)
        except:
            print(url)
        for link in links:
            try:
                get_page(link)
            except:
                print(link)
    print("done")
