from PIL import Image
from rectpack import newPacker, SORT_NONE

class Atlas():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.atlas = Image.new("RGBA", (width, height))
        self.textures = {}

    def add_texture(self, image_path: str, width: int, height: int):
        '''
        Adds a texture to the texture atlas.
            * image_path: string
            * width: integer
            * height: integer
        '''

        self.textures[image_path] = [None, None, width, height]
        self._organise()
    
    def add_textures(self, images: list):
        '''
        Adds multiple textures to the texture atlas.
            * images: [[path: string, width: integer, height: integer]]
        '''

        for texture in images:
            self.textures[texture[0]] = (None, None, texture[1], texture[2])        
        self._organise()
    
    def remove_texture(self, image_path: str):
        '''
        Removes a specific texture from the texture atlas.
            * image_path: string
        '''

        self.textures.pop(image_path, None)
        self._organise()
    
    def remove_textures(self, textures: list):
        '''
        Removes multiple specific textures from the texture atlas.
            * textures: [texture_name: string]
        '''
    
    def resize_texture(self, image_path: str, width: int, height: int):
        '''
        Resizes a specific texture in the texture atlas.
            * image_path: string
            * width: integer 
            * height: integer
        '''

        if image_path in self.textures:
            self.textures[image_path][2] = width
            self.textures[image_path][3] = height
            self._organise()
    
    def resize(self, width: int, height: int):
        '''
        Resizes the texture atlas.
            * width: integer
            * height: integer
        '''

        self.width = width
        self.height = height
        self._organise()
    
    def get_texture_position(self, image_path: str):
        '''
        Returns a list of a texture's x, y, width and height.
            * image_path: string
        '''

        return self.textures[image_path]
    
    def all_texture_positions(self):
        '''
        Returns a dictionary of all the textures and their positions.
        '''

        return self.textures
    
    def save_as(self, output_name: str):
        '''
        Saves the texture atlas as an image file.
            * output_name: string
        '''

        self.atlas.save(output_name)
    
    def get_pillow_output(self):
        '''
        Returns the texture atlas in the form of PIL.Image.
        '''

        return self.atlas
    
    def get_size(self):
        '''
        Returns a list of the width and height of the texture atlas.
        '''
        return [self.width, self.height]

    def clear(self):
        '''
        Clears all textures from the texture atlas.
        '''
        self.atlas.close()
        self.atlas = Image.new("RGBA", (self.width, self.height))

    def _organise(self):
        self.atlas.close()

        self.atlas = Image.new("RGBA", (self.width, self.height))
        bins = [(self.width, self.height)]

        packer = newPacker(rotation=False, sort_algo=SORT_NONE)

        for r in self.textures:
            packer.add_rect(self.textures.get(r)[2], self.textures.get(r)[3])

        for b in bins:
            packer.add_bin(*b)

        packer.pack()

        output = []

        dict_index = 0
        texture_index = 0

        for index, abin in enumerate(packer):
            bw, bh  = abin.width, abin.height
            for rect in abin:
                x, y, w, h = rect.x, rect.y, rect.width, rect.height
                for texture in self.textures:
                    if dict_index == texture_index:
                        self.textures[texture] = [x, y, w, h]
                        image = Image.open(texture)
                        image = image.resize((self.textures[texture][2], self.textures[texture][3]))
                        self.atlas.paste(image, (self.textures[texture][0], self.textures[texture][1]))
                        dict_index = 0
                        break
                    dict_index += 1
                texture_index += 1