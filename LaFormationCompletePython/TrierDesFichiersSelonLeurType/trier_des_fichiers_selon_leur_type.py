import os
from glob import glob
import shutil

# os.rename('fichier1.txt', 'test\\fichier2.txt')
shutil.move("fichier1.txt", "test\\")
