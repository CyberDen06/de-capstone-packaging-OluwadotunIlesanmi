from setuptools import setup, find_packages

setup(
    name="omnicart-pipeline-Oluwadotun_Ilesanmi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0,<3.0.0",
        "requests>=2.28.0,<3.0.0",
        "numpy>=1.23.0,<2.0.0",
    ],
    package_data={
        'omnicart_pipeline': ['pipeline.cfg'],
    },
    entry_points={
        'console_scripts': [
            'omnicart-pipeline=omnicart_pipeline.cli:main',
            'omnicart-pipeline-Oluwadotun_Ilesanmi=omnicart_pipeline.cli:main',
        ],
    },
)