from pathlib import Path


class DatasetValidator:
    """
    Validates dataset structure before training.
    """

    SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

    def __init__(self, dataset_root: str):
        self.dataset_root = Path(dataset_root)

    def validate_split(self, split_name: str):
        split_path = self.dataset_root / split_name

        if not split_path.exists():
            raise FileNotFoundError(
                f"{split_name} folder not found: {split_path}"
            )

        class_folders = [
            folder
            for folder in split_path.iterdir()
            if folder.is_dir()
        ]

        if len(class_folders) == 0:
            raise ValueError(
                f"No class folders found in {split_name}"
            )

        print(f"\n{split_name.upper()}")

        total_images = 0

        for class_folder in sorted(class_folders):

            images = [
                image
                for image in class_folder.iterdir()
                if image.suffix.lower()
                in self.SUPPORTED_EXTENSIONS
            ]

            image_count = len(images)

            if image_count == 0:
                raise ValueError(
                    f"Empty class folder: {class_folder.name}"
                )

            total_images += image_count

            print(
                f"{class_folder.name}: "
                f"{image_count} images"
            )

        print(
            f"\nTotal Images in {split_name}: "
            f"{total_images}"
        )

    def validate(self):
        print("\nDataset Validation Started")

        self.validate_split("train")
        self.validate_split("validation")
        self.validate_split("test")

        print("\nDataset Validation Passed")