import os

def generate_allsql(indir, inprefix, outprefix):
    # sample command: 
    #python generate_sqls_by_gpt3.5.py --input_dataset_path ../testtemp1.json --output_dataset_path ../testsql1.json
    for f in os.listdir(indir):
        if f.startswith(inprefix) and f.endswith('.json'):
            suffix = f[len(inprefix):-5]
            outfile = outprefix + suffix + '.sql'
            if os.path.exists(outfile):
                continue
            
            fullf = os.path.join(indir, f)
            cmd = "python ../src/generate_sqls_by_gpt3.5.py --input_dataset_path " + fullf
            cmd += " --output_dataset_path " + outprefix + suffix + '.sql'
            os.system(cmd)

if __name__=='__main__':
    # generate_allsql('../', 'testtemp', '../testsql')
    generate_allsql('../q1exp', 'q1exp', '../q1sql')
    # generate_allsql('../q2exp', 'q2exp', '../q2sql')
    # generate_allsql('../q3exp', 'q3exp', '../q3sql')
    # generate_allsql('../q4exp', 'q4exp', '../q4sql')
    # generate_allsql('../q5exp', 'q5exp', '../q5sql')
    # generate_allsql('../q6exp', 'q6exp', '../q6sql')

