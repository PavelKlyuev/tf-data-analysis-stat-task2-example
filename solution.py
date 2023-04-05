import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return expon.ppf(alpha / 2) / len(x) * x.min(), \
           expon.ppf(1 - alpha / 2) / len(x) * len(x) * x.min()
