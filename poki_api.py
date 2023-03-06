#import requests
from dad_jokes_api import search_dad_jokes
from pastebin_api import post_new_paste
import sys

def main():
    search_term = get_search_term()
    jokes_list = search_dad_jokes(search_term)
    if jokes_list:
        title, body_text = get_paste_content()
        paste_url = post_new_paste(title, body_text)
        print(f'URL of jokes paste: {paste_url}')

def get_search_term():

    num_params = len(sys.argv) - 1
    if num_params > 0:
        search_term = sys.argv[1]
        return search_term
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_content(jokes_list, search term):
    return #title, body_text

if __name__ == "__main__":
    main()