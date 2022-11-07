import config as test_config
from core import runner


def test_api_connection():
    info = runner.YouSync(test_config).run()
