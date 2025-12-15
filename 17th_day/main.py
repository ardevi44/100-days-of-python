# This code is just an example nothing related to the project of this day

# Name classes in Pascal case
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.followings = 0
        print("New user has been created")
        print(f"Welcome {self.name}")

    def show_followers_number(self):
        print(f"{self.name} has {self.followers} followers.")

    def show_followers_and_followings(self):
        print(
            f"{self.name} has {self.followers} followers and {self.followings} followings")

    def follow(self, User):
        User.followers += 1
        self.followings += 1
        print(f"{self.name} has started follow {User.name}")


# Doesn't use the new keyword like in other programming languages
user_1 = User("001", "Ardevi44")
user_2 = User("002", "Angela")

user_1.follow(user_2)
user_1.show_followers_and_followings()
