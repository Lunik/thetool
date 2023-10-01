'''
Tool helpers functions
'''
import os
import tempfile
import shutil
import zipfile
import tarfile

from packaging.version import parse as VersionParser
from thetool.helpers.http import get_http_session

from thetool.metadata import METADATA
from thetool.helpers.log import LOGGER
from thetool.helpers.system import get_system_info


def get_tool_version(tool_metadata):
  '''
  Get the version of the tool
  '''
  session = get_http_session()
  response = session.get(tool_metadata.get('version_url'))
  LOGGER.debug('Response retrieved from cache: %s', response.from_cache)
  LOGGER.debug(response.text)

  if response.status_code == 200:
    version_format = tool_metadata.get('version_format')
    match version_format:
      case 'github_release':
        raw_version = response.json().get('tag_name')
      case 'plain':
        raw_version = response.text.strip()
      case _:
        raise ValueError(f'Unknown version type {version_format}')

    return VersionParser(raw_version)

  raise ValueError(f'Unable to get version for {tool_metadata.get("name")}')

def get_tool_url(tool_metadata, version=None):
  '''
  Get the url of the tool
  '''
  system_info = get_system_info()

  if version is None:
    version = get_tool_version(tool_metadata)

  return tool_metadata.get('download_url').format(
    version=version,
    os=system_info.get('os').lower(),
    arch=system_info.get('arch'),
  )

def get_tool_directory(public=False):
  '''
  Get the path to the tool directory
  '''
  home_path = os.path.expanduser('~')

  if public:
    path = os.path.join(
      home_path,
      'bin',
    )
  else:
    path = os.path.join(
      home_path,
      f".{METADATA.get('name')}",
      'bin',
    )

  return path

def init_tool_directory():
  '''
  Initialize the tool directory
  '''
  # Get the path to the tool directory
  tool_directory = get_tool_directory()

  # If the tool directory does not exist
  if not os.path.isdir(tool_directory):
    LOGGER.debug('Tool directory does not exist')
    # Create the tool directory
    os.makedirs(tool_directory)

  tool_directory_public = get_tool_directory(public=True)

  # If the tool directory does not exist
  if not os.path.isdir(tool_directory_public):
    LOGGER.debug('Tool directory does not exist')
    # Create the tool directory
    os.makedirs(tool_directory_public)

def download_tool(tool_metadata, force=False, version=None):
  '''
  Download the tool
  '''

  session = get_http_session()
  if version:
    tool_version = VersionParser(version)
  else:
    tool_version = get_tool_version(tool_metadata)
  tool_url = get_tool_url(tool_metadata, version=tool_version)
  tool_path = os.path.join(get_tool_directory(public=False), f"{tool_metadata.get('name')}_{tool_version}")
  final_tool_path = os.path.join(get_tool_directory(public=True), tool_metadata.get('name'))

  if os.path.isfile(tool_path) and not force:
    LOGGER.debug('Tool already downloaded')
    return

  LOGGER.debug('Downloading %s from %s', tool_metadata.get('name'), tool_url)
  response = session.get(tool_url)

  with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(response.content)

  download_format = tool_metadata.get('download_format')
  match download_format:
    case 'bin':
      LOGGER.debug('Moving %s to %s', temp_file.name, tool_path)
      shutil.move(temp_file.name, tool_path)

    case 'zip':
      with tempfile.TemporaryDirectory() as temp_dir:
        LOGGER.debug('Extracting %s', temp_file.name)
        with zipfile.ZipFile(temp_file.name, 'r') as zip_file:
          zip_file.extractall(temp_dir)

        LOGGER.debug('Moving %s to %s', tool_metadata.get('download_archive_bin'), tool_path)
        shutil.move(os.path.join(temp_dir, tool_metadata.get('download_archive_bin')), tool_path)

    case 'tar.gz':
      with tempfile.TemporaryDirectory() as temp_dir:
        LOGGER.debug('Extracting %s', temp_file.name)
        with tarfile.open(temp_file.name, 'r:gz') as tar_file:
          tar_file.extractall(temp_dir)

        LOGGER.debug('Moving %s to %s', tool_metadata.get('download_archive_bin'), tool_path)
        shutil.move(os.path.join(temp_dir, tool_metadata.get('download_archive_bin')), tool_path)

  LOGGER.debug('Setting permissions on %s', tool_path)
  os.chmod(tool_path, 0o700)
  if os.path.islink(final_tool_path):
    LOGGER.debug('Removing %s', final_tool_path)
    os.remove(final_tool_path)
  LOGGER.debug('Symlinking %s to %s', tool_path, final_tool_path)
  os.symlink(tool_path, final_tool_path)

def remove_tool(tool_metadata, version=None):
  '''
  Remove the tool
  '''
  if version:
    tool_version = VersionParser(version)
  else:
    tool_version = get_tool_version(tool_metadata)

  tool_path = os.path.join(get_tool_directory(public=False), f"{tool_metadata.get('name')}_{tool_version}")

  if os.path.isfile(tool_path):
    LOGGER.debug('Removing %s', tool_path)
    os.remove(tool_path)

def list_installed_tools():
  '''
  List installed tools
  '''
  tool_directory = get_tool_directory(public=False)
  raw_tools = os.listdir(tool_directory)

  tools = []

  for binary in raw_tools:
    tool_parts = binary.split('_')
    tools.append({
      'name': tool_parts[0],
      'version': tool_parts[1],
    })

  return tools
