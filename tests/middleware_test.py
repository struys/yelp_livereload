from __future__ import unicode_literals

import pytest
import webtest
from webob import Request
from yelp_livereload import middleware


@pytest.fixture
def app():
    def application(environment, start_response):
        request = Request(environment)

        headers = []

        if request.path == '/':
            body = b'<html><head></head></html>'
            status = b'200 OK'
            headers.append((str('Content-Type'), str('text/html; charset=UTF-8')))
        elif request.path == '/html_no_head':
            body = b'<html></html>'
            status = b'200 OK'
            headers.append((str('Content-Type'), str('text/html; charset=UTF-8')))
        else:
            body = b'404 Not Found'
            status = b'404 Not Found'
            headers.append((str('Content-Type'), str('text/plain; charset=UTF-8')))

        headers.append((str('Content-Length'), str(len(body))))

        start_response(status, headers)

        return [body]

    return webtest.TestApp(middleware.yelp_livereload_middleware(application))


def test_app_404(app):
    with pytest.raises(webtest.AppError):
        app.get('/does_not_exist')


def test_livereload_scss_route(app):
    resp = app.get('/livereload-scss.js')
    assert 'LiveReloadPluginSCSS' in resp.body.decode('utf-8')


def test_html_with_no_head(app):
    resp = app.get('/html_no_head')
    assert 'livereload.js' not in resp.body.decode('utf-8')


def test_applied_middleware(app):
    resp = app.get('/')

    assert 'livereload.js' in resp.body.decode('utf-8')
