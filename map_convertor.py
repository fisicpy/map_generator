class MapConvertor:
    @staticmethod
    def mapping(input_data, old_min, old_max, new_min, new_max):
        return (((input_data - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

    @classmethod
    def noise_to_gray_map(cls, noise, width):
        picture = []
        for i in range(width):
            new_line = []
            for j in range(width):
                gray_gradation = int(
                    MapConvertor.mapping(
                        noise([i / width, j / width]),
                        -1,
                        1,
                        0,
                        255
                    )
                )
                new_line.append(gray_gradation)
            picture.append(new_line)
        return picture

    @classmethod
    def gray_map_to_txt(cls, gray_map, seed):
        with open(f"gray_map_{seed}.txt", "w") as file:
            file.write(f"{seed};{len(gray_map)}\n")
            for line in gray_map:
                new_line = ", ".join(str(x) for x in line)
                file.write(f"{new_line}\n")

    @classmethod
    def txt_to_gray_map(cls, file_name):
        with open(file_name, "r") as file:
            data = file.readline().replace("\n", "")
            seed, width = data.split(";")
            seed = int(seed)
            width = int(width)
            print(seed)
            print(width)
            gray_map = []
            for i in range(width):
                line = file.readline().replace("\n", "").split(", ")
                line = [int(x) for x in line]
                print(line)
                gray_map.append(line)
            return gray_map
