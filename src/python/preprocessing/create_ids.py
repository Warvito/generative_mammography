""" Script to create train, validation and test data lists with paths to images and radiological reports. """
import argparse
from pathlib import Path

import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--metadata_path", help="Path to CSAW-M_train.csv file.")
    parser.add_argument("--output_dir", help="Path to directory to save files with paths.")

    args = parser.parse_args()
    return args


def main(args):
    metadata_df = pd.read_csv(args.metadata_path, sep=";", na_values="-")

    data_list = []
    for index, row in metadata_df.iterrows():
        data_list.append(
            {
                "image": f"/sourcedata/images/{row['Filename']}",
            }
        )

    # transform data list to dataframe and shuffle it using a random seed
    data_df = pd.DataFrame(data_list)
    data_df = data_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # split in train, validation and test data lists. The total number of PA images in data_df is 96161.
    train_data_list = data_df[:9000]
    val_data_list = data_df[9000:]

    # save the data lists
    output_dir = Path(args.output_dir)
    train_data_list.to_csv(output_dir / "train.tsv", index=False, sep="\t")
    val_data_list.to_csv(output_dir / "validation.tsv", index=False, sep="\t")


if __name__ == "__main__":
    args = parse_args()
    main(args)
