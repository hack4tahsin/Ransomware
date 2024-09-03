from setuptools import find_packages, setup

setup(
    name="gcdlcm",
    version="0.0.0",
    author="Tahsin Ahmed",
    description="This library is for finding GCD and LCM",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=["gcd", "lcm", "math", "calculation", "greatest common divisor", "least common multiple"],
    packages=find_packages(),
    license=open("LICENSE.md", encoding="utf-8").read(),
    include_package_data=True,
    install_requires=[""],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Natural Langauge :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)