'''
Cache helper functions
'''

import os

from thetool.metadata import METADATA

def get_cache_path():
  '''
  Get the path to the database
  '''
  # Get the path to the user's home directory
  home_path = os.path.expanduser('~')

  # Return the path of the database cache directory
  return os.path.join(
    home_path,
    '.cache',
    METADATA.get('name'),
  )
