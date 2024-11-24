# Weighted Average Filter

This project implements a weighted average filter that processes a digitized signal. The filter computes a weighted sum average of the last `n` values of the signal. This example demonstrates the filter using a sine wave signal.

## Features

- Process a signal and compute the weighted sum average of the last `n` values.
- Demonstration with a sine wave signal.
- Visualization of the original and filtered signals using Matplotlib.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/-Tholokuhle-2024-/project-2.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project-2
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Example Code

Here's an example of how to use the `WeightedAverage` class:

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List

class WeightedAverage:
    def __init__(self, w: List[float]):
        """
        Initialize the WeightedAverage with a list of weights.
        :param w: List of weights where w[0] is the weight for the most recent value.
        """
        self.w = w
        self.n = len(w)
        self.buffer = []

    def process(self, x: float) -> float:
        """
        Process a new signal value and return the weighted average of the last n values.
        :param x: The current signal value.
        :return: The weighted average.
        """
        # Add the new value to the buffer
        self.buffer.insert(0, x)
        
        # Ensure the buffer contains only the last n values
        if len(self.buffer) > self.n:
            self.buffer.pop()
        
        # Compute the weighted sum average
        weighted_sum = sum(self.w[i] * self.buffer[i] for i in range(len(self.buffer)))
        average = weighted_sum / self.n
        return average

# Generate a sine wave signal
t = np.linspace(0, 2 * np.pi, 100)  # 100 sample points for smoothness
sine_wave = np.sin(t)

# Initialize the WeightedAverage with equal weights (moving average)
weights = [1, 1, 1, 1, 1]  # Equal weights
weighted_average_filter = WeightedAverage(weights)

# Process the sine wave and compute the moving average
results = [weighted_average_filter.process(x) for x in sine_wave]

# Plot the original sine wave and the processed moving average
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original Sine Wave", color="blue")
plt.plot(t, results, label="Weighted Moving Average", color="red", linestyle="--")
plt.title("Sine Wave and Weighted Moving Average")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
```

### Steps to Run

1. **Initialize the Class**: Create an instance of the `WeightedAverage` class with the desired weights.
    ```python
    weights = [1, 1, 1, 1, 1]  # Example weights
    weighted_average_filter = WeightedAverage(weights)
    ```
2. **Process the Signal**: Call the `process` method for each entry in your signal.
    ```python
    results = [weighted_average_filter.process(x) for x in signal]
    ```
3. **Visualize the Results**: Use Matplotlib to plot the original and filtered signals.
    ```python
    plt.plot(t, original_signal, label="Original Signal")
    plt.plot(t, results, label="Filtered Signal")
    plt.legend()
    plt.show()
    ```

## Customization

- **Change Weights**: You can change the weights by passing a different list of weights when initializing the class.
    ```python
    weights = [0.5, 0.5, 0.5, 0.5, 0.5]  # Example weights
    weighted_average_filter = WeightedAverage(weights)
    ```