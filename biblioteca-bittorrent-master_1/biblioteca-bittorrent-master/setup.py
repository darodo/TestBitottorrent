#!/usr/bin/env python3

from distutils.core import setup

setup(name='BitTorrentBib',

      version='0.1',
      description='Biblioteca para conectarse a la red bittorrent',

      author='Grupo de investigación TECU',
      author_email='ausanabria@itcr.ac.cr',

      url= 'https://tecu.gitlab.io/',


      include_package_data=True,
      packages=['btb'],
      scripts=['bin/btcliente'],

      install_requires=[
          'twisted',
          'torrentool',
          'bitstring',
          'setuptools',
          'argparse',
	  'bencodepy',
	  'bencode'
      ],
     )

