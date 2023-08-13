import os

def generate_allprompts(indir, inprefix, outprefix):
    for f in os.listdir(indir):
        if f.startswith(inprefix) and f.endswith('.json'):
            suffix = f[len(inprefix):]
            fullf = os.path.join(indir, f)
            cmd = "python prompt_generate.py --input_dataset_path " + fullf
            cmd += " --output_dataset_path " + outprefix + suffix
            os.system(cmd)

if __name__=='__main__':
    generate_allprompts('scripts', 'testgen', 'testtemp')


