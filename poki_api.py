#import requests
from poki_names_api import search_poki_names
import sys

def main():
    search_term = get_search_term()
    poki_list = search_poki_names(search_term)
    if poki_list:
        title, body_text = get_paste_content()
        paste_url = post_new_paste(title, body_text)
        print(f'URL of poki paste: {paste_url}')

def get_search_term():

    num_params = len(sys.argv) - 1
    if num_params > 0:
        search_term = sys.argv[1]
        return search_term
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_content(poki_list, search term):
    return None

if __name__ == "__main__":
    main()
