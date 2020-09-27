
import argparse
from . import get_ressources

def parse_args():
    parser = argparse.ArgumentParser(description="""Crawl the ESM API docs and print all URLs""", prog="python3 -m esm_api_docs_crawler", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument( '--url', help="SIEM API help URL.", required=True )
    args = parser.parse_args()
    return(args)

if __name__=="__main__":
    args = parse_args()

    summary, methods, types = get_ressources(args.url)
    
    print(summary['url'])
    [ print(m['url']) for m in methods ]
    [ print(t['url']) for t in types ]
