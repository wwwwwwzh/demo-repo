# models.py
import json

class DataLoader:
    """
    Simple JSON data loader with loading and preprocessing.
    """

    def __init__(self, data_path):
        """
        Args:
            data_path (str): Path to the JSON file to load.
        """
        self.data_path = data_path
        self.data = None

    def load_data(self):
        """
        Load JSON data from self.data_path into self.data.
        
        Returns:
            The loaded Python object (usually list or dict).
        """
        with open(self.data_path, 'r') as f:
            self.data = json.load(f)
        return self.data

    def preprocess_data(self):
        """
        Example preprocessing step: filter items with 'processed': True.
        
        Returns:
            A list of filtered items.
        """
        if self.data is None:
            # ensure data is loaded first
            self.load_data()
        return [item for item in self.data if item.get('processed', False)]
