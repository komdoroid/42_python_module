#bin!/usr/bin/env python3

import importlib.util


def analyze_data() -> int:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 35.6895,
        "longitude": 139.6917,
        "hourly": "temperature_2m",
        "timezone": "Asia/Tokyo",
    }
    try:
        response = rq.get(url, params)
    except rq.exceptions.RequestException as e:
        print(f"Exception catched: {e}")
        return 0
    json_data = response.json()
    time = pd.to_datetime(json_data["hourly"]["time"])
    temperature = json_data["hourly"]["temperature_2m"]
    df = pd.DataFrame({"time": time, "temperature": temperature})
    arr = df["temperature"].to_numpy()
    window = 24
    kernel = np.ones(window) / window
    moving_avg = np.convolve(arr, kernel, mode='same')

    mpl.use('Agg')
    plt = importlib.import_module("matplotlib.pyplot")

    fig, ax = plt.subplots()
    ax.plot(time, arr, alpha=0.4, label="Raw temperature")
    ax.plot(time, moving_avg, linewidth=2, label="Moving average")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    fig.autofmt_xdate()

    output_path = "matrix_analysis.png"
    fig.savefig(output_path)
    return len(arr)


if __name__ == '__main__':
    MISSING_DEPENDENCIES = False

    print("LOADING STATUS: Loading programs...\n")
    if importlib.util.find_spec("pandas"):
        pd = importlib.import_module("pandas")
        print(
                f"[OK] pandas ({pd.__version__}) - "
                "Data manipulation ready"
              )
    else:
        print("[NG] pandas - Data manipulation not ready")
        MISSING_DEPENDENCIES = True
    if importlib.util.find_spec("numpy"):
        np = importlib.import_module("numpy")
        print(
                f"[OK] numpy ({np.__version__}) - "
                "Numerical computation ready"
              )
    else:
        print("[NG] numpy - Numerical computation not ready")
        MISSING_DEPENDENCIES = True
    if importlib.util.find_spec("requests"):
        rq = importlib.import_module("requests")
        print(
                f"[OK] requests ({rq.__version__}) - "
                "Network access ready"
              )
    else:
        print("[NG] requests - Network access not ready")
        MISSING_DEPENDENCIES = True
    if importlib.util.find_spec("matplotlib"):
        mpl = importlib.import_module("matplotlib")
        print(
                f"[OK] matplotlib ({mpl.__version__}) - "
                "Visualization ready"
              )
    else:
        print("[NG] matplotlib - Visualization not ready")
        MISSING_DEPENDENCIES = True

    if MISSING_DEPENDENCIES:
        print("\nMATRIX STATUS: Some programs are still missing."
              "The construct is incomplete. Load the missing programs with:\n")
        print("  pip: pip install -r requirements.txt\n"
              "  Poetry: poetry install\n")
        print("Then run this program again.")
    else:
        print("\nAnalyzing Matrix data...")
        data_num = analyze_data()
        print(f"Processing {data_num} data points...")
        print("Generating visualization...")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
