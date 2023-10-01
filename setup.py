#!/usr/bin/env python
# pylint: disable=missing-docstring
import os
from setuptools import setup, find_packages


def get_version():
  """Get version from __init__.py file."""
  filename = os.path.join(os.path.dirname(__file__), 'src', 'thetool', 'metadata.py')
  with open(filename, encoding="UTF-8") as file:
    for line in file:
      if line.startswith('__version__'):
        return eval(line.split('=')[-1]) # pylint: disable=eval-used

  raise ValueError(f"No __version__ defined in {filename}")

setup(
  name='thetool',
  version=get_version(),
  description='Get and install tools from internet',
  long_description=open('README.md', encoding='UTF-8').read(), # pylint: disable=consider-using-with
  author='Guillaume MARTINEZ',
  author_email='lunik@tiwabbit.fr',
  maintainer='Guillaume MARTINEZ',
  maintainer_email='lunik@tiwabbit.fr',
  url='http://localhost/thetool',
  download_url='http://localhost/thetool',
  license_files = ('LICENSE',),
  package_dir={'': 'src'},
  packages=find_packages(where='src'),
  entry_points={
    'console_scripts': [
      'thetool = thetool:main',
    ],
  },
  python_requires=">=3.8.0",
  install_requires = [
    'requests==2.*',
    'requests-cache==1.*',
    'pyyaml==6.*',
    'GitPython==3.*',
  ],
  extras_require={
    'dev': [
      'pylint',
      'build',
      'pytest',
      'pytest-cov',
      'pytest-html',
      'pytest-xdist',
      'pytest-helpers-namespace',
      'pytest-order',
      'wheel',
      'twine'
    ],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
