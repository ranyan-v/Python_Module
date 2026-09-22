import sys
import importlib
# import importlib.metadata
# import os

# def package_version(package_name: str) -> str:
#     try:
#         current_v = importlib.metadata.version(package_name)
#     except importlib.metadata.PackageNotFoundError:
#         return f"Can't find the module: {package_name}"
#     expected = "n/a"
#     filename = "requirements.txt"
#     if os.path.exists(filename):
#         with open(filename, 'r') as r:
#             for line in r:
#                 if not line or line.startswith("#"):
#                     continue
#                 for equ in ["==", ">=", "~="]:
#                     if equ in line:
#                         name, ver = line.split(equ, 1)
#                         if name.strip().lower() == package_name.lower():
#                             expected = f"{equ}{ver.strip()}"
#                             break
#                 if expected != "n/a":
#                     break
#     return f"package {package_name} -> Current: {current_v}"\
#             f"| Expected: {expected}"


def package_check() -> None:
    print("Checking dependencies:")
    missing_package = []
    try:
        pd = importlib.import_module("pandas")
        name = getattr(pd, '__name__', 'n/a')
        version = getattr(pd, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Data manipulation ready")
    except Exception:
        missing_package.append("pandas")

    try:
        np = importlib.import_module("numpy")
        name = getattr(np, '__name__', 'n/a')
        version = getattr(np, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Numerical computation ready")
    except Exception:
        missing_package.append("numpy")

    try:
        plt = importlib.import_module("matplotlib")
        name = getattr(plt, '__name__', 'n/a')
        version = getattr(plt, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Visualization ready")
    except Exception:
        missing_package.append("matplotlib")
    if missing_package:
        print(
            f"Please install the packages: {missing_package}\n"
            "Use 'pip install -r requirements.txt' or \n"
            "'poetry install' to install missing packages"
        )
        sys.exit(1)


def generate_graph() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    rolls = np.random.randint(1, 7, 100)
    index = np.arange(1, 101)
    print(
        "\nAnalyzing Matrix data...\n"
        "Processing 1000 data points..."
    )
    data_frame = pd.DataFrame({"index": index, "roll": rolls})
    plt.figure()
    plt.plot(data_frame["index"], data_frame["roll"], marker="o")
    plt.title("Dice Rolls")
    print(
        "Generating visualization...\n\n"
        "Analysis complete!\n"
        "Results saved to : dice.png"
        )
    plt.savefig("dice.png")
    # plt.show()
    plt.close()


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    package_check()
    print()
    # for pkg in ["pandas", "numpy", "matplotlib"]:
    #     print(package_version(pkg))
    generate_graph()
