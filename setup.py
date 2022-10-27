"""setup script.

https://github.com/ninjaaron/fast-entry_points
https://github.com/pypa/setuptools/issues/510
"""

__author__ = 'mangalbhaskar'


import setuptools

import setuputils

if __name__ == '__main__':
  setuptools.setup(
    name='prag-csg518iot',
    version=setuputils.get_version('csg518iot'),
    packages=setuptools.find_packages(),
    ## version 3.6 or later, but not version 4.0 or later.
    python_requires='~=3.6',
    include_package_data=True,
    package_dir={
      'csg518iot': 'csg518iot',
    },
    install_requires=[
      'Click>=7.1.2',
      'pydantic>=1.8.2',
      'fastapi>=0.61.1',
      'sqlalchemy>=^1.3.16',
      'pydantic-to-typescript>=1.0.8',
    ],
    extras_require={
      'docs': [
        'pdoc>=11.1.0; python_version>="3.7"',
        'Jinja2==3.0.2',
        'mkdocs>=1.1.2',
        'mkdocs-exclude>=1.0.2',
        'mkdocs-git-revision-date-localized-plugin>=0.8',
        'mkdocs-git-revision-date-plugin>=0.3.1',
        'mkdocs-macros-plugin>=0.6.0',
        'mkdocs-markdownextradata-plugin>=0.1.7',
        'mkdocs-minify-plugin>=0.4.0',
        'mkdocs-material<=6.1.0',
        'mkdocs-material-extensions>=1.0.1',
        'pymdown-extensions>=9.0',
      ],
      'tests': [
        'pytest',
        'codecov',
        'interrogate',
        'xdoctest >= 0.10.0',
        'yapf',
      ],
      'build': [
        'twine==3.7.0',
      ],
    },
  )
