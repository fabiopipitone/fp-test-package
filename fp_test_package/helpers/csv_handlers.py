import os, sys, glob
import pandas as pd

def write_csv(dataframe, fields_to_export, export_path, exception_message='Something went wrong when writing the csv file from the dataframe.'):
  try: 
    dataframe.to_csv(export_path, index=False, columns=fields_to_export)
  except Exception as e:
    sys.exit(f"{exception_message} Here's the exception: \n\n{e}")