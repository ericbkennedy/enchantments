"""
Calculate the odds of getting a hiking permit in the Enchantments Lottery 
for different permit start dates. By Eric Kennedy February 2023

Data from https://www.fs.usda.gov/detail/okawen/passes-permits/recreation/?cid=fsbdev3_053607
"""
import pandas as pd
pd.options.display.float_format = '{:.1%}'.format

def calculate_odds(csv_file, date_start, date_end):
    with open(csv_file) as f:
        df = pd.read_csv(f)
    desired_zone = "Core Enchantment Zone"
    all_entries = pd.DataFrame(index=pd.Index([], name="entry_date")) # empty DF with index to concat winners and entries

    for i in range(1, 4):
        winners = df[(df[f"Preferred Division {i}"] == desired_zone) & (df["Awarded Preference"] == i)]
        # Group by "Preferred Entry Date {i}" and then sum on "Minimum Acceptable Group Size {i}" column
        winners_by_date = winners.groupby(f"Preferred Entry Date {i}")[f"Minimum Acceptable Group Size {i}"].sum()
        # winners_by_date is now a Series. Rename axis "Preferred Entry Date {i}" to "entry_date" and sum col to "r{i}_winners" 
        winners_by_date = winners_by_date.rename_axis("entry_date").rename(f"r{i}_winners")

        entries = df[(df[f"Preferred Division {i}"] == desired_zone) & (pd.isnull(df["Awarded Preference"]) | (df["Awarded Preference"] >= i))]
        entries_by_date = entries.groupby(f"Preferred Entry Date {i}")[f"Minimum Acceptable Group Size {i}"].sum()
        entries_by_date = entries_by_date.rename_axis("entry_date").rename(f"r{i}_entries")

        all_entries = pd.concat([all_entries, winners_by_date, entries_by_date], axis=1)
        all_entries = all_entries.fillna(0)
        all_entries[f"r{i}_odds"] = all_entries[f"r{i}_winners"] / (all_entries[f"r{i}_entries"])
        all_entries = all_entries.fillna("") # skip % calculation if no one entered for a date

    all_entries.index = pd.to_datetime(all_entries.index)

    all_entries = all_entries.loc[date_start: date_end] # filter out dates too early or too late in the season

    all_entries["weekday"] = pd.to_datetime(all_entries.index).day_name()
    # pop and insert weekday call as first column after date index
    weekday_col = all_entries.pop("weekday")
    all_entries.insert(0, weekday_col.name, weekday_col)

    all_entries = all_entries.sort_values(by=["r1_odds"], ascending=False)

    # format count of winners and entries using general number format
    count_format = {col: '{0:g}'.format for col in all_entries.columns if "i" in col} # w*i*nners or entr*i*es

    print(all_entries.head(25).to_string(formatters=count_format))

calculate_odds(csv_file="data/2022_data_fseprd1076588.csv", date_start="2022-06-15", date_end="2022-10-23")

calculate_odds(csv_file="data/2021_data_fseprd997472.csv", date_start="2021-06-15", date_end="2021-10-24")

calculate_odds(csv_file="data/2020_data_fseprd997471ek.csv", date_start="2020-06-15", date_end="2020-10-25")