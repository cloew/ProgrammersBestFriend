from distutils.core import setup

setup(name='pbf',
      version='.1',
      description="Programmer's Best Friend Command Line Utility",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['pbf',
                'pbf.helpers', 'pbf.helpers.Bluewolf', 'pbf.helpers.Project', 'pbf.helpers.Python',
                    'pbf.helpers.Python.unittest', 'pbf.helpers.Salesforce', 'pbf.helpers.XML',
                'pbf.Commands', 'pbf.Commands.Bluewolf', 'pbf.Commands.Core', 'pbf.Commands.KaoGUI',
                'pbf.Commands.PBF', 'pbf.Commands.Project', 'pbf.Commands.Python', 'pbf.Commands.Python.PySide', 'pbf.Commands.Python.unittest',  
                'pbf.Commands.Salesforce',
                'pbf.templates'],
      package_data = {'pbf.templates':['KaoGUI/*', 'PBF/*', 'Python/PySide/*', 'Python/unittest/*', 'Python/*.py', 'Salesforce/*']},
      scripts=['pbf/scripts/pbf']
     )