'''
Command: clean
'''

import os
import shutil

from thetool.helpers.log import LOGGER
from thetool.helpers.cache import get_cache_path

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('clean', help='remove all cached files')

  return parser

def run(_args):
  '''
  Run command.
  '''

  LOGGER.debug('Running clean command')

  cache_path = get_cache_path()
  if os.path.isdir(cache_path):
    LOGGER.debug('Removing cache directory: %s', cache_path)
    shutil.rmtree(cache_path)
