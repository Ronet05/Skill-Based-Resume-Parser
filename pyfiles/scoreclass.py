from zipfile import ZipFile
import PyPDF2
import re
import os
import csv
import json

class Calc_Score:
    def level2_skills(self, skill, dataset, level1_skl):
        skills = []
        related = ['related_1','related_2','related_3','related_4','related_5','related_6','related_7','related_8','related_9','related_10']
        for i in dataset:
            for skl in related:
                if i[skl] == skill:
                    if i['name'] in level1_skl:
                        continue
                    else:
                        skills.append(i['name'])
        for i in level1_skl:
            for j in dataset:
                if j['name'] == i:
                    for r in related:
                        if j[r] in level1_skl:
                            continue
                        elif j[r] in skills:
                            continue
                        elif j[r] == skill:
                            continue
                        else:
                            skills.append(j[r])   
        return skills
    
    def level1_skills(self, jd_skill, dataset):
        skills = []
        related = ['related_1','related_2','related_3','related_4','related_5','related_6','related_7','related_8','related_9','related_10']
        for i in dataset:
            if i['name'] == jd_skill:
                for j in related:
                    skills.append(i[j])
        return skills

    def similarity_score_levels(self, r_skill, jd_skill, dataset):
        s_score = 0
        if r_skill == jd_skill:
            s_score = 1
        else:
            l1_skills = self.level1_skills(jd_skill, dataset)
            l2_skills = self.level2_skills(jd_skill, dataset, l1_skills)
            if r_skill in l1_skills:
                s_score = 0.7
            elif r_skill in l2_skills:
                s_score = 0.5
            else:
                s_score = 0
        return s_score
        

    def skillscore_update(self, r_skills, jd_skills, dataset):
        skill_score = 0
        for i in r_skills:
            score = 0
            for j in range(len(jd_skills)):
                sc = self.similarity_score_levels(i, jd_skills[j], dataset)
                score += (sc)
            skill_score += score
        return skill_score
