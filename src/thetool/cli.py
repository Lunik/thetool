'''
This module contains the command line interface for the thetool package.
'''

import argparse
import sys

from thetool.commands.version import init_parser as version_init_parser
from thetool.commands.list import init_parser as list_init_parser
from thetool.commands.info import init_parser as info_init_parser
from thetool.commands.install import init_parser as install_init_parser
from thetool.commands.uninstall import init_parser as uninstall_init_parser
from thetool.commands.update import init_parser as update_init_parser
from thetool.commands.upgrade import init_parser as upgrade_init_parser
from thetool.commands.clean import init_parser as clean_init_parser

class TTParser(argparse.ArgumentParser):
  '''
  thetool parser.
  '''
  def error(self, message):
    '''
    Print error message and exit.
    '''
    sys.stderr.write(f'error: {message}\n')
    self.print_help()
    sys.exit(2)

parser = TTParser(description='Get and install tools from internet')
parser.add_argument('--debug', action='store_true', help='enable debug logging')
parser.add_argument('--quiet', action='store_true', help='disable logging')

subparsers = parser.add_subparsers(dest='command', help='command to run')
subparsers.required = True

version_init_parser(subparsers)
list_init_parser(subparsers)
info_init_parser(subparsers)
install_init_parser(subparsers)
uninstall_init_parser(subparsers)
update_init_parser(subparsers)
upgrade_init_parser(subparsers)
clean_init_parser(subparsers)
