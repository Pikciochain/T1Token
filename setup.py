from setuptools import setup, find_packages

version = '0.0.1'

with open('./requirements.txt', 'r') as requirements_file:
    requirements = [
        requirement for requirement in requirements_file
    ]

with open('./dev_requirements.txt', 'r') as dev_file:
    dev_requirements = [
        dev_requirement
        for dev_requirement in dev_file
        if not dev_requirement.startswith('-r') and dev_requirement != '\n'
    ]

setup(
    name='pikciotok',
    version=version,
    description='Pikcio Tokens Toolkit',
    url='https://github.com/Pikciochain/T1Token',
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Pikcio Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    author='Pikcio SAS',
    author_email='jorick.lartigau@pikcio.com',
    packages=find_packages(exclude=['examples', 'docs', 'tests*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
    setup_requires=dev_requirements,
    tests_require=dev_requirements,
)
