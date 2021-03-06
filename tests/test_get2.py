
# test_get2
from ie_pandas import DataFrame
import numpy as np

# Define test to get more than one item
def test_get():

	dictionary = {
    		"pet": np.array(["cat", "dog", "mouse"]),
    		"age": np.array([1, 2, 3]),
    		"weight": np.array([1.0, 2.0, 3.0]),
		"sick": np.array([True, True, False]),
		}

  group0 = ["cat","dog"]

	df=DataFrame(dictionary)

	assert df[["pet"]][0:2] == group0
