'''
Command: uninstall
'''

from thetool.helpers.log import LOGGER
from thetool.helpers.database import get_database_tool
from thetool.helpers.tool import remove_tool

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('uninstall', help='uninstall tool')
  parser.add_argument('tool', help='tool name')
  parser.add_argument('-v', '--version', help='tool version to uninstall')

def run(args):
  '''
  Run command.
  '''

  LOGGER.info('uninstall tool %s', args.tool)
  tool_metadata = get_database_tool(args.tool)
  remove_tool(tool_metadata, version=args.version)
