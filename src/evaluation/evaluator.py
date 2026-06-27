import torch


class Evaluator:
    """
    Evaluate trained model on test dataset.
    """

    def __init__(
        self,
        model,
        dataloader,
        device
    ):
        self.model = model
        self.dataloader = dataloader
        self.device = device

        self.model.to(device)

    def evaluate(self):

        self.model.eval()

        y_true = []
        y_pred = []

        with torch.no_grad():

            for images, labels in self.dataloader:

                images = images.to(
                    self.device
                )

                labels = labels.to(
                    self.device
                )

                outputs = self.model(
                    images
                )

                _, predictions = torch.max(
                    outputs,
                    1
                )

                y_true.extend(
                    labels.cpu().numpy()
                )

                y_pred.extend(
                    predictions.cpu().numpy()
                )

        return (
            y_true,
            y_pred
        )