from setuptools import setup

setup(
    name='ovex_py',
    version='0.0.1',    
    description='A package to interact with OVEX API',
    url='https://github.com/Quirky-Fox/OVEX-py',
    author='Duncan Andrew',
    author_email='duncan@lumina-x.com',
    license='BSD 2-clause',
    packages=['ovex_python'],
    install_requires=['requests'],
    keywords='OVEX cryptocurrency exchange API',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
    ],
)