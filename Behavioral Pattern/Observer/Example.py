import abc

class YouTubeChannel:
    """
    The Subject class representing a YouTube channel.
    """
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(self.channel_name, video_title)


class Subscriber:
    """
    The Observer class representing a subscriber to a YouTube channel.
    """
    def __init__(self, name):
        self.name = name

    def update(self, channel_name, video_title):
        print(f"{self.name} received a new video '{video_title}' from {channel_name}.")


def main():
    channel = YouTubeChannel("MyAwesomeChannel")

    subscriber1 = Subscriber("John")
    subscriber2 = Subscriber("Alice")

    channel.subscribe(subscriber1)
    channel.subscribe(subscriber2)

    channel.notify_subscribers("New Video: Introduction to Python")

    channel.unsubscribe(subscriber2)

    channel.notify_subscribers("New Video: Advanced Machine Learning")


if __name__ == "__main__":
    main()
