from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='nectarifere',
    url='https://github.com/XanAstia/Nectarifere.git',
    author='Xan Astia',
    author_email='xan.astia@live.fr',
    # Needed to actually package something
    packages=['nectarifere', 'tests'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='1.0',
    # The license can be anything you like
    license='MIT',
    description='Décorateur pour ambiancer vos codes.',
    long_description=open('README.md').read(),
#   include_package_data=True, #empeche package_data de fonctionner
    package_data={'nectarifere': ['Sounds/Kaamelott/Echec/*.wav', 'Sounds/Kaamelott/Succes/*.wav']},
)