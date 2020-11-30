import torch.nn as nn
from src.submodels import ResNetEncoder


def get_transformer_encoder(d_model, nhead, num_layers, norm=None):
    ############################################################
    # Creates and returns a transformer encoder
    # d_model: The dimension of the encoder input
    # nhead: Number of heads for multihead attention
    # num_layers: The number of encoder layers for the encoder
    # norm: The layer normalization component
    ############################################################
    encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
    return nn.TransformerEncoder(encoder_layer=encoder_layer, num_layers=num_layers, norm=norm)


def get_resnet18_encoder(in_channels=3):
    return ResNetEncoder(in_channels=in_channels)