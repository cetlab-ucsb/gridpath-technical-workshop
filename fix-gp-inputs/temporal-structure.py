import os
from glob import glob
import pandas as pd
import numpy as np
import datetime

# input csvs path
input_path = "/Users/meas/Documents/gridpath-0.14.1/db/csvs_sapp_GPv0.14.1_workshop_072022" # directory to pull inputs
output_path = "/Users/meas/Documents/gridpath-0.14.1/db/csvs_reds_102022"

# get temporal files
temporal_path = os.path.join(input_path, "temporal")
temporal_scens = [f.path for f in os.scandir(temporal_path) if f.is_dir()]
out_temporal_scens = [f.replace(input_path, output_path) for f in temporal_scens]

# loop through and fix all temporal files
for i in range(len(temporal_scens)):
    dir = temporal_scens[i]
    period_params_df = pd.read_csv(os.path.join(dir, "period_params.csv"))
    horizon_params_df = pd.read_csv(os.path.join(dir, "horizon_params.csv"))
    horizon_timepoints_df = pd.read_csv(os.path.join(dir, "horizon_timepoints.csv"))
    structure_df = pd.read_csv(os.path.join(dir, "structure.csv"))
    periods = period_params_df.period.unique().tolist()
    periods = [str(i) for i in periods]

    horizon_params_df['period'] = horizon_params_df['horizon'].astype(str).str[:4]
    horizon_timepoints_df['period'] = horizon_timepoints_df['horizon'].astype(str).str[:4]
    structure_df['period'] = structure_df['period'].astype(str)

    horizon_params_df_fixed = horizon_params_df[horizon_params_df.period.isin(periods)]
    horizon_timepoints_df_fixed = horizon_timepoints_df[horizon_timepoints_df.period.isin(periods)]
    structure_df_fixed = structure_df[structure_df.period.isin(periods)]

    horizon_params_df_fixed = horizon_params_df_fixed.drop(["period"], axis=1)
    horizon_timepoints_df_fixed = horizon_timepoints_df_fixed.drop(["period"], axis=1)

    horizon_params_df_fixed.to_csv(os.path.join(out_temporal_scens[i], "horizon_params.csv"), index=False)
    horizon_timepoints_df_fixed.to_csv(os.path.join(out_temporal_scens[i], "horizon_timepoints.csv"), index=False)
    structure_df_fixed.to_csv(os.path.join(out_temporal_scens[i], "structure.csv"), index=False)
