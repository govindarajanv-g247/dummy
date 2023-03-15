from setuptools import setup, find_packages
setup(
    name="main",
    version="1.0.0",
    packages=find_packages(),

    package_data={'.': ['employee.json']},
    include_package_data=True,

)