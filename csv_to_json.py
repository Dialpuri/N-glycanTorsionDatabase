import os
import pandas as pd 
import json 
def main():

    database_dir = "data_csv"
    output_dir = "data_json"
    for file_ in os.scandir(database_dir):

        df = pd.read_csv(file_.path)
        json_data = [{"phi": phi, "psi": psi} for phi, psi in zip(df.Phi, df.Psi)]

        name = file_.name.rstrip('.csv')
        x = name.split("-")
        swapped_name = f"{x[2]}-{x[1]}-{x[0]}.json"
        out_file_name = os.path.join(output_dir, swapped_name)

        with open(out_file_name, "w") as out_file:
            json.dump(json_data, out_file)


if __name__ == "__main__":
    main()