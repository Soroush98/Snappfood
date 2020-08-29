import jsonlines
with jsonlines.open('result.jl') as reader:
    for obj in reader:
        print(obj)