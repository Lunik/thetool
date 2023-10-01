'''
Command: list
'''

from gettool.helpers.log import LOGGER
from gettool.helpers.database import get_database_index
from gettool.helpers.tool import list_installed_tools

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('list', help='list available tools')
  parser.add_argument('--installed', action='store_true', help='list installed tools')

def run(args):
  '''
  Run command.
  '''

  if args.installed:
    LOGGER.info('list installed tools')
    tools = list_installed_tools()

    pretty_tools = []
    for tool in tools:
      pretty_tools.append(f"{tool.get('name')}:{tool.get('version')}")

    LOGGER.info('Installed tools: %s', ', '.join(pretty_tools))
  else:
    LOGGER.info('list available tools')
    index = get_database_index()
    tools = index.get('tools').keys()

    LOGGER.info('Available tools: %s', ', '.join(tools))
