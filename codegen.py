from os import path
import os

if __name__ == "__main__":
    code_directory = path.abspath(path.join(path.realpath(__file__), os.pardir))
    cet_directory = path.join(code_directory, "CETperceptual_csv_0_1")

    files = [file for file in os.listdir(cet_directory) if file.endswith(".csv")]
    files.sort()

    cet_datas: dict[str, list[tuple[int, int, int]]] = {}

    for filename in files:
        cet_id = filename[4:-4]  # CET-[cet_id].csv

        cet_data = []

        with open(path.join(cet_directory, filename)) as f:
            while line := f.readline():
                values = line.split(",")
                cet_data.append(
                    (int(values[0][2:]), int(values[1][2:]), int(values[2][2:]))
                )

        assert len(cet_data) == 256

        cet_datas[cet_id] = cet_data

    with open("datacet.ua", "w") as f:
        f.write("Ids ← {")

        for i, cet_id in enumerate(cet_datas.keys()):
            f.write(f'{" " if i else ""}"{cet_id}"')

        f.write("}\n\nFilenames ← {")

        for i, filename in enumerate(files):
            f.write(f'{" " if i else ""}"{filename}"')

        f.write("}\n")

        # f.write("Colors = [\n")

        # for cet_data in cet_datas.values():
        #     f.write("  [\n")

        #     for r, g, b in cet_data:
        #         f.write(f"    0.{r}_0.{g}_0.{b}\n")

        #     f.write("  ]\n")

        # f.write("]\n")
