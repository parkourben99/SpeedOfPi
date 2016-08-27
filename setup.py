from setuptools import setup

setup(name='SpeedOfPi',
      version='0.1',
      description='Speed Of Pi Arcade Game',
      url='http://github.com/parkourben99/SpeedOfPi',
      author='Benjamin Ayles',
      author_email='ben@ayles.com.au',
      license='MIT',
      packages=['SpeedOfPi'],
      install_requires=[
          'yaml',
      ],
      zip_safe=False)