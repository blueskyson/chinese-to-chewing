import sys
import yaml
import os
import trie

DICT_DIR = "data/dict"
HETERO_DIR = "data"
TRIE_DIR = "data"


def get_dict():
    # Load dict from DICT_DIR
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


def get_trie(dict):
    s_path = os.path.join(HETERO_DIR, "special_case.yml")
    f = open(s_path)
    yml = yaml.safe_load(f)

    t = trie.Trie()
    for key in yml:
        chewing = ""
        for i, c in enumerate(key, start=0):
            idx = int(yml[key][i])
            chewing += dict[c][idx]
        t.insert(key, chewing)
    f.close()

    return t


def main(argv):
    dict = get_dict()  # chinese-chewing dictionary
    t = get_trie(dict)  # trie
    s = argv[1]  # original string
    slen = len(argv[1])  # original string's length
    result = ""  # result chewing string
    index = 0  # current index in while loop

    while index < slen:
        tup = t.match(argv[1], index)

        # Doesn't match any special case
        if tup[0] is None:
            result += dict[s[index]][0]
            index = index + 1
        # Match
        else:
            result += tup[0]
            index = tup[1]
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv)
