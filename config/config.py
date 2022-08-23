import yaml
from yaml import Loader

from consts.paths import ABSOLUTE_PATH_YAML

with open(ABSOLUTE_PATH_YAML, "r") as yaml_file:
    CONFIG = yaml.load(yaml_file, Loader=Loader)

ENV_NAME = CONFIG["env"]["env_name"]
TOPIC = CONFIG["kafka"]["topic"]
BOOTSTRAP_SERVERS = CONFIG["kafka"]["bootstrap_servers"]
IS_ALIVE_URL = CONFIG["url"]["is_alive_url"]
API_TODOS_URL = CONFIG["url"]["api_todos_url"]
POST_REQUEST_BODY = CONFIG["request_body"]["post"]
