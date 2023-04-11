import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def exact_solution(p: float, x: np.array) -> float:
        alpha = 1 - p
        loc = (x.mean() - 0.5) / 512.0
        scale = 1 / (512.0 * len(x))
        return gamma.ppf(alpha / 2, len(x), loc=loc, scale=scale), \
               gamma.ppf(1 - alpha / 2, len(x), loc=loc, scale=scale)

