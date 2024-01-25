from pydantic import BaseModel


class ModelConfig(BaseModel):
    name: str = "bert"
    input_max_length: int = 32


class TrainConfig(BaseModel):
    lr: float = 1e-5
    epochs: int = 10
    batch_size: int = 16


class MyConfig(BaseModel):
    models_cfg: ModelConfig = ModelConfig()
    train_cfg: TrainConfig = TrainConfig()
    data_dir: str = ""
    output_dir: str = ""
