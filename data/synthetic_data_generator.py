import numpy as np
import pandas as pd

start = "2022-01-01 00:00"
end = "2024-12-31 23:00"
date_range = pd.date_range(start=start, end=end, freq="h")

n = len(date_range)
np.random.seed(42)

day_of_year = date_range.dayofyear.values
yearly_season = 60 * np.sin(2 * np.pi * day_of_year / 365.25)

hour_of_day = date_range.hour.values
daily_pattern = 40 * np.sin(2 * np.pi * (hour_of_day - 7) / 24) + 25 * np.exp(-0.5 * ((hour_of_day - 19)/2.5)**2)

base_temp = 18
temp_season = 10 * np.sin(2 * np.pi * (day_of_year - 30) / 365.25)
temp_daily = 3 * np.sin(2 * np.pi * (hour_of_day - 15) / 24)
temperature = base_temp + temp_season + temp_daily + np.random.normal(0, 1.5, n)

humidity = 65 - 0.5 * (temperature - temperature.mean()) + np.random.normal(0, 5, n)
humidity = np.clip(humidity, 10, 100)

is_weekend = date_range.weekday >= 5
weekend_factor = np.where(is_weekend, -25, 0)

holidays = set([
    "2022-01-01","2022-01-26","2022-08-15","2022-10-02","2022-12-25",
    "2023-01-01","2023-01-26","2023-08-15","2023-10-02","2023-12-25",
    "2024-01-01","2024-01-26","2024-08-15","2024-10-02","2024-12-25"
])

rng = np.random.default_rng(12345)
for year in [2022, 2023, 2024]:
    extra = rng.choice(pd.date_range(f"{year}-01-01", f"{year}-12-31", freq="D").strftime("%Y-%m-%d"), size=3, replace=False)
    for d in extra:
        holidays.add(d)

holiday_flag = date_range.strftime("%Y-%m-%d").isin(holidays)
holiday_factor = np.where(holiday_flag, -40, 0)

base_load = 300
temp_effect = 1.8 * (temperature - temperature.mean())
noise = np.random.normal(0, 12, n)

energy = base_load + yearly_season + daily_pattern + temp_effect + weekend_factor + holiday_factor + noise

spike_indices = rng.choice(n, size=int(0.002 * n), replace=False)
energy[spike_indices] += rng.normal(80, 30, len(spike_indices))

missing_indices = rng.choice(n, size=int(0.01 * n), replace=False)
energy_with_nans = energy.copy()
energy_with_nans[missing_indices] = np.nan

df = pd.DataFrame({
    "timestamp": date_range,
    "energy_consumption": energy_with_nans,
    "temperature_C": np.round(temperature, 2),
    "humidity_pct": np.round(humidity, 2),
    "hour": hour_of_day,
    "dayofweek": date_range.weekday,
    "is_weekend": is_weekend.astype(int),
    "is_holiday": holiday_flag.astype(int)
})

df.set_index("timestamp", inplace=True)

path = "data/raw/energy_dataset.csv"
df.to_csv(path)