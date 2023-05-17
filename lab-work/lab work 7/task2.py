from multiprocessing import Pool
import numpy as np


def calculate_mean(column):
    return np.mean(df[column])


if __name__ == '__main__':
    columns = ['Total_Spent', 'Order_Count']
    pool = Pool(processes=2)
    results = pool.map(calculate_mean, columns)
