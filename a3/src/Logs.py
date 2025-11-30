import os
import csv

DEFAULT_DIR: str = "a3/output"

CSV_HEADER: list = [
    "generation", "min_string", "min_fitness", "max_string", "max_fitness", "avg_fitness", "sum_fitness"
]

def loadExistingCSV(filePath: str, csvHeader: list[str]) -> list[dict]:
    """Loads a pre-existing CSV file,
    create nefw CSV file using path filename if it did not exist.

    Args:
        filePath (str): Path to read CSV from.
        csvHeader (list[str]): Default header data.

    Returns:
        list[dict]: Contents of the CSV file. (cpy)
    """
    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csvHeader)
            writer.writeheader()
        return []
    
    with open(filePath, 'r', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def newRecord(csvHeader: list[str], data: list[str]) -> dict:
    """Load a list of record keys to a respective list of values,
    return the output record as a dictionary. 

    Args:
        csvHeader (list[str]): Header names.
        data (list): Data for each header.

    Returns:
        dict: Record.
    """
    return dict(zip(csvHeader, data))

def overwrite(filePath: str, csvHeader: list[str], records: list[dict]) -> None:
    """Overwrites the contents of the CSV file.

    Args:
        filePath (str): Path to read CSV from.
        csvHeader (list[str]): Header names. 
        records (list[dict]): Collection of data records.
    """
    with open(filePath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csvHeader)
        writer.writeheader()
        writer.writerows(records)