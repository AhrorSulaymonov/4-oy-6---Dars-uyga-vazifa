import json, os
os.system("cls")
from errors import UsernameAlreadyExistsError

class Database:
    def selectAllUsers(self) -> list:
        with open("./database/users.json", "r", encoding="utf-8") as file:
            data = file.read()
            users = json.loads(data) or []
            return users
        
    def selectUser(self, username : str) -> dict | None:
        users = self.selectAllUsers()
        [user] = list(filter(lambda user : user["username"] == username, users)) or [None]
        return user
    def login(self, username : str, password : str) -> dict | None:
        users = self.selectAllUsers()
        [user] = list(filter(lambda user : user["username"] == username and user["password"] == password, users)) or [None]
        return user

    def register(self, name : str, surname : str, username : str, password : str):
        foundUser = self.selectUser(username)
        if foundUser:
            UsernameAlreadyExistsError("Username band!")
        USERS = self.selectAllUsers()
        new_user = {
        "id" : USERS[-1]["id"] + 1,
        "name" : name,
        "surname" : surname,
        "username" : username,
        "password" : password
        }
        USERS.append(new_user)
        with open("./database/users.json", "w") as file:
            data = json.dumps(USERS, indent=4)
            file.write(data)
        return new_user

    def selectAllPosts(self) -> list:
        with open("./database/posts.json", "r", encoding="utf-8") as file:
            data = file.read()
            posts = json.loads(data) or []
            return posts
    def getUserName(self, user_id : int) -> str:
         with open("./database/users.json", "r", encoding="utf-8") as file:
            data = file.read()
            users = json.loads(data) or []
            if len(users) > 0:
                for i in range(len(users)):
                    if users[i]["id"] == user_id:
                        return users[i]["name"]
        
        
    def selectuserPosts(self,user_id : int) -> list:
        with open("./database/posts.json", "r", encoding="utf-8") as file:
            data = file.read()
            posts = json.loads(data) or []
            filtredPosts = list(filter(lambda p: p["user_id"] == user_id, posts))
            return filtredPosts

    def addpost(self,user_id : int, post_text : str) -> None:
        allposts = self.selectAllPosts()
        ID = allposts[-1]["id"] + 1
        allposts.append({
            "id" : ID,
            "user_id" : user_id,
            "text" : post_text
        })

        with open("./database/posts.json","w") as file:
            data = json.dumps(allposts,indent=4)
            file.write(data)

