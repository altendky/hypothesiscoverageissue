import setuptools

setuptools.setup(
    name='example',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'coverage',
        'hypothesis',
        'pytest',
    ],
)
