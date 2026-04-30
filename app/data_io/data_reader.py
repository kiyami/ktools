import numpy as np


def read_data_txt(filename, info=None):
    """
    Auto-detect column TXT reader (NumPy based)
    Returns: data_columns(list of arrays), colnames
    """

    config = {
        "delimiter": None,
        "dtype": float,
        "skip_header": True,
        "colnames": None
    }

    if info:
        config.update(info)

    delimiter = config["delimiter"]
    dtype = config["dtype"]

    # ---------------- HEADER ----------------
    with open(filename, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()

    if delimiter:
        header = first_line.split(delimiter)
    else:
        header = first_line.split()

    # ---------------- DATA LOAD ----------------
    data = np.loadtxt(
        filename,
        delimiter=delimiter,
        dtype=dtype,
        skiprows=1
    )

    data = np.atleast_2d(data)

    # ---------------- AUTO COLUMN DETECT ----------------
    n_cols = data.shape[1]

    if config["colnames"] is None:
        if len(header) == n_cols:
            colnames = header
        else:
            colnames = [f"col_{i}" for i in range(n_cols)]
    else:
        colnames = config["colnames"]

    # ---------------- SPLIT COLUMNS ----------------
    columns = [data[:, i].tolist() for i in range(n_cols)]

    return colnames, columns

"""
cols[0] → x
cols[1] → y
cols[2] → z
names → ["x", "y", "z"]

cols, names = read_data_txt(
    "data.txt",
    {"colnames": ["time", "temp", "pressure"]}
)

names = ["col_0", "col_1", "col_2"]
"""