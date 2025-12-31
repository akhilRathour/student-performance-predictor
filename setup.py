#to setup project automaticallly
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    #returns list of requirements
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[r.replace("\n","") for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req



setup(
name='student-performance',
version='0.0.1',
author='akhil',
author_email='akhil_rathour@outlook.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)