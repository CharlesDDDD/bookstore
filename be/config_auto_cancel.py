class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': '__main__:auto_cancel',
            'trigger': 'interval',    # 间隔执行
            'seconds': 5,

        }

    ]