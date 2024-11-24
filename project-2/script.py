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
