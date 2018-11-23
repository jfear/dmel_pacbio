import os
import pandas as pd
import collections
import yaml
from snakemake.io import expand
from lcdblib.snakemake.helpers import fill_patterns

HERE = os.path.abspath(os.path.dirname(__file__))


def load_yaml(fname):
    with open(fname) as fh:
        return yaml.load(fh)


class SeqConfig(object):
    def __init__(self, config, patterns, workdir='.'):
        """
        This class takes care of common tasks related to config and patterns
        files (reading the sampletable, etc).

        Parameters
        ----------
        config : str or dict

        patterns : str
            Path to patterns YAML file

        """

        self.config = load_yaml(config)
        self.sampletable = pd.read_csv(self.config['sampletable'], sep='\t')

        self.runs = self.sampletable['run'].tolist()
        self.samples = self.sampletable['sample'].tolist()
        self.patterns = load_yaml(patterns)

        self.fill = self.config.copy()
        self.fill.update(self.sampletable.to_dict('list'))

        self.targets = fill_patterns(self.patterns, self.fill)



if __name__ == '__main__':
    from pprint import pprint
    os.chdir('../../pacbio-wf')
    res = SeqConfig('config/config.yaml', 'config/patterns.yaml')
    pprint(res.targets)
