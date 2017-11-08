from distutils.core import setup
from pip.req import parse_requirements


install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]
dep_links = [str(req_line.url) for req_line in install_reqs]

setup(
    name='data_utils',
    version='0.1.0',
    description='',
    install_requires=reqs,
    dependency_links=dep_links,
    packages=[
        'data_utils',
    ],
)
