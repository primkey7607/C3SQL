import pandas as pd
import json
import os
import random
import spacy

administrators = [
    "System Administrator",
    "Network Administrator",
    "Database Administrator",
    "Linux Administrator",
    "Windows Administrator",
    "Cloud Administrator",
    "Salesforce Administrator",
    "Exchange Administrator",
    "SharePoint Administrator",
    "Active Directory Administrator",
    "Security Administrator",
    "Database Security Administrator",
    "Application Administrator",
    "Web Administrator",
    "Storage Administrator",
    "Virtualization Administrator",
    "SAP Administrator",
    "HR Administrator",
    "Financial Administrator",
    "School Administrator",
    "Healthcare Administrator",
    "Hospital Administrator",
    "Office Administrator",
    "Project Administrator",
    "Salesforce Administrator",
    "CRM Administrator",
    "Database Developer/Administrator",
    "Education Administrator",
    "Event Administrator",
    "System Integration Administrator"
]

admin_lst = [st.replace(' ', '_') for st in administrators]

def get_tabcols(dirname, statement, outname):
    out_dct = {}
    out_dct['schema'] = {}
    out_dct['db_contents'] = {}
    out_dct['question'] = statement
    out_dct['fk'] = []
    for f in os.listdir(dirname):
        if f.endswith('.csv'):
            fullf = os.path.join(dirname, f)
            df = pd.read_csv(fullf)
            tname = f[:-4]
            cols = df.columns.tolist()
            out_dct['schema'][tname] = cols
            out_dct['db_contents'][tname] = {}
            for i,c in enumerate(cols):
                out_dct['db_contents'][tname][int(i)] = None
    
    out_obj = [out_dct]
    
    with open(outname + '.json', 'w+') as fh:
        json.dump(out_obj, fh, indent=2)

def gen_questions(dirname, outname, roles, tables, privileges):
    cnt = 1
    for r in roles:
        for t in tables:
            for p in privileges:
                question = 'The role ' + r + ' has ' + p + ' access to table ' + t + '.'
                get_tabcols(dirname, question, outname + str(cnt))
                cnt += 1

def gen_questions_from_docs(doc_dir, table_dir, outname):
    nlp = spacy.load("en_core_web_sm")
    doc_cnt = 0
    for f in os.listdir(doc_dir):
        if f.endswith('.txt'):
            with open(os.path.join(doc_dir, f)) as fh:
                doc_st = fh.read()
            doc = nlp(doc_st)
            for i,sent in enumerate(doc.sents):
                get_tabcols(table_dir, sent.text, outname + '_doc' + str(doc_cnt) + '_sent' + str(i))
            doc_cnt += 1

if __name__=='__main__':
    csv_dir = os.path.expanduser('~/tpch-kit/scale1data/tpchcsvs')
    # random.seed(3)
    # gen_questions(csv_dir, 'testgen', random.sample(admin_lst, k=25), ['customer', 'lineitem'], ['SELECT', 'INSERT'])
    gen_questions_from_docs('../../automatedgov/q1readonly/docs', csv_dir, '../q1exp/q1readonly')
    gen_questions_from_docs('../../automatedgov/q2readwrite/docs', csv_dir, '../q2exp/q2readwrite')
    gen_questions_from_docs('../../automatedgov/q3complex/docs', csv_dir, '../q3exp/q3complex')
    gen_questions_from_docs('../../automatedgov/q4dac/docs', csv_dir, '../q4exp/q4dac')
    gen_questions_from_docs('../../automatedgov/q5complexview/docs', csv_dir, '../q5exp/q5complexview')
    gen_questions_from_docs('../../automatedgov/q6dacview/docs', csv_dir, '../q6exp/q6dacview')
            
            
            
            
            

