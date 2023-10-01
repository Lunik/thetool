'''
HTTP helper functions
'''
import os
from datetime import timedelta

from requests_cache import CachedSession, SQLiteCache

from thetool.helpers.cache import get_cache_path

def get_http_session():
  '''
  Get a http session
  '''
  cache_path = os.path.join(get_cache_path(), 'http_cache')
  return CachedSession(backend=SQLiteCache(cache_path), expire_after=timedelta(hours=1))
