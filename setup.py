from setuptools import setup, find_packages

setup(
    name="checknet",
    version="0.1.0",
    description="Verifica se há conexão com a internet usando sockets",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Rodrigo Gusso",
    author_email="rgusso@gmail.com",
    url="https://github.com/rgusso/checknet",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
