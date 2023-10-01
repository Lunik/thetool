'''
Helper functions for logging.
'''

import logging

LOGGER = logging.getLogger(__name__)

def setup_logging(args):
  '''
  Setup logging.
  '''

  if args.debug:
    logging.basicConfig(level=logging.DEBUG)
  elif args.quiet:
    logging.basicConfig(level=logging.ERROR)
  else:
    logging.basicConfig(level=logging.INFO)
