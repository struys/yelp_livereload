import mock
import pytest

from yelp_livereload import cli


@pytest.yield_fixture
def mock_server():
    with mock.patch.object(cli, 'Server') as ServerMock:
        yield ServerMock


def test_main_defaults(mock_server):
    cli.main([])
    mock_server().serve.assert_called_with(host=mock.ANY, port=35729, debug=True)


def test_main_port_override(mock_server):
    cli.main(['--port', '10000'])
    mock_server().serve.assert_called_with(host=mock.ANY, port='10000', debug=True)


def test_extra_watch(mock_server):
    cli.main(['--extra-watch', 'foo.scss'])
    mock_server().watch.assert_called_with('foo.scss')
