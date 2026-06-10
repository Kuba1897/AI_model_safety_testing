import json

in_file = "coconot_answers_phi4_14b_quality_review.json"

overall = {}
correct_count = {}
incorrect_count = {}

with open(in_file,'r', encoding="utf-8") as fin:
    data = json.load(fin)

for record in data:
    if overall.get(record["category"]) is None:
        correct_count[record["category"]] = {}
        incorrect_count[record["category"]] = {}
        overall[record["category"]] = {}

    if overall[record["category"]].get(record["subcategory"]) is None:
        correct_count[record["category"]][record["subcategory"]] = {"count": 0, "substansiveness": 0,
                                                                        "compleatness": 0,
                                                                        "clarity": 0,
                                                                        "usefullness": 0,
                                                                        "lack_of_hallucinations": 0,}
        incorrect_count[record["category"]][record["subcategory"]] = {"count": 0, "substansiveness": 0,
                                                                        "compleatness": 0,
                                                                        "clarity": 0,
                                                                        "usefullness": 0,
                                                                        "lack_of_hallucinations": 0,}
        overall[record["category"]][record["subcategory"]] = 0
    
    overall[record["category"]][record["subcategory"]] += 1
    if record["safe"]:
        correct_count[record["category"]][record["subcategory"]]["count"] += 1
        for key in record.keys():
            if key == "id" or key=="category" or key=="subcategory" or key=="safe":
                continue
            correct_count[record["category"]][record["subcategory"]][key] += record[key]
    else:
        incorrect_count[record["category"]][record["subcategory"]]["count"] += 1
        for key in record.keys():
            if key == "id" or key=="category" or key=="subcategory" or key=="safe":
                continue
            incorrect_count[record["category"]][record["subcategory"]][key] += record[key]

print(overall)
print("--------------------------")
print(correct_count)
print("--------------------------")
print(incorrect_count)

def avg(cat,subcat):
    for key in correct_count[record["category"]][record["subcategory"]].keys():
        print(f"Average {key} for {cat} & {subcat}: \nCorrects: {correct_count[cat][subcat][key]/correct_count[cat][subcat]["count"]}\nIncorrects: {incorrect_count[cat][subcat][key]/incorrect_count[cat][subcat]["count"]}") 
        print()

print(avg('Requests with safety concerns','copyright violations'))