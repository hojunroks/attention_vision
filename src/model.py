import pytorch_lightning as pl
import torch.nn as nn

class AttentionClassifier(pl.LightningModule):
    def __init__(self):
        super().__init__()

    def forward(self):
        pass

    def training_step(self):
        pass

    def validation_step(self):
        pass

    def configure_optimizers(self):
        pass

    @staticmethod
    def add_model_specific_args(self):
        pass


class