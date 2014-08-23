import os
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'readme.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-inquisition',
    version='0.1.1',
    packages=['inquisition'],
    include_package_data=True,
    license='MIT',
    description='Search integrated into Django managers',
    long_description=readme,
    url='https://github.com/jleeothon/inquisition',
    author='Johnny Lee',
    author_email='jleeothon@outlook.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['django'],
    tests_require=['django'],
)
