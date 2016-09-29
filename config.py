# <-*- encoding:utf8 -*->

"""
    Configuration Profile
"""
import time
import ConfigParser

__author__ = 'jacoxu & shin'

# External configuration file
config_file = './config.cfg'
# Record log into this file, such as: hmn4qa_output.log_2016_09_28_114503
log_file_pre = "./hmn4qa_output.log"
# k of k-max pooling, 1, 2, 3, ..., -1
top_k = 2
# set the max epoch of training
max_epoch = 500
# Choose the word segmentation mode
is_blank_split = True
# max length of each sentence in Story/Query
max_sent_enc = 100
# max number of sentence in Story
max_seq_story = 100
max_sent_dec = 100

# data path
# Air-Ticket (CH): ./datasets/task_01*_{}.txt
# Hotel (CH): ./datasets/task_02*_{}.txt
# Air-Ticket (EN): ./datasets/task_03*_{}.txt
# Hotel (EN): ./datasets/task_04*_{}.txt
# Total: ./datasets/task_*_{}.txt
data_path = "./datasets/task_*_{}.txt"

# temporal encoding
enable_time = True
# set the hop number
n_hops = 3
# Batch size
batch_size = 32
# hidden dimension
embed_size = 100
opt_rule = 'SGD'
# initial learning rate
init_lr = 0.01
normal_std = 0.1
lrate_decay_step = 15
max_decay_step = 60
max_norm = 40

stop_iter_dev = 4
shuffle_batch = True


def init_config():
    _config = ConfigParser.ConfigParser()
    cfg_file = open(config_file, 'r')
    _config.readfp(cfg_file)
    global data_path
    data_path = _config.get('cfg', 'data_path').strip()
    global max_epoch
    max_epoch = eval(_config.get('cfg', 'max_epoch').strip())
    global batch_size
    batch_size = eval(_config.get('cfg', 'batch_size').strip())
    global top_k
    top_k = eval(_config.get('cfg', 'top_k').strip())
    global embed_size
    embed_size = eval(_config.get('cfg', 'embed_size'))
    global init_lr
    init_lr = eval(_config.get('cfg', 'init_lr').strip())
    cfg_file.close()


def log_config(_log_file):
    _log_file.write('*' * 80 + '\n')
    _log_file.write('current time:' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
    _log_file.write('config.data_path: ' + data_path + '\n')
    _log_file.write('config.enable_time: ' + str(enable_time) + '\n')
    _log_file.write('config.n_hops: ' + str(n_hops) + '\n')
    _log_file.write('config.top_k: ' + str(top_k) + '\n')
    _log_file.write('config.batch_size: ' + str(batch_size) + '\n')
    _log_file.write('config.embed_size: ' + str(embed_size) + '\n')
    _log_file.write('config.opt_rule: ' + opt_rule + '\n')
    _log_file.write('config.init_lr: ' + str(init_lr) + '\n')
    _log_file.write('config.normal_std: ' + str(normal_std) + '\n')
    _log_file.write('config.max_epoch: ' + str(max_epoch) + '\n')
    _log_file.write('config.lrate_decay_step: ' + str(lrate_decay_step) + '\n')
    _log_file.write('config.max_decay_step: ' + str(max_decay_step) + '\n')
    _log_file.write('config.max_norm: ' + str(max_norm) + '\n')

    _log_file.write('*' * 80 + '\n')
    _log_file.flush()
