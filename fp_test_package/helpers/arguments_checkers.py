import argparse, sys, re, os
import dateutil.parser as dateparser
from dateutil import tz
from .utility_functions import *

def fetch_arguments():
  ap = argparse.ArgumentParser()
  ap.add_argument("-ep", "--export_path", required=True, help="Export path where to write the csv file. Required.")
  ap.add_argument("-sa", "--second_argument", required=False, help="Second argument. Not required. If set, must be one of the following: [\"foo\", \"bar\", \"go\"]. Default is \"foo\"", default="foo")
  ap.add_argument("-ta", "--third_argument", required=False, help="Third argument. Not required. Entere whatever you want to print as third argument. Default is \"tharg\"", default="tharg")
  return vars(ap.parse_args())

def check_csv_valid_filename(filename):
  if not is_csv(filename):
    raise argparse.ArgumentTypeError(f"\n\n\t\"{filename}\" is not a valid path where to store the retrieved data. It must be a csv file")
  return filename

def check_arguments_conflicts(args, log):
  args['log'] = log
  check_csv_valid_filename(args['export_path']) 
  if args['second_argument'] not in ['foo', 'bar', 'go']:
    sys.exit("\Second argument, if set, must be one of the following: [\"foo\", \"bar\", \"go\"]")
  return args
