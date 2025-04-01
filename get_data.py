import pyxdf

# 👉 Replace this with your actual file path
xdf_path = "D:/movement_data/your_file.xdf"

# Load the XDF file
streams, header = pyxdf.load_xdf(xdf_path)

# Print out stream metadata
print("\n📦 Found the following streams:\n")
for i, stream in enumerate(streams):
    name = stream['info']['name'][0]
    stype = stream['info']['type'][0]
    sfreq = float(stream['info']['nominal_srate'][0])
    n_samples = len(stream['time_series'])
    print(f"Stream {i}:")
    print(f"  ▶ Name: {name}")
    print(f"  ▶ Type: {stype}")
    print(f"  ▶ Sampling Rate: {sfreq} Hz")
    print(f"  ▶ # Samples: {n_samples}")
    print()
