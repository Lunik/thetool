'''
Command: update
'''

from thetool.helpers.log import LOGGER
from thetool.helpers.database import update_database

def init_parser(subparsers):
  '''
  Initialize parser.
  '''

  parser = subparsers.add_parser('update', help='update tools database')
  parser.add_argument('-f', '--force', action='store_true', help='force update')

  return parser

def run(args):
  '''
  Run command.
  '''

  LOGGER.info('update tools database')
  update_database(force=args.force)
