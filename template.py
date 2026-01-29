import os
from pathlib import Path
import logging

list_of_files =[
    "QAWithCustomData/__init__.py",
    "QAWithCustomData/data_ingestion.py",
    "QAWithCustomData/embedding.py",
    "QAWithCustomData/model_api.py",
    "StreamlitApp.py",
    "setup.py",
    "logger.py",
    "exception.py",
]

for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Created directory: {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")
   else:
      logging.info(f"File already exists: {filepath} and is not empty")
