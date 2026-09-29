import importlib.util
from importlib.metadata import version


def check_dependency() -> bool:
    print("Checking dependencies:")
    missing_package = []

    # Separate data from logic.
    dependencies = [
        ["pandas", "Data manipulation ready"],
        ["numpy", "Numerical computation ready"],
        ["matplotlib", "Visualization ready"]
    ]

    for dependency in dependencies:
        package = dependency[0]
        description = dependency[1]

        spec = importlib.util.find_spec(package)
        if spec is not None:
            ver = version(package)
            print(f"[OK] {package} ({ver}) - {description}")
        else:
            missing_package.append(package)

    if missing_package:
        print(
            f"Please install the packages: {missing_package}\n"
            "# with pip \n"
            "python3 -m venv .venv \n"
            "source .venv/bin/activate \n"
            "pip install -r requirements.txt \n"
            "python3 loading.py \n\n"
            "# with Poetry \n"
            "poetry install \n"
            "poetry run python3 loading.py"
        )
        return False
    else:
        return True


def data_analyzer() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # NumPy - generate simulated Matrix data
    matrix_data = np.random.rand(1000)

    # Pandas -  data manipulation
    data_frame = pd.DataFrame(matrix_data)
    statistics = data_frame.describe()
    print(
        "\nAnalysis:\n"
        f"Data points: {statistics.loc['count', 0]}\n"
        f"Mean: {statistics.loc['mean', 0]}\n"
        f"Minimum: {statistics.loc['min', 0]}\n"
        f"Maximum: {statistics.loc['max', 0]}"
    )

    # Matplotlib - visualization
    print("\nGenerating visualization...")
    plt.hist(data_frame[0], bins=10)
    plt.xlabel("Matrix Value")
    plt.ylabel("Frequency")
    plt.title("Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    if check_dependency():
        data_analyzer()


if __name__ == "__main__":
    main()
