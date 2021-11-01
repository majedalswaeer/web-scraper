import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    """
    This function accept an url and scrap the data from it, then, it counting the citation needed in the paragraphs

    Args:
        url : String

    Returns:
        Number of needed citations: Integer
    """
    wiki_res = requests.get(url)
    soup = BeautifulSoup(wiki_res.content, "html.parser")
    citations_needed=soup.find_all(title='Wikipedia:Citation needed',limit=None)
    return len(citations_needed)

def get_citations_needed_report(url):
    """
    This function accept an url and scrap the data from it, then, its reporting the citaion needed

    Args:
        url : String

    Returns:
        Number of needed citations: Integer
    """
    output=''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    citations_needed=soup.find_all(class_='noprint Inline-Template Template-Fact')
    for u in citations_needed:
        parent=u.find_parent('p')
        text=parent.getText()
        output+=text+'\n'
    return output


if __name__ == '__main__':
    # get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))