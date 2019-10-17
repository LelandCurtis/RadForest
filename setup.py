import setuptools

setuptools.setup(
    name = 'radforest-LSC', #pypi package name
    version = '0.1.0',
    description = 'This is a test file created during the 2019 AEC Tech conference. Hey hey.',
    url = 'https://github.com/LelandCurtis/RadForest',
    author = 'Leland Curtis',
    author_email = 'leland.curtis@smithgroup.com',
    license = 'MIT',
    packages = setuptools.find_packages(exclude = ['tests'])
)