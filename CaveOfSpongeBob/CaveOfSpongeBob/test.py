from pathlib import Path
import os 
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

print("BASE_DIR:{}".format(BASE_DIR))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, r'apps\static'),
)

print(STATICFILES_DIRS)