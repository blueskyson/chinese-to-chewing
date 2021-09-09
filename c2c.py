import sys
import yaml
import os

DICT_DIR = "data"


def get_dict():
    tone = {1: " ", 2: "ˊ", 3: "ˇ", 4: "ˋ", 5: "˙"}
    dict = {}
    ymls = [fname for fname in os.listdir(DICT_DIR) if fname.endswith(".yml")]
    for y in ymls:
        y_path = os.path.join(DICT_DIR, y)
        f = open(y_path)
        yml = yaml.safe_load(f)
        for chewing in yml:
            for keytone in yml[chewing]:
                words = yml[chewing][keytone]
                val = chewing + tone[keytone]
                for word in words:
                    dict[word] = val
        f.close()
    return dict


def main(argv):
    dict = get_dict()
    result = ""
    for word in argv[1]:
        if word in dict:
            result += dict[word]
        else:
            result += word
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv)