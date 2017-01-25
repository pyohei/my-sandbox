from setuptools import setup#, find_packages

long_desc = ''
with open('README.md') as f:
    logn_desc = f.read()

setup(name='prodictor',
      version='0.0.1',
      description='Cron scheduler.',
      logn_description=long_desc,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: MIT Licenseo',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ],
      keywords='cron crontab schedule',
      author='Shohei Mukai',
      author_email='xxxx@mail.mail',
      url='http://www.www',
      license='MIT',
      # packages=find_packages,
      install_requires=['crontab']
      )
