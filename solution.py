import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def exact_solution(p: float, x: np.array) -> float:
    t = 32
    alpha = 1 - p
    return expon.ppf(alpha / 2) / len(x) * (x.min()/t), \
           expon.ppf(1 - alpha / 2) / len(x) * (x.min()/t)

