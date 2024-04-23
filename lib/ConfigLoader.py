import configparser
from pyspark import SparkConf

def get_config(env):
    config=configparser.ConfigParser()
    config.read("conf/sbdl.conf")
    conf={}
    for (key,value) in config.items(env):
        conf[key]=value
    return conf

def get_spark_conf(env):
    config=configparser.ConfigParser()
    config.read("conf/spark.conf")
    conf={}
    for (key,value) in config.items(env):
        conf[key]=value
    return conf

def get_data_filter(env,data_filter):
    conf=get_config(env)
    return "true" if conf[data_filter] == "" else conf[data_filter]
