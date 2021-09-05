import sys
import yaml
import os

def get_dict():
    note = {1: ' ', \
            2: 'ˊ', \
            3: 'ˇ', \
            4: 'ˋ', \
            5: '˙'}
    dict = {}
    for fname in os.listdir('dict'):
        f = open('dict/' + fname)
        yml = yaml.safe_load(f)
        for chewing in yml:
            for keynote in yml[chewing]:
                words = yml[chewing][keynote]
                val = chewing + note[keynote]
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