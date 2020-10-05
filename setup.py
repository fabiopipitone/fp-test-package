from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
  long_description = fh.read()

setup( 
  name ='fp-test-package', 
  version ='0.0.1', 
  author ='Fabio Pipitone', 
  author_email='fabio.pipitone93@gmail.com',
  description='Simple test building a CLI tool package',
  long_description=long_description,
  long_description_content_type='text/x-rst', 
  license ='GPLv2', 
  packages = find_packages(), 
  entry_points ={ 
    'console_scripts': [ 
      'fp_test_package = fp_test_package.py:main'
    ] 
  }, 
  classifiers =( 
    "Programming Language :: Python :: 3", 
    "License :: OSI Approved :: GNU General Public License v2", 
    "Operating System :: Linux", 
  ), 
  keywords ='test packaging fabiopipitone', 
  install_requires = ['tqdm>=4.49.0'], 
  zip_safe = False
) 