# <-*- encoding:utf-8 -*->
"""
    The main function of HMN4QA
    COLING2016 - Hierarchical Memory Networks for Answer Selection on Unknown Words
"""
import model
import numpy
import config
import time
numpy.random.seed(0)
__author__ = '[jacoxu](https://github.com/jacoxu) & [shin](https://github.com/shincling)'


def main():
    # load the external configuration
    config.init_config()
    print("Go to model")
    print '*' * 80

    _log_file = open(config.log_file_pre + time.strftime("_%Y_%m_%d_%H%M%S", time.localtime()), 'w')

    # record current configuration
    config.log_config(_log_file)
    # initialize model
    hmn4qa_model = model.Model(_log_file)
    # train
    hmn4qa_model.train(n_epochs=config.max_epoch, shuffle_batch=config.shuffle_batch)

    _log_file.close()
if __name__ == '__main__':
    main()
