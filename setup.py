from setuptools import setup

setup(
  name = 'Texture_Atlas',         # How you named your package folder (MyLib)
  packages = ['TextureAtlas'],   # Chose the same as "name"
  version = '0.1.9',
  license='MIT',
  description = 'Create a texture dynamic texture atlas you can constantly change.',
  author = 'Shaun Kulesa',
  author_email = 'shaunkulesa@gmail.com',
  url = 'https://github.com/ShaunKulesa/Texture-Atlas',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ShaunKulesa/Texture-Atlas/blob/main/Texture_Atlas-0.1.5.tar.gz',    # I explain this later on
  keywords = ['Texture Atlas'],
  install_requires=[
          'pillow',
          'rectpack',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.9',
  ],
)