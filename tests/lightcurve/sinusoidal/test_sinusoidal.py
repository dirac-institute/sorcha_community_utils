from sorcha_community_utils.lightcurve.sinusoidal.sinusoidal_lightcurve import SinusoidalLightCurve
import pandas as pd


def test_sinusoidal_lightcurve_name():
    assert "sinusoidal" == SinusoidalLightCurve.name_id()


def test_compute_simple():
    data_dict = {
        "FieldMJD": [0],
        "LCA": [1],
        "Period": [1],
        "Time0": [0],
    }

    df = pd.DataFrame.from_dict(data_dict)

    model = SinusoidalLightCurve()
    output = model.compute(df)

    assert output.values[0] == 0
