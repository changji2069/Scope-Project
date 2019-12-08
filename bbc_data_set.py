import scipy
import scipy.io.mmread
from pathlib import Path


filename = Path('bbc_dataset/bbc.mtx')
output_matrix = scipy.io.mmread(filename)
print(output_matrix)