class Solution:
    def simplifyPath(self, path: str) -> str:
        routes = path.split("/")
        dirs = []
        print(routes)
        i = 0
        while i < len(routes):
            if routes[i] == "..":
                if len(dirs) > 0:
                    dirs.pop()
                i += 1
                continue
            
            if routes[i] == "." or routes[i] == "":
                i += 1
                continue
            
            dirs.append(routes[i])
            i += 1
        print(dirs)

        return "/" + ("/".join(dirs))