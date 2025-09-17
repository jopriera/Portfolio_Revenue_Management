"""
data_generation.py
Create synthetic hotel booking data by sampling real records and adding slight random variations with Faker.
"""

import pandas as pd
from faker import Faker
import numpy as np
import os

fake = Faker()

def load_real_data(path):
    """Load the original bookings CSV into a DataFrame."""
    return pd.read_csv(path)

def perturb_row(row):
    """Apply small random changes to numeric fields and randomize reservation dates."""
    new = row.copy()
    if 'adr' in row:
        # Adjust ADR by up to ±10%
        new['adr'] = max(0, row['adr'] * (1 + np.random.normal(0, 0.1)))
    if 'lead_time' in row:
        # Adjust lead time by up to ±10%
        new['lead_time'] = max(0, int(row['lead_time'] * (1 + np.random.normal(0, 0.1))))
    if 'reservation_status_date' in row:
        # Assign a random reservation status date within the past year
        new['reservation_status_date'] = fake.date_between(start_date='-1y', end_date='today')
    return new

def generate_synthetic_data(df, num_rows):
    """Randomly sample rows with replacement and perturb each one."""
    sampled = df.sample(n=num_rows, replace=True).reset_index(drop=True)
    return sampled.apply(perturb_row, axis=1)

def save_synthetic_data(df, path):
    """Write the synthetic DataFrame to CSV."""
    df.to_csv(path, index=False)
    print(f'Synthetic data saved to: {path}')

def main():
    base_dir = os.path.dirname(__file__)
    real_path = os.path.join(base_dir, '..', '01_Raw_Data', 'kaggle_hotel_booking.csv')
    synth_dir = os.path.join(base_dir, '..', '01_Raw_Data', 'synthetic_data')
    synth_path = os.path.join(synth_dir, 'synthetic_hotel_bookings.csv')
    os.makedirs(synth_dir, exist_ok=True)

    print(f'Loading real data from: {real_path}')
    real_df = load_real_data(real_path)

    num_rows = len(real_df)
    print(f'Generating {num_rows} synthetic rows with random perturbations...')
    synth_df = generate_synthetic_data(real_df, num_rows)

    save_synthetic_data(synth_df, synth_path)

if __name__ == '__main__':
    main()
