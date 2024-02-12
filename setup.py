from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    ## this function will return the list of requirements ##
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


# def get_requirements(file_path: str) -> List[str]:
#     requirements = []
#     with open(file_path) as file_obj:
#         for line in file_obj:
#             line = line.strip()  # Remove leading/trailing whitespace
#             if line and line != HYPEN_E_DOT:  # Check if line is not empty and not '-e .'
#                 requirements.append(line)
#     return requirements

setup(
    name='ml_project',
    version ='0.0.1',
    author='Avishek Modi',
    author_email='avishekmodi839@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']

)