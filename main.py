import os
from bottle import request, route, run, redirect, static_file, template

# URL Constants
KEYWORD_QUERY_NAME = "q"
PAGE_QUERY_NAME = "page"

# App Constants
PAGE_SIZE = 5

@route('/')
def process_page():
    # If the request contains a keyword query (/?q=query)
    # Show query result page
    if KEYWORD_QUERY_NAME in request.query:
        page = 1
        # If the request contains a page query (/?q=query&page=2)
        if PAGE_QUERY_NAME in request.query:
            page = int(request.query[PAGE_QUERY_NAME])
        return process_query(request.query[KEYWORD_QUERY_NAME].lower(), page)
    else:
    # Show home page
        return show_main_page()

def show_main_page():
    return template('main.html')

def process_query(query_string, page):
    # If query string is empty or only white spaces, redirect to home page
    if not query_string or query_string.isspace():
        return redirect('/')

    # 1. Split the query string into a list of words
    query_words = filter(bool, query_string.split())

    return template('search_result.html', query_string = query_string)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))