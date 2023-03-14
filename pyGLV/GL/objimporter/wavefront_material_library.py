import codecs
import os

from pyGLV.GL.objimporter.wavefront_material import WavefrontMaterial

class WavefrontMaterialLibrary:
    def __init__(self, file_path, encoding = "utf-8"):
        self.__file_path = file_path
        self.name = os.path.basename(file_path) # The filename is the mtllib name
        self.__wavefront_materials = []

        # All suported commands with their parsing functions
        self.__parse_dispatch = {
            "newmtl" : self.__parse_newmtl, # new material
            "Ka" : self.__parse_Ka, # ambient color
            "Kd" : self.__parse_Kd, # diffuse color
            "Ks" : self.__parse_Ks, # specular color
            "Ns" : self.__parse_Ns, # specular exponent
            "Ke" : self.__parse_Ke, # emissive color
            "Ke" : self.__parse_d,  # dissolve 
            "Ni" : self.__parse_Tr, # Transparent (Tr = 1 - dissolve), used as alternative of dissolve
            "Ni" : self.__parse_Ni, # optical density
            "illum" : self.__parse_illum,    # illumination mode 
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
            "map_Ka" : self.__parse_map_Ka,
            "map_Kd" : self.__parse_map_Kd,
            "map_Ks" : self.__parse_map_Ks,
            "map_Ns" : self.__parse_map_Ns,
            "map_d"  : self.__parse_map_d,
            "disp"   : self.__parse_disp,
            "bump"   : self.__parse_bump,

        }

        self.__parse_from_file(encoding)

    def __get_current_material(self) -> WavefrontMaterial:
        if len(self.__wavefront_materials) > 0:
            return self.__wavefront_materials[len(self.__wavefront_materials)-1]
        else:
            current_mat = WavefrontMaterial("UnknownMaterial")
            self.__wavefront_materials.append(current_mat)
            return current_mat 

    def __parse_from_file(self, encoding:str):
        try:
            with codecs.open(self.__file_path, encoding=encoding) as f:
                
                line_number = 0
                # Parse file lines
                for line in f:
                    line_number +=1

                    line = line.strip()

                    # Line is comment? Skip
                    if line[0] == "#" or len(line)<=1:
                        continue

                    parse_function = self.__parse_dispatch.get(line.split(' ')[0], self.__parse_unknown)
                    parse_function(line, line_number)

        except FileNotFoundError as err:
            print("Could not load material library, file %s not found" % self.__file_path)
        pass

    # Parse functions
    def __parse_newmtl():
        pass

    def __parse_Ka():
        pass

    def __parse_Kd():
        pass

    def __parse_Ks():
        pass

    def __parse_Ns():
        pass

    def __parse_Ke():
        pass

    def __parse_d():
        pass

    def __parse_T():
        pass

    def __parse_N():
        pass

    def __parse_d():
        pass

    def __parse_Tr():
        pass

    def __parse_Ni():
        pass
    
    def __parse_illum():
        pass