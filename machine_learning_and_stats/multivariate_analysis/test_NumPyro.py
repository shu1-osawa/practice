import subprocess, sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpyro'])

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import jax
import jax.numpy as jnp
import numpyro
sns.set_style("darkgrid")