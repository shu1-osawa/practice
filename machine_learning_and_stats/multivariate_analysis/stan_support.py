'''
 stan_support.py
 STANのモデルを生成したりサンプリングを行うための支援をする
  Created on 2022/2/23
  @author: Shuichi OHSAWA
'''
from distutils.command.install_egg_info import safe_version
from cmdstanpy import  CmdStanModel
import arviz as az
#from tarpan.cmdstanpy.traceplot import save_traceplot
import matplotlib.pyplot as plt

class Stan_model():

    def __init__(self, stan_file_path):
        self.model = CmdStanModel(stan_file=stan_file_path)

    def fit(self, data, iter_sampling=1000, iter_warmup=500,chains=4):
        self.chains = chains
        self.fit_sm = self.model.sample(data=data,
                                        iter_sampling=iter_sampling,
                                        iter_warmup = iter_warmup,
                                        chains = self.chains,
                                        seed=1234)

    def diagnose(self):
        sa = self.fit_sm.stan_variables()
        print(la2)
        la2.to_csv('csv.csv')
        for i, k in enumerate(la.keys()):
            print(f'{k} = {la[k].mean()}')
            print(la[k])
            #print(la2[:,i,:].shape)
            print(f'{k}_shape = {la[k].shape}')
            #plt.plot(la[k])
            plt.plot(la2)
            plt.ylim(-2, 3)
            plt.show()
        samples = az.from_cmdstanpy(posterior = self.fit_sm)
        print(self.fit_sm.draws())
        print(self.fit_sm.diagnose())
        print(az.rhat(samples))
        print(az.summary(samples))
        print(la2.shape)

        self.fit_sm.save_csvfiles(dir='test_stan_csv')
        #save_traceplot(fit, param_names=['mu', 'tau', 'eta.1'])

  