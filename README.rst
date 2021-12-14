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

=====
Atlas
=====

* add_texture(image_path, width, height)
    | Adds a texture to the texture atlas.

    * image_path: string
    * width: integer
    * height: integer

* add_textures(images)
    | Adds multiple textures to the texture atlas.

    * images: [[path: string, width: integer, height: integer]]
    
* remove_texture(image_path)
    | Removes a specific texture from the texture atlas.

    * image_path: string

* remove_textures(textures)
    | Removes multiple specific textures from the texture atlas.

    * textures: [texture_name: string]

* resize_texture(image_path, width, height)
    | Resizes a specific texture in the texture atlas.

    * image_path: string
    * width: integer 
    * height: integer

* resize(width, height)
    | Resizes the texture atlas.

    * width: integer
    * height: integer
    
* get_texture_position(image_path)
    | Returns a list of a texture's x, y, width and height.

    * image_path: string
    
* all_texture_positions()
    | Returns a dictionary of all the textures and their positions.

* save_as(output_name)
    | Saves the texture atlas as an image file.

    * output_name: string

* get_pillow_output()
    | Returns the texture atlas in the form of PIL.Image.

* get_size()
    | Returns a list of the width and height of the texture atlas.

* clear()
    | Clears all textures from the texture atlas.
