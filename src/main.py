from logging import getLogger

import hydra
from omegaconf import OmegaConf

from config.config import MyConfig

logger = getLogger(__name__)


@hydra.main(
    config_name="config", version_base=None, config_path="config/Yaml/"
)
def main(cfg: MyConfig) -> None:
    logger.info(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    main()
