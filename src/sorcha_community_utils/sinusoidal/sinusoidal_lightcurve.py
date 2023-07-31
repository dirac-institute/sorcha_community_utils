from sorcha.lightcurves.base_lightcurve import AbstractLightCurve

from typing import List
import pandas as pd
import numpy as np


class SinusoidalLightCurve(AbstractLightCurve):
    """
    Note: assuming sinusoidal in magnitude instead of flux. Maybe not call LCA?
    """

    def __init__(self, required_column_names: List[str] = ["FieldMJD", "LCA", "Period", "Time0"]) -> None:
        super().__init__(required_column_names)

    def compute(self, df: pd.DataFrame) -> np.array:
        """
        Computes a sinusoidal light curve given the input dataframe
        """

        self._validate_column_names(df)

        modtime = np.mod(df["FieldMJD"] / df["Period"] + df["Time0"], 2 * np.pi)
        return df["LCA"] * np.sin(modtime)

    @staticmethod
    def name_id() -> str:
        return "sinusoidal"
