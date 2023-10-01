'''
System helper functions
'''
import platform

def get_system_info():
  '''
  Get system information
  '''
  return {
    'os': platform.system(),
    'arch': platform.machine(),
  }
