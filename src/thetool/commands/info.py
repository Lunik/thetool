'''
Command: info
'''

from thetool.helpers.log import LOGGER
from thetool.helpers.database import get_database_index, get_database_tool
from thetool.helpers.tool import get_tool_version

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('info', help='print info about tool')
  parser.add_argument('tool', help='tool name')


def run(args):
  '''
  Run command.
  '''

  LOGGER.info('print info about tool %s', args.tool)
  index = get_database_index()

  if args.tool not in index.get('tools').keys():
    raise Exception(f"Tool {args.tool} not found") # pylint: disable=broad-exception-raised

  tool_metadata = get_database_tool(args.tool)
  version = get_tool_version(tool_metadata)

  LOGGER.info('Tool: %s', args.tool)
  LOGGER.info('Version: %s', version)
  LOGGER.info('Description: %s', tool_metadata.get('description'))
  LOGGER.info('URL: %s', tool_metadata.get('url'))
