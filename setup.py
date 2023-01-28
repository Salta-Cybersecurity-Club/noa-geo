from setuptools import setup, find_packages

setup(
    name="noa-geo",
    version="0.4.0",
    description="Utilidades geo para el NOA: POSGAR94/Gauss-Krüger, UTM, localidades",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Martina Delgado",
    author_email="7704567+mdelgado-noa@users.noreply.github.com",
    url="https://github.com/Salta-Cybersecurity-Club/noa-geo",
    packages=find_packages(exclude=("tests",)),
    package_data={"noa_geo": ["data/*.csv"]},
    python_requires=">=3.8",
    extras_require={"pyproj": ["pyproj>=3.3"]},
    entry_points={"console_scripts": ["noa-geo=noa_geo.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
