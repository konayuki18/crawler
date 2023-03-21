import re
import os
import pickle as pk

hant_pattern = re.compile(r'public static \$zh2Hant = \[([^]]*)]', re.M)
pair_pattern = re.compile(r'\'([^\']+)\' => \'([^\']+)\'')
hans_pattern = re.compile(r'public static \$zh2Hans = \[([^]]*)]', re.M)
pardir = os.path.abspath(__file__)
pardir = os.path.dirname(pardir)

def make_dict(data, pattern, file_path):
    with open(file_path, 'w', encoding='UTF-8') as fout:
        for p in pattern.findall(data):
            for pp in pair_pattern.findall(p):
                fout.write('%s\t%s\n' % pp)

def load_dict(file_path):
    conv = dict()
    conv['dict'] = dict()
    with open(file_path, 'r', encoding='UTF-8') as fin:
        for line in fin:
            line = line.strip().split('\t')
            n = len(line[0])
            dd = conv['dict'].get(n, dict())
            dd[line[0]] = line[1]
            conv['dict'][n] = dd
    conv['length'] = sorted(list(conv['dict'].keys()), reverse=True)
    return conv

def abspath(path):
    global pardir
    return os.path.join(pardir, path)

def conv():
    with open(abspath('ZhConversion.php'), 'r', encoding='UTF-8') as fin:
        data = fin.read()
        make_dict(data, hant_pattern, abspath('zhhans2t.txt'))
        make_dict(data, hans_pattern, abspath('zhhant2s.txt'))

    zhhanz = dict()
    zhhanz['s2t'] = load_dict(abspath('zhhans2t.txt'))
    zhhanz['t2s'] = load_dict(abspath('zhhant2s.txt'))
    with open(abspath('zhhanz.pkl'), 'wb') as pkl:
        pk.dump(zhhanz, pkl)

    os.remove(abspath('zhhans2t.txt'))
    os.remove(abspath('zhhant2s.txt'))

if __name__ == '__main__':
    conv()
