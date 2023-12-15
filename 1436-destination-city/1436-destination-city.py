class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_dicts = dict(paths)

        for start, dest in path_dicts.items():
            while dest in path_dicts:
                start = dest
                dest = path_dicts[start]
            else:
                return dest