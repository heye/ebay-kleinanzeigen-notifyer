
from typing import Dict, Tuple, List
import os
import traceback


class FileStorage:
        
    def __init__(self):
        self.channel = ""
        self.temp_path = "temp/"


    def setup(self, channel = ""):
        self.channel = channel
        try:
            os.mkdir(self.temp_path)
        except FileExistsError:
            return
        except:
            traceback.print_exc()

            
    #add data to a temporary file
    def write_file(self, data: str) -> bool:
        result = False

        try:    
            file_path = self.temp_path + self.channel + ".txt"

            #print("STORAGE WRITE " + file_path)

            with open(file_path, 'w+') as temp_file:
                temp_file.write(data)
                result = True
        except:
            traceback.print_exc()
        
        return result


    def append_file(self, data: str) -> bool:
        result = False

        try:    
            file_path = self.temp_path + self.channel + ".txt"

            #print("STORAGE APPEND " + file_path)

            with open(file_path, 'a+') as temp_file:
                temp_file.write(data)
                result = True
        except:
            traceback.print_exc()
        
        return result


    def read_file(self) -> bytes:
        data = ""

        try:
            file_path = self.temp_path + self.channel + ".txt"

            if not os.path.isfile(file_path):
                return data

            #print("STORAGE READ " + file_path)
        
            with open(file_path, 'r+') as temp_file:
                data = temp_file.read()
        except:
            traceback.print_exc()
        return data


