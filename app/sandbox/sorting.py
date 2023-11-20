def calcExp(exp_years):
    try:
        jExp = int(exp_years[:1])
    except:
        jExp = 0
    return jExp

def compareKeywords(candidateKeywords, jobKeywords):
    matches = 0
    candidateKeywordsArr = []
    jobKeywordsArr = []
    if jobKeywords != None and candidateKeywords != None:
        try:
            candidateKeywordsArr = candidateKeywords.split()
            jobKeywordsArr = jobKeywords.split()

            for keyword in jobKeywordsArr:
                if keyword in candidateKeywordsArr: matches += 1
        except:
            matches = 0

        return matches
    return matches

def calcScore(candidate, job):
    score = 0
    jExp = calcExp(job.exp_years)
    secondaryKeywords = compareKeywords(candidate.secondary_keyword, job.secondary_keyword)

    score += secondaryKeywords
    if candidate.experience_years >= jExp: score += 1
    if candidate.experience_years == jExp: score += 1
    if candidate.primary_keyword == job.primary_keyword: score += 2
    if candidate.salary_min <= job.salary_max: score += 1

    return score * 2