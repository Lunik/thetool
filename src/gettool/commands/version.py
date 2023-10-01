'''
Command: version
'''

from gettool.metadata import METADATA
from gettool.helpers.log import LOGGER

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  return subparsers.add_parser('version', help='print version')

def run(_args):
  '''
  Run command.
  '''

  LOGGER.info('%s version %s', METADATA.get('name'), METADATA.get('version'))
