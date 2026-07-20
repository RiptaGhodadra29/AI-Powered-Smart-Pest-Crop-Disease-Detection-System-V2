from pathlib import Path

from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

from src.data_preparation.transforms import (
    get_train_transforms,
    get_validation_transforms,
    get_test_transforms
)


class AlbumentationsDataset:
    """
    Wrapper to apply Albumentations transforms
    with ImageFolder datasets.
    """

    def __init__(self, dataset, transform=None):
        self.dataset = dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):

        image, label = self.dataset[index]

        import numpy as np

        image = np.array(image)

        if self.transform:
            image = self.transform(
                image=image
            )["image"]

        return image, label


def create_datasets(dataset_root):

    dataset_root = Path(dataset_root)

    train_dataset = ImageFolder(
        dataset_root / "train"
    )

    validation_dataset = ImageFolder(
        dataset_root / "val"
    )

    test_dataset = ImageFolder(
        dataset_root / "test"
    )

    train_dataset = AlbumentationsDataset(
        train_dataset,
        transform=get_train_transforms()
    )

    validation_dataset = AlbumentationsDataset(
        validation_dataset,
        transform=get_validation_transforms()
    )

    test_dataset = AlbumentationsDataset(
        test_dataset,
        transform=get_test_transforms()
    )

    return (
        train_dataset,
        validation_dataset,
        test_dataset
    )


def create_dataloaders(
    dataset_root,
    batch_size=16
):

    (
        train_dataset,
        validation_dataset,
        test_dataset
    ) = create_datasets(
        dataset_root
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    return (
        train_loader,
        validation_loader,
        test_loader
    )