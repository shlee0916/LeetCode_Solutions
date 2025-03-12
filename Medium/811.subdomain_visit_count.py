'''
https://leetcode.com/problems/subdomain-visit-count/description/
'''

from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit = {}

        for num_domain in cpdomains:
            num, domains = num_domain.split()
            num, domains = int(num), domains.split(".")

            for idx in range(len(domains)):
                domain = ".".join(domains[idx:])
                visit[domain] = visit[domain] + num if domain in visit else num

        return [f"{num} {domain}" for domain, num in visit.items()]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.subdomainVisits(cpdomains = ["9001 discuss.leetcode.com"])
    assert set(test1) == set(["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"])
    
    test2 = sol.subdomainVisits(cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    assert set(test2) == set(["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"])
