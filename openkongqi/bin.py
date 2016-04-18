# -*- coding: utf-8 -*-
import argparse
import distutils.spawn
import os
import sys

from openkongqi.exceptions import OpenKongqiError

from celery.bin.celery import main as clry_main


def okq_server():
    parser = argparse.ArgumentParser(description='outdoor air quality data')
    parser.add_argument('--okqconf', dest='conffile', action='store',
        type=str, help='path to a configuration file')
    args, clry_args = parser.parse_known_args()

    if args.conffile is not None:
        os.environ.setdefault('OKQ_CONFMODULE', args.conffile)

    # reproduce sys.argv to call celery
    clry_args.insert(0, distutils.spawn.find_executable('celery'))
    try:
        clry_main(clry_args)
    except OpenKongqiError as e:
        sys.stderr.write(e.message + "\n")
        sys.exit(1)


if __name__ == '__main__':          # pragma: no cover
    okq_server()
