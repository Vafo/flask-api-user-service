
from User import User
from UserController import UserController

class UserPrimitive(UserController):

    def __init__(self):
        self.local_storage = []
        self.unique_id = 0

    def _username_is_free(self, uname):
        free = True
        for entry in self.local_storage:
            if entry.name == uname:
                free = False
                break

        return free

    def save_user(self, user: User):
        exit_state = True
        if(self._username_is_free(user.name)):
            user.id = self.unique_id
            self.unique_id += 1
            self.local_storage.append(user)
        else:
            exit_state = False

        return exit_state

    def _find_idx_by(self, /, name=None, id=None):
        user_res = None
        find_val = None
        find_by = None
        idx = -1

        if id is not None:
            find_by = "id"
            find_val = id
        elif name is not None:
            find_by = "name"
            find_val = name
        else:
            return None
            
        for i, entry in enumerate(self.local_storage):
            if getattr(entry, find_by) == find_val:
                idx = i
                break

        return idx

    def load_user(self, /, name=None, id=None):
        idx = self._find_idx_by(name=name, id=id)
        if idx == -1:
            return None

        return self.local_storage[idx]

    def delete_user(self, /, name=None, id=None):
        
        idx = self._find_idx_by(name=name, id=id)
        
        if idx != -1:
            del self.local_storage[idx]
            return True
        else:
            return False

    def update_user(self, user, /, name=None, id=None):
        pass