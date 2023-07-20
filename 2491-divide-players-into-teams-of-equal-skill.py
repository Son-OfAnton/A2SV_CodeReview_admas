class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        summ = skill[0] + skill[-1]
        left = 0
        right = len(skill) - 1
        teams = []
        
        while left < right:
            if summ != skill[left] + skill[right]:
                return -1
                
            teams.append([skill[left], skill[right]])
            left += 1
            right -= 1
        
        chemistry = 0
        
        for skill_1, skill_2 in teams:
            chemistry += skill_1 * skill_2
        
        return chemistry
