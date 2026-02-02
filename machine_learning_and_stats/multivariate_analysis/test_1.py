import os
import cmdstanpy
cmdstanpy.install_cmdstan()
from cmdstanpy import cmdstan_path, CmdStanModel
stan_file = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.stan')

model = CmdStanModel(stan_file='sample_model.stan')

# データの作成
front_and_back_list = [1,0,1,0,0,0,0,0,1,0]
data = {
    "N" : len(front_and_back_list),
    "y" : front_and_back_list
    }


data_file = os.path.join(cmdstan_path(), 'examples', 'bernoulli', 'bernoulli.data.json')

fit = model.sample(data=data_file)