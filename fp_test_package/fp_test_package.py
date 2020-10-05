from helpers.arguments_checkers import *
from helpers.utility_functions import *
from utils.TqdmLoggingHandler import TqdmLoggingHandler
from utils.CustomLogger import CustomLogger
from tqdm import *
from time import sleep


def main():
  log = CustomLogger(__name__).logger
  
  args = fetch_arguments()
  args = check_arguments_conflicts(args, log)

  log.info("################ SCRIPT INIT ################\n")

  log.info('Csv will be written at {export_path}.\n\nSecond argument: {second_argument}\n\nThird argument: {third_argument}\n\n'.format(**args))

  dummy_list = [['foo_value1', 'bar_value1'], ['foo_value2','bar_value2']]
  df = make_df_to_write(dummy_list, ['foo', 'bar'])

  log.info("Writing your csv with dummy data\n")

  #Dummy fake loading
  for i in tqdm(range(30), leave=False, ncols=150, desc="Dummy Loading", position=0):
    sleep(0.1)
    pass

  write_csv(df, ['foo', 'bar'], args['export_path'])

  log.info("################ EXITING SUCCESSFULLY ################\n")

if __name__ == "__main__":
  main()

