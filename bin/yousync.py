import config
from core import runner

if __name__ == '__main__':
    ys = runner.YouSync(config)
    ys.run()
