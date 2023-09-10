import yaml
from .PATHS import PROJECT_PATH
from box import Box

with open(PROJECT_PATH / "config.yaml", "r") as file:
    cfg = yaml.load(file, Loader=yaml.FullLoader)
cfg = Box(cfg)
