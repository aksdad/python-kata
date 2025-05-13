import tomllib
from dsa import generateDSAFile
import os

with open('config.toml', 'rb') as file:
    config = tomllib.load(file)
    print(config["dsa"])

    if not os.path.isdir(os.getcwd() + '/day1'):
        os.makedirs(os.getcwd() + '/day1')
    dsa_list = [k for k, v in config['dsa'].items() if v] # Get enabled DSA items

    for algo in dsa_list:
        generateDSAFile(algo, config[algo]["signature"], os.getcwd() + '/day1')
