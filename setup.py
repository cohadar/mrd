from setuptools import setup, find_packages
setup(
    name="mrd",
    packages=find_packages("код"),
    package_dir={"": "код"},
    install_requires=[
        "pysdl2",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
)
