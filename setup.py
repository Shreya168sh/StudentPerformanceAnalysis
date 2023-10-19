from setuptools import find_packages, setup
from typing import List


"""
setup.py is created to build and distribute one's own Python package so that others can use it.
"""

# To ignore -e . from requirements file which is added to execute 
# the setup when installing all the requirements
_e = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of packages required in this project.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if _e in requirements:
            requirements.remove(_e)

    return requirements


setup(
    name = 'mlproject',
    version='0.0.1',
    author='Shreya',
    author_email='qv.shreyasharma2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)

