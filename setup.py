from setuptools import setup

setup(name='devserve',
      version='0.11',
      description='Web based control software for our custom built spectrofluoremeter ',
      url='http://github.com/jmosbacher/devserve',
      author='Yossi Mosbacher',
      author_email='joe.mosbacher@gmail.com',
      license='MIT',
      packages=['devserve'],
      install_requires=[
          'flask',
          'flask_restful',
          'pyserial',
          'redis',
          'automodinit',
          'pyvisa',
          'ThorlabsPM100',
          'thorlabs_apt',
      ],
      
      
      zip_safe=False)