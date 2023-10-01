'''
Main module for gettool.
'''

import sys

from gettool.cli import parser
from gettool.helpers.log import setup_logging, LOGGER
from gettool.helpers.database import init_database
from gettool.helpers.tool import init_tool_directory

from gettool.commands.version import run as version_run
from gettool.commands.list import run as list_run
from gettool.commands.info import run as info_run
from gettool.commands.install import run as install_run
from gettool.commands.uninstall import run as uninstall_run
from gettool.commands.update import run as update_run
from gettool.commands.upgrade import run as upgrade_run
from gettool.commands.clean import run as clean_run

def main():
  '''
  Main function for gettool.
  '''

  args = parser.parse_args()

  setup_logging(args)

  LOGGER.debug('args: %s', args)

  if args.command not in ['version', 'clean']:
    init_database()
    init_tool_directory()

  match args.command:
    case 'version':
      version_run(args)
    case 'list':
      list_run(args)
    case 'info':
      info_run(args)
    case 'install':
      install_run(args)
    case 'uninstall':
      uninstall_run(args)
    case 'update':
      update_run(args)
    case 'upgrade':
      upgrade_run(args)
    case 'clean':
      clean_run(args)
    case _:
      parser.print_help()
      sys.exit(1)

if __name__ == '__main__':
  main()
