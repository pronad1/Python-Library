from setuptools import setup, find_packages

setup(
    name="prosen-pythonlib",
    version="0.1.2",
    packages=find_packages(),
    author="Prosenjit Mondol",
    author_email="ug2102049@cse.pstu.ac.bd",
    description="A simple greeting package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",

    # Add these:
    url="https://github.com/pronad1/Python-Library",
    project_urls={
        "Source": "https://github.com/pronad1/Python-Library",
        "Tracker": "https://github.com/pronad1/Python-Library/issues",
    },
)
