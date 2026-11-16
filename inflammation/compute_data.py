"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import numpy as np
import os


from inflammation import models, views

class CSVDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)
        return list(data)

class JSONDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in pah {self.dir_path}")
        data = map(models.load_json, data_file_paths)
        return list(data)



def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    #data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    #if len(data_file_paths) == 0:
      #  raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    #data = map(models.load_csv, data_file_paths)
    data = data_source.load_inflammation_data()


    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    #graph_data = {
     #   'standard deviation by day': daily_standard_deviation,
    #}
    #views.visualize(graph_data)
    return daily_standard_deviation

def load_inflammation_data_old(data_dir):
    """Gets all the inflammation data from CSV files within a directory

    Args:
        data_dir (_type_): direcory for retrieving data

    Raises:
        ValueError: _description_

    Returns:
        list:list of 2D NumPy arrays with inflammation data loaded from all inflammation CSV files found in a specified directory path
    """
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    data = map(models.load_csv, data_file_paths)
    return list(data)