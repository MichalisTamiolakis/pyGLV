import numpy as np

class WavefrontMaterial:
    def __init__(self, name):
        self.name = name
        
        # Color related values
        self.ambient_color = [1.0, 1.0, 1.0] # RGB ambient color value
        
        self.diffuse_color = [1.0, 1.0, 1.0] # RGB diffuse color value
        
        self.sepcular_color = [0.0, 0.0, 0.0] # RGB sepcular color value
        self.specular_exponent = 10.0 # between 0 and 1000. Weight for the specular color
        
        self.dissolve = 1 # between 0 and 1. 0 being fully transparent, while 1 being fully opaque

        # Texture related values

        # Illumination mode:
        # 0. Color on and Ambient off
        # 1. Color on and Ambient on
        # 2. Highlight on
        # 3. Reflection on and Ray trace on
        # 4. Transparency: Glass on, Reflection: Ray trace on
        # 5. Reflection: Fresnel on and Ray trace on
        # 6. Transparency: Refraction on, Reflection: Fresnel off and Ray trace on
        # 7. Transparency: Refraction on, Reflection: Fresnel on and Ray trace on
        # 8. Reflection on and Ray trace off
        # 9. Transparency: Glass on, Reflection: Ray trace off
        # 10. Casts shadows onto invisible surfaces
        self.illumination_mode = 1