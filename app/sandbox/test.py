def testF(candidate, job):
    data = [
        [f'Candidate exp: {candidate.experience_years}, Job exp: {job.exp_years}'],
        [f'Candidate primary: {candidate.primary_keyword}, Job primary: {job.primary_keyword}'],
        [f'Candidate secondary: {candidate.secondary_keyword}, Job secondary: {job.secondary_keyword}'],
        [f'Candidate compensation min: {candidate.salary_min}, Job compensation max: {job.salary_max}'],
    ]
    
    return data