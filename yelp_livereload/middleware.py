from __future__ import unicode_literals

import socket
import io
import pkg_resources

from webob import Request
from webob import Response

from yelp_livereload.util import get_port

markup_format_string = '''
    <script src="/livereload-scss.js"></script>
    <script src="//{0}:{1}/livereload.js"></script>
'''


def is_html_response(response):
    return response.headers.get("Content-Type") == 'text/html; charset=UTF-8'


def yelp_livereload_middleware(app, port=get_port()):

    def yelp_livereload(environment, start_response):
        request = Request(environment)

        if request.path == '/livereload-scss.js':
            js_path = pkg_resources.resource_filename('yelp_livereload', 'assets/livereload-scss.js')

            response = Response(
                io.open(js_path, 'rb').read(),
                content_type='application/javascript',
            )
            return response(environment, start_response)

        response = request.get_response(app)

        if is_html_response(response):
            position = get_insert_position(response.text)

            if position != -1:
                html = markup_format_string.format(socket.getfqdn(), port)
                response.content_length += len(html)
                response.text = ''.join([response.text[:position], html, response.text[position:]])

        return response(environment, start_response)

    return yelp_livereload


def get_insert_position(response_text):
    try:
        start_head_index = response_text.index("<head")
        start_head_end_index = response_text.index(">", start_head_index)
        return start_head_end_index + 1
    except ValueError:
        return -1
