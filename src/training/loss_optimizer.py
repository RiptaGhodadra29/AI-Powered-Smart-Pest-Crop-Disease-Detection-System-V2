import torch.nn as nn
import torch.optim as optim


def get_loss_function():
    """
    Create loss function.
    """

    return nn.CrossEntropyLoss()


def get_optimizer(
    model,
    learning_rate=0.001
):
    """
    Create optimizer.
    """

    return optim.AdamW(
        model.parameters(),
        lr=learning_rate
    )