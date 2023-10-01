'''
Command: install
'''

from thetool.helpers.log import LOGGER
from thetool.helpers.tool import download_tool
from thetool.helpers.database import get_database_tool

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('install', help='install tool')
  parser.add_argument('tool', help='tool to install')
  parser.add_argument('-f', '--force', action='store_true', help='force install')
  parser.add_argument('-v', '--version', help='tool version to install')

  return parser

def run(args):
  '''
  Run command.
  '''

  LOGGER.info('install tool %s', args.tool)
  tool_metadata = get_database_tool(args.tool)
  download_tool(tool_metadata, force=args.force, version=args.version)
