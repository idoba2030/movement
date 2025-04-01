import pyxdf
import numpy as np
import mne

# Path to your XDF file
xdf_file_path = "D:/movement_data/sub-P001_ses-S001_task-Default_run-001_eeg.xdf"

# Load XDF file
streams, _ = pyxdf.load_xdf(xdf_file_path)

# Find EEG and Marker (trigger) streams
eeg_stream = next(s for s in streams if s['info']['type'][0] == 'EEG')
marker_stream = next(s for s in streams if s['info']['type'][0] in ['Markers', 'Trigger'])

# Extract EEG data and timestamps
eeg_data = np.array(eeg_stream['time_series']).T  # shape: (n_channels, n_times)
sfreq = float(eeg_stream['info']['nominal_srate'][0])  # Sampling rate
eeg_times = np.array(eeg_stream['time_stamps'])  # Timestamps

# Extract marker (trigger) data
trigger_times = np.array(marker_stream['time_stamps'])
trigger_labels = [x[0] for x in marker_stream['time_series']]

# Channel names for EEG
ch_names = [ch['label'][0] for ch in eeg_stream['info']['desc'][0]['channels'][0]['channel']]
ch_types = ['eeg'] * len(ch_names)

# Create MNE Raw object from EEG data
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
raw = mne.io.RawArray(eeg_data, info)

# Print basic info
print(raw.info)
