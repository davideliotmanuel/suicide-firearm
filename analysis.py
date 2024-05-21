import pandas as pd
from scipy.stats import ttest_ind

# Data from the file
data = {
    "State": ["Montana", "South Dakota", "Alaska", "Wyoming", "Idaho", "New Mexico", "Colorado", "Kansas", "Utah", "Oklahoma", "North Dakota", "Nevada", "Nebraska", "Arizona", "Oregon", "Washington", "Iowa", "Indiana", "South Carolina", "Kentucky", "Missouri", "Arkansas", "Georgia", "Virginia", "Texas", "Maine", "Tennessee", "Hawaii", "Louisiana", "North Carolina", "Minnesota", "Wisconsin", "West Virginia", "Ohio", "Michigan", "New Hampshire", "Mississippi", "Alabama", "Illinois", "Florida", "Pennsylvania", "Maryland", "California", "Connecticut", "Massachusetts", "New Jersey", "New York", "Delaware", "Rhode Island", "Vermont"],
    "Deaths": [86, 70, 51, 35, 103, 98, 246, 126, 167, 158, 28, 103, 67, 236, 118, 215, 100, 209, 149, 126, 172, 86, 317, 231, 888, 30, 170, 30, 116, 263, 141, 140, 39, 273, 229, 28, 69, 108, 264, 392, 250, 119, 594, 49, 87, 105, 208, 19, 10, 18],
    "Population": [284799, 257040, 195165, 163249, 577864, 597024, 1557357, 860014, 1140293, 1150996, 213958, 815476, 575597, 2039219, 1055282, 1946774, 915960, 1940743, 1406051, 1220600, 1675153, 851851, 3153865, 2315822, 8976839, 325354, 1844630, 327791, 1267702, 2920578, 1572167, 1603631, 448780, 3172820, 2677744, 342535, 864588, 1361584, 3463837, 5227354, 3384310, 1633162, 10748501, 990115, 1828818, 2408818, 4928007, 259553, 286928, 167287],
    "Crude Rate": [30.2, 27.2, 26.1, 21.4, 17.8, 16.4, 15.8, 14.7, 14.6, 13.7, 13.1, 12.6, 11.6, 11.6, 11.2, 11.0, 10.9, 10.8, 10.6, 10.3, 10.3, 10.1, 10.1, 10.0, 9.9, 9.2, 9.2, 9.2, 9.2, 9.0, 9.0, 8.7, 8.7, 8.6, 8.6, 8.2, 8.0, 7.9, 7.6, 7.5, 7.4, 7.3, 5.5, 4.9, 4.8, 4.4, 4.2, None, None, None]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add a column to categorize states by gun control laws
df['Gun Control Law'] = df['State'].apply(lambda x: 1 if x in ['California', 'Colorado', 'Connecticut', 'Delaware', 'Hawaii', 'Illinois', 'Massachusetts', 'Maryland', 'Maine', 'Minnesota', 'New Jersey', 'New York', 'North Carolina', 'Rhode Island', 'Texas', 'Virginia', 'Vermont', 'Washington', 'Wisconsin'] else 0)

# Separate the data into two groups based on gun control laws
with_gun_control = df[df['Gun Control Law'] == 1]['Crude Rate'].dropna()
without_gun_control = df[df['Gun Control Law'] == 0]['Crude Rate'].dropna()

# Calculate the means and perform a t-test
mean_with_gun_control = with_gun_control.mean()
mean_without_gun_control = without_gun_control.mean()
t_stat, p_value = ttest_ind(with_gun_control, without_gun_control)

# Calculate the effect size (Cohen's d)
mean_diff = mean_without_gun_control - mean_with_gun_control
pooled_sd = ((with_gun_control.std() ** 2 * (len(with_gun_control) - 1) + without_gun_control.std() ** 2 * (len(without_gun_control) - 1)) / (len(with_gun_control) + len(without_gun_control) - 2)) ** 0.5
cohen_d = mean_diff / pooled_sd

mean_with_gun_control, mean_without_gun_control, t_stat, p_value, cohen_d
