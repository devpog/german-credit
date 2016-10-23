import os
import re
import string

columns = ['account_checking', 'duration', 'credit_history', 'purpose', 'credit_amount', 'account_saving',
           'employmet_status', 'installment_rate', 'personal_status_sex', 'other_debtors', 'residence_type',
           ]

work_dir = os.getcwd()
in_dir = work_dir + '/'

files = os.listdir(in_dir)
in_file = [in_dir + f for f in files if re.match(r'german\.data', f)].pop()

