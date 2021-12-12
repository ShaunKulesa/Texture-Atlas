Install
-------
.. code-block:: py

    pip install Texture-Atlas

Example
-------
.. code-block:: py

    from TextureAtlas import Atlas

    atlas = Atlas(1000, 1000)
    atlas.add_textures([['image1.png', 100, 100], ['image2.png', 200, 200], ['image3.png', 100, 100]])
    atlas.save_as("atlas.png")

Atlas
-----

* add_texture(image_path, width, height)
    * image_path: string
    * width: integer
    * height: integer

* def add_textures(self, images):
    * images: list 
        | [['1.png', 100, 100], ['2.png', 200, 200]]
