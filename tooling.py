import sys
import yaml
import os

DICT_DIR = "data/dict"
HETERO_DIR = "data"


def get_dict():
    tone = {1: " ", 2: "ˊ", 3: "ˇ", 4: "ˋ", 5: "˙"}
    dict = {}
    ymls = [fname for fname in os.listdir(DICT_DIR) if fname.endswith(".yml")]
    ymls.sort()
    for y in ymls:
        y_path = os.path.join(DICT_DIR, y)
        f = open(y_path)
        yml = yaml.safe_load(f)
        for chewing in yml:
            for keytone in yml[chewing]:
                words = yml[chewing][keytone]
                val = chewing + tone[keytone]
                for word in words:
                    if word in dict:
                        dict[word].append(val)
                    else:
                        dict[word] = [val]
        f.close()

    # Reorder by frequently-used pronounciations in HETERO_DIR
    h_path = os.path.join(HETERO_DIR, "heteronym.yml")
    f = open(h_path)
    yml = yaml.safe_load(f)
    for key in yml:
        dict[key] = yml[key]
    f.close()

    return dict


def main(argv):
    dict = get_dict()
    for word in argv[1]:
        if word not in dict:
            print(word)
        else:
            print(f"{word}: {dict[word]}")


if __name__ == "__main__":
    if len(sys.argv) > 0:
        main(sys.argv)
