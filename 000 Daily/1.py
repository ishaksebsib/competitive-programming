# LINK: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

from typing import List


def removeSubfolders(folder: List[str]) -> List[str]:
    folder.sort()
    res = [folder[0]]
    
    for i in range(1, len(folder)):
        last_folder = res[-1] + '/'
        
        if not folder[i].startswith(last_folder):
            res.append(folder[i])
    
    return res
