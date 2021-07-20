from wikipedia import wikipedia # type: ignore
from typing import List, Union
import csv
from random import sample
def DrawAConcept():

    ListOFTopics = []
    with open('concept.csv', encoding='utf-8') as file:
        read = csv.reader(file)
        for row in read:
            ListOFTopics.append(row[0])
    checks = sample(ListOFTopics, 1)
    return checks[0]

def seach_in_wikipedia(query: Union[List[str], str]="") -> str:
    if query == [] or query == "":
        query = DrawAConcept()
    wikipedia.set_lang('pl')
    results = wikipedia.summary(query, auto_suggest=True)
    results = results.replace("=", "")
    print(results)
    return results

if __name__ == '__main__':
    # check = DrawAConcept()
    seach_in_wikipedia()

