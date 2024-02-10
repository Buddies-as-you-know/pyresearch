import hydra
from omegaconf import OmegaConf
from loguru import logger
from config.conf import MyConfig


@hydra.main(config_name="config", version_base=None, config_path="config/Yaml/")
def main(cfg: MyConfig) -> None:
    logger.info(cfg)

if __name__ == "__main__":
    main()
