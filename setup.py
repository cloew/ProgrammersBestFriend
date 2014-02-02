from distutils.core import setup

setup(name='pbf',
      version='.1',
      description="Programmer's Best Friend Command Line Utility",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['pbf',
                'pbf.helpers', 'pbf.helpers.Project', 
                'pbf.helpers.Python', 'pbf.helpers.XML',
                'pbf.Commands', 'pbf.Commands.Core', 
                'pbf.Commands.PBF', 'pbf.Commands.Project', 
                'pbf.Commands.Python',
                'pbf.templates'],
      package_data = {'pbf.templates':['PBF/*', 'Python/*.py']},
      scripts=['pbf/scripts/pbf']
     )