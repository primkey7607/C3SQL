import os

def generate_allprompts(indir, inprefix, outprefix):
    for f in os.listdir(indir):
        if f.startswith(inprefix) and f.endswith('.json'):
            suffix = f[len(inprefix):]
            fullf = os.path.join(indir, f)
            cmd = "python ../src/prompt_generate.py --input_dataset_path " + fullf
            cmd += " --output_dataset_path " + outprefix + suffix
            os.system(cmd)

if __name__=='__main__':
    # generate_allprompts('.', 'testgen', 'testtemp')
    generate_allprompts('../q1raw', 'q1readonly', '../q1exp')
    generate_allprompts('../q2raw', 'q2readwrite', '../q2exp')
    generate_allprompts('../q3raw', 'q3complex', '../q3exp')
    generate_allprompts('../q4raw', 'q4dac', '../q4exp')
    generate_allprompts('../q5raw', 'q5complexview', '../q5exp')
    generate_allprompts('../q6raw', 'q6dacview', '../q6exp')


