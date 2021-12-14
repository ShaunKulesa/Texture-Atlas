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
    | Adds a texture to the texture atlas.
    * image_path: string
    * width: integer
    * height: integer

* def add_textures(images):
    | Adds multiple textures to the texture atlas.
    * images: [[path: string, width: integer, height: integer]]
    
* remove_texture(image_path):
    | Removes a specific texture from the texture atlas.
    * image_path: 

* remove_textures(textures: list)
    * not made yet

* resize_texture(image_path, width, height)
    * image_path: string
    * width: integer 
    * height: integer

* resize(width, height):
    | Resizes the texture atlas.
    * width: int 
    * height: int
    
* get_texture_position(image_path)
    | Returns a list of a texture's x, y, width and height.
    * image_path: str
    
* all_texture_positions():
    | Returns a dictionary of all the textures and their positions.
