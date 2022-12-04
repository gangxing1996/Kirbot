import csv 
def read_qa(file_name):
    with open(file_name,mode="r",encoding="utf8") as file:
        rows=rows=list(csv.reader(file))
        file.readline()
        qa_dict={row[0]:row[1:] for row in rows}
    return qa_dict
    


if __name__=="__main__":
    file_name="./qa.csv"
    file=open(file_name)
    # file.readline()
    rows=list(csv.reader(file))
    qa_dict={row[0]:row[1:] for row in rows}
    # for row in rows:
    #     print(row)
    # with open(file_name, newline='') as csvfile:
    #     rows = csv.reader(csvfile)
    #     for row in rows:
    #         print(row)
    import ipdb
    ipdb.set_trace()

