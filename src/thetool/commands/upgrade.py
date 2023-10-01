'''
Command: upgrade
'''

from thetool.helpers.log import LOGGER
from thetool.helpers.database import get_database_tool
from thetool.helpers.tool import download_tool, list_installed_tools

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('upgrade', help='upgrade tool')
  parser.add_argument('tool', help='tool to upgrade', nargs='?')

  return parser

def run(args):
  '''
  Run command.
  '''

  if args.tool:
    LOGGER.info('upgrade tool %s', args.tool)
    tool_metadata = get_database_tool(args.tool)
    download_tool(tool_metadata)
  else:
    LOGGER.info('upgrade all tools')
    tools = list_installed_tools()
    for tool in tools:
      LOGGER.info('upgrade tool %s', tool.get('name'))
      tool_metadata = get_database_tool(tool.get('name'))
      download_tool(tool_metadata)
