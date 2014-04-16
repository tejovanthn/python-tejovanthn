try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'tejovanthn',
    'author': 'Tejovanth N',
    'url': 'https://github.com/tejovanthn/tejovanthn',
    'download_url': 'https://github.com/tejovanthn/tejovanthn',
    'author_email': 'tejovanthn@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['tejovanthn'],
    'scripts': [],
    'name': 'tejovanthn'
}

setup(**config)
