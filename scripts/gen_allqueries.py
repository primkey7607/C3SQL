import os

def generate_allsql(indir, inprefix, outprefix):
    # sample command: 
    #python generate_sqls_by_gpt3.5.py --input_dataset_path ../testtemp1.json --output_dataset_path ../testsql1.json
    for f in os.listdir(indir):
        if f.startswith(inprefix) and f.endswith('.json'):
            suffix = f[len(inprefix):-5]
            fullf = os.path.join(indir, f)
            cmd = "python ../src/generate_sqls_by_gpt3.5.py --input_dataset_path " + fullf
            cmd += " --output_dataset_path " + outprefix + suffix + '.sql'
            os.system(cmd)

if __name__=='__main__':
    generate_allsql('../', 'testtemp', '../testsql')

