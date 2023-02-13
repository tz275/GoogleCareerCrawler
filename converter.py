import json


def allPunctuations(x):
    punctuations = [':', ',', '[', ']', '{', '}']
    if len(x) >= 3:
        return False
    for b in x:
        if b not in punctuations:
            return False
    return True


def onlyText(x):
    punctuations = [':', ',', '[', ']', '{', '}']
    if x[0] not in punctuations and x[-1] not in punctuations:
        return x
    front_index = 0
    back_index = len(x)
    for i in x:
        if i in punctuations:
            front_index += 1
        else:
            break
    for i in x[::-1]:
        if i in punctuations:
            back_index -= 1
        else:
            break
    return x[front_index:back_index]


def converter(index):
    # Read the file
    with open(f'./raw_data/google_careers_page{index}.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    text = None
    for i in json_object.values():
        text = i
    jobs_txt = []
    for i in text.split('"id"'):
        jobs_txt.append('"id"' + i)

    jobs_dic = {}

    for w in range(len(jobs_txt)):
        if w == 0:
            continue
        # split each job into jobs_lst
        job_dic = {}
        job = jobs_txt[w]
        job_lst = []
        split = job.split("\"")
        required_keys = ["id", "title", "categories", "apply_url", "responsibilities", "qualifications",
                         "company_id", "company_name", "language_code", "locations", "lat", "lon",
                         "address_lines", "city", "post_code", "country", "country_code", "is_remote",
                         "description", "education_levels", "created", "modified", "publish_date", "application_instruction"]

        temp = ""
        for i in range(len(split)):
            if not split[i] and i != 0:
                job_lst.append("None")
            if split[i] == "locations_count":
                break
            if not allPunctuations(split[i]) and split[i] != "display":
                if split[i] in required_keys:
                    if temp:
                        job_lst.append(["None" if not onlyText(temp) else onlyText(temp)][0])

                    job_lst.append(onlyText(split[i]))
                    temp = ""
                else:
                    temp += split[i]

        key_lst, value_lst = [], []
        for i in range(len(job_lst)):
            if i % 2 == 0:
                key_lst.append(job_lst[i])
            else:
                value_lst.append(job_lst[i])

        for i in range(min(len(key_lst), len(value_lst))):
            job_dic[key_lst[i]] = value_lst[i]

        jobs_dic[w] = job_dic

    with open(f"./raw_convert/converter_jobs_{index}.json", "w") as outfile:
        json.dump(jobs_dic, outfile)




