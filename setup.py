#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup


setup(
    name='lineflow',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Framework-Agnostic NLP Data Loader in Python',
    long_description=open('./README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yasufumy/lineflow',
    author='Yasufumi Taniguchi',
    author_email='yasufumi.taniguchi@gmail.com',
    packages=[
        'lineflow', 'lineflow.datasets', 'lineflow.torch'
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=['easyfile'],
    tests_require=['pytest'],
    extras_require={
        'allennlp': ['allennlp'],
        'pytorch': ['torch_nightly'],
        'torchtext': ['torchtext']
    },
    dependency_links=[
        'https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html',
        'https://download.pytorch.org/whl/nightly/cu90/torch_nightly.html',
        'https://download.pytorch.org/whl/nightly/cu100/torch_nightly.html',
    ],
)
