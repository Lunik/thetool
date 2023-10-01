'''
Main module for thetool.
'''

import sys

from thetool.cli import parser
from thetool.helpers.log import setup_logging, LOGGER
from thetool.helpers.database import init_database
from thetool.helpers.tool import init_tool_directory

from thetool.commands.version import run as version_run
from thetool.commands.list import run as list_run
from thetool.commands.info import run as info_run
from thetool.commands.install import run as install_run
from thetool.commands.uninstall import run as uninstall_run
from thetool.commands.update import run as update_run
from thetool.commands.upgrade import run as upgrade_run
from thetool.commands.clean import run as clean_run

def main():
  '''
  Main function for thetool.
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
