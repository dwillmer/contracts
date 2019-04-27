import os

from setuptools import setup, find_packages

description = (
    'blue-contracts is a hard fork of the PyContracts library'
    'from Andrea Censi. This fork has been updated to allow '
    'multiple contract definitions on a function, as well as'
    'removing Python 2.x support and other updates.')


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


long_description = read('readme.md')


def get_version(filename):
    import ast
    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in %r.' % filename)
    if version is None:
        raise ValueError(filename)
    return version


version = get_version(filename='src/contracts/__init__.py')

setup(name='bluecove-contracts',
      author="BlueCove Developers",
      url='http://github.com/bluecoveltd/contracts',

      description=description,
      long_description=long_description,
      keywords="type checking, value checking, contracts",
      license="LGPL",

      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Testing'
      ],

      version=version,
      download_url='http://github.com/bluecoveltd/contracts/tarball/%s' % version,

      package_dir={'': 'src'},
      packages=find_packages('src'),
      install_requires=['pyparsing', 'decorator', 'six', 'future', 'numpy'],
      tests_require=['pytest'],
      entry_points={},
      )
