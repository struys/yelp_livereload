#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import argparse
import sys
from livereload import Server
from livereload.watcher import Watcher

from yelp_livereload.util import get_port


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--extra-watch', nargs='*', default=[],
        help='Additional directories/files/globs to watch',
    )

    parser.add_argument('--port', default=get_port())

    args = parser.parse_args(argv)

    # The default pyinotify watcher seems to be broken, it only reloads once for some
    # reason, instead let's just always use the polling Watcher.
    server = Server(watcher=Watcher())
    server.watch('assets/scss/*.scss')
    server.watch('bower_components/*/assets/scss/*.scss')

    for extra in args.extra_watch:
        server.watch(extra)

    server.serve(host=socket.getfqdn(), port=args.port, debug=True)

if __name__ == '__main__':
    exit(main())
