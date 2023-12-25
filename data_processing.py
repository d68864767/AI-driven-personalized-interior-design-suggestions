```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.scaler = StandardScaler()

    def load_data(self):
        """
        Load the data from the given path
        """
        self.data = pd.read_csv(self.data_path)

    def preprocess_data(self):
        """
        Preprocess the data: handle missing values, outliers, and scale the data
        """
        # Handle missing values
        self.data = self.data.fillna(self.data.mean())

        # Handle outliers
        self.data = self.data[(self.data - self.data.mean()).abs() <= 3*self.data.std()]

        # Scale the data
        self.data = self.scaler.fit_transform(self.data)

    def get_data(self):
        """
        Return the preprocessed data
        """
        return self.data
```
