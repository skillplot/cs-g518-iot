"""setup script."""

__author__ = 'mangalbhaskar'


import os
import re
import sys

this_dir = os.path.abspath(os.path.dirname(__file__))


def get_pyver():
  __pyver = list(sys.version_info)[:2]
  pyver = float('.'.join(map(str, __pyver)))
  pyver = '.'.join(map(str, __pyver))
  return pyver


def get_requirements_filepath(pyver, filename):
  requirements_basepath = os.path.join(
      this_dir,
      'requirements',
      pyver,
      filename,
  )
  return requirements_basepath


def get_version(_name_):
  filepath = os.path.join(this_dir, _name_, '__init__.py')
  with open(filepath, encoding='utf8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)
  return version


def long_description():
  filepath = os.path.join(this_dir, 'README.md')
  with open(filepath, encoding='utf-8') as f:
    long_description = f.read()


def parse_requirements(
    fname='requirements/requirements.txt',
    with_version=True,
):
  """Parse the package dependencies listed in a requirements file but strips
  specific versioning information.

  python -c "import setup; print(setup.parse_requirements())"
  """
  require_fpath = fname

  def parse_line(line):
    """Parse information from a line in a requirements text file."""
    if line.startswith('-r '):
      # Allow specifying requirements in other files
      target = line.split(' ')[1]
      for info in parse_require_file(target):
        yield info
    else:
      info = {'line': line}
      if line.startswith('-e '):
        info['package'] = line.split('#egg=')[1]
      else:
        # Remove versioning from the package
        pat = '(' + '|'.join(['>=', '==', '>']) + ')'
        parts = re.split(pat, line, maxsplit=1)
        parts = [p.strip() for p in parts]

        info['package'] = parts[0]
        if len(parts) > 1:
          op, rest = parts[1:]
          if ';' in rest:
            # Handle platform specific dependencies
            # http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-platform-specific-dependencies
            version, platform_deps = map(
                str.strip,
                rest.split(';'),
            )
            info['platform_deps'] = platform_deps
          else:
            version = rest  # NOQA
          info['version'] = (op, version)
      yield info

  def parse_require_file(fpath):
    with open(fpath) as f:
      for line in f.readlines():
        line = line.strip()
        if line and not line.startswith('#'):
          yield from parse_line(line)

  def gen_packages_items():
    if os.path.exists(require_fpath):
      for info in parse_require_file(require_fpath):
        parts = [info['package']]
        if with_version and 'version' in info:
          parts.extend(info['version'])
        if not sys.version.startswith('3.4'):
          # apparently package_deps are broken in 3.4
          platform_deps = info.get('platform_deps')
          if platform_deps is not None:
            parts.append(';' + platform_deps)
        item = ''.join(parts)
        yield item

  packages = list(gen_packages_items())
  return packages
