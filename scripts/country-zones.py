"""
script to create subscenarios for running individual countries in SAPP
"""

import os
import pandas as pd

# input csvs path
input_path = "/Users/meas/Documents/gridpath-0.14.1/db/csvs_sapp_GPv0.14.1_workshop_072022"

# output csvs path
output_path = "/Users/meas/Documents/gridpath-0.14.1/db/csvs_reds_102022"

# get project to load zone mapping
project_lz_file = os.path.join(input_path, "project/project_load_zones/2_2.csv") # subscenario 2 is used in base
project_lz_df = pd.read_csv(project_lz_file)
un_lz = project_lz_df.load_zone.unique().tolist()
un_lz = sorted(un_lz)

# read in base portfolio file
project_portfolio_file = os.path.join(input_path, "project/project_portfolios/100_project_portfolios_simple_re.csv")
project_portfolio_df = pd.read_csv(project_portfolio_file)

# loop through and create country-specific portfolios
for i in range(len(un_lz)):
    lz = un_lz[i]
    proj = project_lz_df[project_lz_df.load_zone == lz]
    un_proj = proj.project.unique().tolist()
    lz_portfolio = project_portfolio_df[project_portfolio_df.project.isin(un_proj)]

    subs_id = 101+i
    lz_portfolio.to_csv(os.path.join(output_path,
                                     "project/project_portfolios",
                                     str(subs_id) + "_project_portfolios_simple_re_" + lz + ".csv"), index=False)

# read in load zones file
load_zones_file = os.path.join(input_path, "system_load/load_zones/1_15zones.csv")
load_zones_df = pd.read_csv(load_zones_file)

# loop through regions and create load zones files
for i in range(len(un_lz)):
    lz = un_lz[i]
    sub_lz = load_zones_df[load_zones_df.load_zone == lz]

    subs_id = 101 + i
    sub_lz.to_csv(os.path.join(output_path,
                               "system_load/load_zones",
                               str(subs_id) + "_1zone_" + lz + ".csv"), index=False)
