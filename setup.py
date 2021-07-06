from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="valueguard",
    version="0.1.3",
    author="Valueguard",
    author_email="info@valueguard.se",
    description="The official client for the Valueguard API",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Valueguard-Index-Sweden/valueguard-python-client",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
)
