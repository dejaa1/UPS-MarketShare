from edgar import Company, TXTML
import re
import pandas as pd

df = pd.read_excel(r'companylist.xls')

expense_estimates = []
for i in df.index:
    print(expense_estimates)
    CIK_string = df['CIK'][i].split("; ")
    print(df['Company Name'][i])
    company = Company("df['Company Name'][i]", CIK_string[0])
    try:
        doc = company.get_10K()
        text = TXTML.parse_full_10K(doc)
    except IndexError:
        expense_estimates.append(float("NaN"))
        continue
    if not ('hipping' in text):
        expense_estimates.append(float("NaN"))
        continue
    matches = [m.start() for m in re.finditer('hipping', text)]
    #print(matches)
    string = ""
    est_available = False
    for i in matches:
        if '$' in text[i:i+50]:
            string = text[i:i+200]
            est_available = True
            break
    if not est_available:
        expense_estimates.append(float("NaN"))
        continue

    print(string)
    estimate_text = [m.start() for m in re.finditer("\$", string)][0]
    value_string = string[estimate_text:estimate_text+20]
    print(value_string)

    cost_list = re.split("\s(?!\d)", value_string)
    print(cost_list)
    cost_string = cost_list[0]
    million = cost_list[1]
    number = cost_string.replace('$', '')
    million = million.replace(',', '')
    cost = number.replace(',', '')
    cost = float(cost)
    if million != 'million':
        cost = cost / 1000
    expense_estimates.append(cost)

expense_estimates