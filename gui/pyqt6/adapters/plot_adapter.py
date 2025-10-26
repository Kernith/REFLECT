import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from backend.visualization.plot_factory import PlotFactory
from backend.visualization.color_manager import ColorManager


class PyQt6PlotAdapter:
    """Adapter to convert matplotlib Figures to PyQt6 MplCanvas widgets"""
    
    def __init__(self, plot_factory: PlotFactory):
        self.plot_factory = plot_factory
    
    def create_time_series_canvas(self, df: pd.DataFrame, color_manager: ColorManager) -> FigureCanvas:
        """Create time series plot as FigureCanvas widget"""
        fig = self.plot_factory.create_time_series_plot(df, color_manager)
        return FigureCanvas(fig)
    
    def create_category_distribution_canvas(self, df: pd.DataFrame, color_manager: ColorManager) -> FigureCanvas:
        """Create category distribution plot as FigureCanvas widget"""
        fig = self.plot_factory.create_category_distribution_plot(df, color_manager)
        return FigureCanvas(fig)
