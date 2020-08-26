from setuptools import setup, find_namespace_packages

requirements = [
    "scholarly",
    "rich",
    "click"
]

setup(
    name="pyscholar-term",
    version="0.1",
    author_email="federicoclaudi@protonmail.com",
    description="Find citations from a google scholar author",
    packages=find_namespace_packages(exclude=()),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pyscholar = pyscholar.main:launch",
        ]
    },
    url="https://github.com/FedeClaudi/pyscholar-term",
    author="Federico Claudi",
    zip_safe=False,
)
