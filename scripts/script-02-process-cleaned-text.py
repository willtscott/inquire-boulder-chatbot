# Process cleaned data set into separate Q-n-A pairs, with each Q-n-A pair as one row in a CSV file 

import pandas as pd

def qna_pairs(row):
    '''
    For argument row of pandas dataframe, parse column 'FAQ' into heading and question-and-answer pairs, 
    storing in columns 'heading' and 'qna' respectively, and returning modified row. Concurrent questions
    are assumed to be in the same entry together.
    '''
    heading = True
    h = q = a = ''
    qna = []
    
    # Cycle through list of strings in FAQ column    
    for item in row.FAQ:
        # Check for heading and store separately, if exists. If not, store first question.
        if heading:
            if '?' not in item:
                h += ' ' + item
            else:
                heading = False
                q = item.strip()
                a = ''
        # Check for subsequent question and, if exists, append previous q-n-a pair before storing.
        elif '?' in item:
            qna.append([q.strip(), a.strip()])
            q = item
            a = ''
        # Accumulate answer strings
        else:
            a += ' ' + item

    # Treat heading as an answer to the question of 'Topic' column text
    if h:
        qna = [[row.Topic, h.strip()]] + qna  
    
    if q:
        qna.append([q.strip(), a.strip()])
        
    row['heading'] = h.strip()
    row['qna'] = qna
    
    return row




if __name__ == '__main__':
    # Load cleaned data, split FAQ column on double new lines, and apply Q-n-A separation function
    faq = pd.read_csv('../data/interim/faq-hand-cleaned.csv')

    faq.FAQ = faq.FAQ.apply(lambda x: x.split('\n\n'))

    faq = faq.apply(qna_pairs, axis=1)

    # Re-stack Q-n-A pairs into separate 'question' and 'answer' columns and drop unneeded columns
    stack = faq.apply(lambda x: pd.Series(x['qna']), axis=1).stack().reset_index(level=1, drop=True)
    stack.name = 'question'
    faq = faq.drop(['FAQ', 'qna', 'heading', 'Updated'], axis=1).join(stack).reset_index(drop=True)
    faq['answer'] = faq.question.apply(lambda x: x[1])
    faq['question'] = faq.question.apply(lambda x: x[0])
    
    # Write dataframe to file for notebook use
    faq.to_csv('../data/processed/faq-text-separated.csv', index=False)
    
    # Write dataframe to file for BotServer use
    faq.to_csv('../src/data/faq-text-separated.csv', index=False)
    
    # Write dataframe to file for Dialogflow Knowledgebase use, requiring only two columns, 'question' and 'answer'
    faq[['question', 'answer']].to_csv('../data/processed/faq-two-columns.csv', index=False)