from setuptools import setup

setup(name='continuous_mutation',
      version='1.0.0',
      description='continuous_mutation of xml files for build systems',
      url='https://github.com/christoffer-nylen/continuous-mutation',
      author='Elias Lilja, Victor Dannetun, Olle Kvarnström, Marcus Sneitz, Daniel Persson',
      author_email='christoffer.nylen@saabgroup.com',
      packages=['continuous_mutation', 'continuous_mutation.xml_mutation', 'continuous_mutation.python_filter', 'continuous_mutation.database','continuous_mutation.command_manager', 'continuous_mutation.test'],
      include_package_data=True,
      zip_safe=False)

      
