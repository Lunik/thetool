'''
Database helper functions
'''

import os
from git import Repo
import yaml

from thetool.metadata import METADATA
from thetool.helpers.cache import get_cache_path
from thetool.helpers.log import LOGGER

# The database is a git project downloaded from GitHub
# The database project is stored in the user's home cache directory
# The database project is cloned from the GitHub repository
# The database project is updated from the GitHub repository

def get_database_path():
  '''
  Get the path to the database
  '''
  # Get the path to the user's home directory
  cache_path = get_cache_path()

  # Return the path of the database cache directory
  return os.path.join(
    cache_path,
    'database'
  )


def init_database():
  '''
  Initialize the database
  '''
  # Get the path to the database directory
  database_path = get_database_path()

  # If the database directory does not exist
  if not os.path.isdir(database_path):
    LOGGER.debug('Database does not exist')
    # Create the database directory
    os.makedirs(database_path)

  # If the database directory is empty
  if not os.listdir(database_path):
    LOGGER.debug('Initializing database')
    # Clone the database project from GitHub
    Repo.clone_from(
      METADATA.get('database_url'),
      database_path
    )

def update_database(force=False):
  '''
  Update the database
  '''
  # Get the path to the database directory
  database_path = get_database_path()

  # If the database directory exists
  if os.path.isdir(database_path):
    LOGGER.debug('Updating database')
    # Open the database project
    repo = Repo(database_path)

    if force:
      # If force is True, reset the database project
      repo.git.reset('--hard')

    # Pull the latest changes from GitHub
    repo.remotes.origin.pull()

def get_database_index():
  '''
  Get the database index
  '''
  # Get the path to the database directory
  database_path = get_database_path()

  with open(os.path.join(database_path, 'index.yml'), 'r', encoding='UTF-8') as index_file:
    # Load the index file
    index = yaml.safe_load(index_file)

  return index

def get_database_tool(tool_name):
  '''
  Get the database tool
  '''
  # Get the path to the database directory
  database_path = get_database_path()

  # Get the database index
  index = get_database_index()

  # Get the tool from the index
  tool = index.get('tools', {}).get(tool_name)

  if tool:
    # If the tool exists, return the tool
    with open(os.path.join(database_path, tool.get('metadata')), 'r', encoding='UTF-8') as tool_metadata:

      tool = yaml.safe_load(tool_metadata)

    return tool

  # If the tool does not exist, raise an error
  raise ValueError(f'Tool {tool_name} not found in database')
