from setuptools import setup, find_namespace_packages

setup(
    name='Clean folder',
    version='0.0.1',
    description='sort file in folder',
    author='Oleksandr Volynets',
    author_email='a.volynets1981@gmail.com',
    url='https://github.com/OleksandrVolynets/Clean-folder.git',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['run=clean_folder.clean:run']}
)
