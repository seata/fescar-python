import setuptools
from os import path

DIR = path.dirname(path.abspath(__file__))
install_requires = open(path.join(DIR, 'requirements.txt')).read().splitlines()

setuptools.setup(
    name="seata-python",
    version="0.1",
    author="jsbxyyx",
    author_email="jsbxyyx@163.com",
    description="seata-python",
    long_description="seata-python",
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    url="https://github.com/opentrx/seata-python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)