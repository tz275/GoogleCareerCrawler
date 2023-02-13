import json


def standardFormatConverter(index):
    # Read the file
    with open(f'./raw_convert/converter_jobs_{index}.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    jobs_dic = dict(json_object)

    for i in range(1, len(jobs_dic)):
        sdf_job = {}
        location = {}
        job = jobs_dic[str(i)]
        sdf_job["jobID"] = job["id"]
        sdf_job["origin_search"] = "Google Careers"
        sdf_job["posted"] = job["publish_date"]
        sdf_job["jobTitle"] = job["title"]
        sdf_job["companyName"] = job["company_name"]
        sdf_job["link"] = job["apply_url"]
        # jobLocation
        location["remote"] = job["is_remote"]
        location["city"] = job["city"]
        location["state"] = job["country"]
        location["country"] = job["country_code"]
        sdf_job["jobLocation"] = location
        sdf_job["educationRequirement"] = {"education": job["education_levels"], "major": None}
        # jobType
        title_lst = job["title"].split(' ')
        title_lst += job["description"].split(' ')
        internship = False
        partTime = False
        fullTime = False
        coop = False
        contract = False
        independent_contractor = False
        temporary = False
        oncall = False
        volunteer = False
        for t in title_lst:
            if t in ["intern", "internship", "Intern", "Internship"]:
                internship = True
            if t in ["part time", "part-time", "Part Time", "Part-time", "Part time"]:
                partTime = True
            if t in ["full time", "full-time", "Full Time", "Full-time", "Full time"]:
                fullTime = True
            if t in ["coop", "Coop", "COOP"]:
                coop = True
            if t in ["contract", "Contract"]:
                contract = True
            if t in ["independent contractor", "Independent contractor"]:
                independent_contractor = True
            if t in ["temporary", "Temporary"]:
                temporary = True
            if t in ["oncall", "Oncall"]:
                oncall = True
            if t in ["volunteer", "Volunteer"]:
                volunteer = True
        type_ = {"internship": internship,
                "partTime": partTime,
                "fullTime": fullTime,
                "coop": coop,
                "contract": contract,
                "independent_contractor": independent_contractor,
                "temporary": temporary,
                "oncall": oncall,
                "volunteer": volunteer}
        sdf_job["jobType"] = type_
        sdf_job["visaSponsorship"] = None
        sdf_job["salary"] = None
        sdf_job["benefits"] = None
        sdf_job["requirement"] = job["qualifications"]
        sdf_job["jobDescription"] = job["description"]

        with open(f"./standard_data/google_career_{index}.json", "w") as outfile:
            json.dump(jobs_dic, outfile)

