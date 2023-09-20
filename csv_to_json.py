import os
import pandas as pd 
import json 
def main():

    database_dir = "data_csv"
    output_dir = "data_json"
    for file_ in os.scandir(database_dir):

        df = pd.read_csv(file_.path)
        json_data = [{"phi": phi, "psi": psi} for phi, psi in zip(df.Phi, df.Psi)]

        with open(os.path.join(output_dir, file_.name.replace("csv", "json")), "w") as out_file:
            json.dump(json_data, out_file)


if __name__ == "__main__":
    main()