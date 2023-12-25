```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

class Model:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def split_data(self):
        """
        Split the data into training and testing sets
        """
        X = self.data.drop('target', axis=1)
        y = self.data['target']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        """
        Train the model using the training data
        """
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """
        Evaluate the model using the testing data
        """
        predictions = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, predictions)
        rmse = np.sqrt(mse)
        return rmse

    def save_model(self, path):
        """
        Save the trained model to a file
        """
        joblib.dump(self.model, path)

    def load_model(self, path):
        """
        Load a trained model from a file
        """
        self.model = joblib.load(path)

    def predict(self, input_data):
        """
        Predict the output for a given input
        """
        return self.model.predict(input_data)
```
