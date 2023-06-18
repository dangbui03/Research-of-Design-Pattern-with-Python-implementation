import abc

class MediaPlayer(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """
    @abc.abstractmethod
    def play(self, audio_type, file_name):
        pass

class AdvancedMediaPlayer(metaclass=abc.ABCMeta):
    """
    Define an existing interface that needs adapting.
    """
    @abc.abstractmethod
    def play_vlc(self, file_name):
        pass

    @abc.abstractmethod
    def play_mp4(self, file_name):
        pass

class VLCPlayer(AdvancedMediaPlayer):
    """
    Lớp VLCPlayer triển khai Interface AdvancedMediaPlayer để phát các file âm thanh định dạng VLC.
    """
    def play_vlc(self, file_name):
        print("Playing VLC file:", file_name)

    def play_mp4(self, file_name):
        pass

class MP4Player(AdvancedMediaPlayer):
    """
    Lớp MP4Player triển khai Interface AdvancedMediaPlayer để phát các file âm thanh định dạng MP4.
    """
    def play_vlc(self, file_name):
        pass

    def play_mp4(self, file_name):
        print("Playing MP4 file:", file_name)

class MediaAdapter(MediaPlayer):
    """
    Lớp MediaAdapter triển khai Interface MediaPlayer và sử dụng Composition để chuyển đổi giao diện MediaPlayer sang AdvancedMediaPlayer.
    """
    def __init__(self, audio_type):
        if audio_type == "vlc":
            self.advanced_player = VLCPlayer()
        elif audio_type == "mp4":
            self.advanced_player = MP4Player()

    def play(self, audio_type, file_name):
        if audio_type == "vlc":
            self.advanced_player.play_vlc(file_name)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(file_name)

class AudioPlayer(MediaPlayer):
    """
    Lớp AudioPlayer triển khai Interface MediaPlayer để phát các file âm thanh. Nếu định dạng file không được hỗ trợ, nó sẽ sử dụng MediaAdapter để chuyển đổi và phát các file âm thanh.
    """
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print("Playing MP3 file:", file_name)
        elif audio_type == "vlc" or audio_type == "mp4":
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)
        else:
            print("Unsupported audio format.")

def main():
    audio_player = AudioPlayer()

    audio_player.play("mp3", "song.mp3")
    audio_player.play("vlc", "movie.vlc")
    audio_player.play("mp4", "video.mp4")
    audio_player.play("avi", "video.avi")

if __name__ == "__main__":
    main()