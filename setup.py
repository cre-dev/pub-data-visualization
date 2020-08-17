import setuptools
from distutils.core import setup

setup(
      name             = 'cre-visu',
      version          = '0.1.dev0',
      packages         = setuptools.find_packages(),
      scripts          = [],
      author           = 'CRE',
      author_email     = 'opensource[at]cre.fr',
      license          = 'MIT License',
      long_description = open('README.txt').read(),
      python_requires  = ">= 3.8",
      install_requires = [
                          'matplotlib',
                          'numpy',
                          'pandas',
                          'seaborn',
			  'termcolor',
                          ],
      )