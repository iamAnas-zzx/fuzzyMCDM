from setuptools import setup, find_packages

VERSION = '1.9.2' 
DESCRIPTION = 'Python package 3'
LONG_DESCRIPTION = 'First Python package with a slightly name change'

# Setting up
setup(
        # the name must match the folder name 
        name="fuzzy_mcdm", 
        version=VERSION,
        author="MMMUT",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['fuzzy_mcdm', 'fuzzy_mcdm.matrixvalidation'],
        install_requires=["numpy"], 
        # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)