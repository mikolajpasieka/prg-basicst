class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f" {self.username} {self.post.sort()} ")


def main():
    user = SocialMediaProfile()
    user.username = 'johndoe'
    user.username = [ "Hello, world!",
    ,"Had a great day at the park!"
    "What's up, Natalie? How are you?"]


if __name__ =="__main__":
    main()