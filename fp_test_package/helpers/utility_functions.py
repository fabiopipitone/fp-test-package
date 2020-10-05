import os, logging, getpass, sys
import dateutil.parser as dateparser
import pandas as pd

def make_df_to_write(data_list, headers):
  df = pd.DataFrame(data_list, columns=headers)
  return df