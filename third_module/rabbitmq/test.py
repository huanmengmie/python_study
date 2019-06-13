# -*- coding: utf-8 -*-
from python_study.third_module.rabbitmq.subscribe import sub_fanout, sub_direct, sub_topic

if __name__ == '__main__':
    # sub_fanout()
    # sub_direct("b")
    sub_topic("*.b")
