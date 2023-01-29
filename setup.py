from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='nectarifere',
    url='https://github.com/XanAstia/Nectarifere.git',
    author='Xan Astia',
    author_email='xan.astia@live.fr',
    # Needed to actually package something
    packages=['nectarifere', 'tests'],
    # Needed for dependencies
    install_requires=['playsound==1.2.2', 'pillow'],
    # *strongly* suggested for sharing
    version='2.1',
    # The license can be anything you like
    license='MIT',
    description='Décorateur pour ambiancer vos codes.',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
#   include_package_data=True, #empeche package_data de fonctionner
    package_data={'nectarifere': ['Sounds/Kaamelott/Echec/*.wav', 'Sounds/Kaamelott/Succes/*.wav', 'Pictures/Echec/*.jpg', 'Pictures/Succes/*.jpg']},
)