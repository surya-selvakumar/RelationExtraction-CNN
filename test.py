import torch
from transformers import AutoTokenizer
import argparse
from config_reader import process_configs
from src import input_reader
from src.tab_trainer import TableFTrainer
from args import eval_argparser
import json



def test_run(run_args):
    trainer = TableFTrainer(run_args)
    trainer.eval(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                 input_reader_cls=input_reader.JsonInputReader)
    


def run_test():
    arg_parser = eval_argparser()
    print(arg_parser)
    process_configs(target=test_run, arg_parser=arg_parser)



if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(add_help=False)
    args, _ = arg_parser.parse_known_args()

    run_test()



