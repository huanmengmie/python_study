# -*- coding:utf-8 -*-
import logging


def root_log():
    """
    直接使用logging，最顶级的log
    默认情况下，Debug和Info的等级太低，控制台不会打印
     """
    logging.log(logging.DEBUG, "DEBUG")
    logging.log(logging.INFO, "INFO")
    logging.log(logging.WARNING, "WARNING")
    # WARNING:root:WARNING
    logging.log(logging.ERROR, "ERROR")
    # ERROR:root:ERROR
    logging.log(logging.CRITICAL, "CRITICAL")
    # CRITICAL:root:CRITICAL


def name_log(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")

if __name__ == '__main__':
    # root_log()
    name_log("2343")
    pass
