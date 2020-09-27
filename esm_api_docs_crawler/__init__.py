from .scrape import scrape
from urllib.parse import urlparse
def get_ressources(url):
    """
    Get the list of all SIEM API docs ressources as a tuple of list of dict with 'url' and 'html' keys.  
    
    Arguments:  

    - url: SIEM API help URL. Like https://ESM_URL/rs/esm/v2/help .  

    Returns: 

        `tuple ( summary (dict), methods (list), types (list) )`
    """

    urlp = urlparse(url)
    print("Crawling SIEM API ressources docs...")
    # Call scrapy
    items = scrape('esm_api_docs', spider_kwargs={'url':url}, additionnal_settings={'LOG_LEVEL':'ERROR'})
    # Sort items
    summary = items.pop(0)
    methods = sorted([i for i in items if '/help/types/' not in i['url']], key=lambda k: k['url'])
    types = sorted([i for i in items if '/help/types/' in i['url']], key=lambda k: k['url'])

    return summary, methods, types