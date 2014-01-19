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
                'pbf.Packages', 'pbf.Packages.Bluewolf', 'pbf.Packages.Core', 'pbf.Packages.KaoGUI',
                'pbf.Packages.PBF', 'pbf.Packages.Project', 'pbf.Packages.Python', 'pbf.Packages.Python.PySide', 'pbf.Packages.Python.unittest',  
                'pbf.Packages.Salesforce',
                'pbf.templates'],
      package_data = {'pbf.templates':['KaoGUI/*', 'PBF/*', 'Python/PySide/*', 'Python/unittest/*', 'Python/*.py', 'Salesforce/*']},
     )