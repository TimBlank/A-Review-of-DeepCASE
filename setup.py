import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepATLAS-programm",
    version="0.1",
    author="Tim Behrens",
    author_email="tim.behrens@uni-oldenburg.de",
    description="DeepATLAS: Practical analysis of DeepCASE an Security Event Handler"
                "for battling Alert Fatigue ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimBlank/DeepCASE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
