# Stubs for pandas.plotting._matplotlib (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# pylint: disable=unused-import,useless-import-alias,unused-argument

from typing import Any

from pandas.plotting._matplotlib.boxplot import boxplot as boxplot
from pandas.plotting._matplotlib.boxplot import boxplot_frame as boxplot_frame
from pandas.plotting._matplotlib.boxplot import (
    boxplot_frame_groupby as boxplot_frame_groupby,
)
from pandas.plotting._matplotlib.converter import deregister as deregister
from pandas.plotting._matplotlib.converter import register as register
from pandas.plotting._matplotlib.hist import hist_frame as hist_frame
from pandas.plotting._matplotlib.hist import hist_series as hist_series
from pandas.plotting._matplotlib.misc import andrews_curves as andrews_curves
from pandas.plotting._matplotlib.misc import (
    autocorrelation_plot as autocorrelation_plot,
)
from pandas.plotting._matplotlib.misc import bootstrap_plot as bootstrap_plot
from pandas.plotting._matplotlib.misc import lag_plot as lag_plot
from pandas.plotting._matplotlib.misc import (
    parallel_coordinates as parallel_coordinates,
)
from pandas.plotting._matplotlib.misc import radviz as radviz
from pandas.plotting._matplotlib.misc import scatter_matrix as scatter_matrix
from pandas.plotting._matplotlib.timeseries import tsplot as tsplot
from pandas.plotting._matplotlib.tools import table as table


def plot(data: Any, kind: Any, **kwargs: Any) -> Any:
    ...
