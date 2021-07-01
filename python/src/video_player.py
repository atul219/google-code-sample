"""A video player class."""

from src.video_playlist import Playlist
from .video_library import VideoLibrary
import random
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

        self.video_playing = False
        self.video_name = None
        self.video_paused = False

        self.playlist_dict = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        # for val in all_videos:
        #     print(val.tags)
        video_list = []
        for vid in all_videos:

            tags = "["

            for tag in vid.tags:
                tags += tag + " "
            tags += "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            video_list += [f"{vid.title} ({vid.video_id}) {tags}"]
        
        
        sort_list = sorted(video_list)
        for i in sort_list:
            print(i)

        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_ids = []
        for i in self._video_library.get_all_videos():
            video_ids.append(i.video_id)

        video = self._video_library.get_video(video_id)
        if video_id in video_ids:
            if self.video_playing == False and self.video_paused == False: 
                self.video_name = video
                print(f" Playing video: {video.title}")
                self.video_playing = True
                self.video_paused == False

            elif self.video_paused == True:
                print(f"Stopping video: {self.video_name.title}")
                print(f"Playing video: {video.title}")
                self.video_playing = False
                self.video_name = video
                self.video_paused = True
                
            else:
                print(f"Stopping video: {self.video_name.title}")
                print(f"Playing video: {video.title}")
                self.video_playing = True
                self.video_name = video
            
        else:
            print(f"Cannot play video: Video does not exist")

      

    def stop_video(self):
        """Stops the current video."""
        
        if self.video_playing == True:
            # print(f"Playing video: {self.video_name}")
            print(f"Stopping video: {self.video_name.title}")
            self.video_playing = False
       
        else:
            print(f"Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        all_ids = self._video_library.get_all_videos()
        if self.video_playing == True:
            print(f"Stopping video: {self.video_name.title}")
            self.video_playing = False
        
       
        
        rand_id = random.choice(all_ids)
        print(f"Playing video: {rand_id.title}")
        self.video_name = rand_id
        self.video_playing = True
        

    def pause_video(self):
        """Pauses the current video."""
        if self.video_playing == True:
            print(f"Pausing video: {self.video_name.title}")
            self.video_paused = True
            self.video_playing = False
        
        elif self.video_paused == True:
            print(f"Video already paused: {self.video_name.title}")
            
        else:
            print(f"Cannot pause video: No video is currently playing")
        
        

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_paused == False:        
            if self.video_playing == False:
                print(f"Cannot continue video: No video is currently playing")
                self.video_playing = False
            else:
                print(f"Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self.video_name.title}")
            self.video_paused = False
            self.video_playing = True

    def show_playing(self):
        """Displays video currently playing."""

        
        if self.video_playing == True:
            all_videos = self._video_library.get_all_videos()
            video_list = []
            for vid in all_videos:
                if self.video_name.title == vid.title:
                    tags = "["
                    for tag in vid.tags:
                        tags += tag + " "
                    tags += "]"

                    if tags != "[]":
                        tags = tags[0:len(tags)-2] + "]"

                    video_list += [f"{vid.title} ({vid.video_id}) {tags}"]

            print(f"Currently playing: {video_list[0]}")
            
        elif self.video_paused == True:
            tags = "["
            for tag in self.video_name.tags:
                tags += tag + " "
            tags += "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"
            print(f"Currently playing: {self.video_name.title} ({self.video_name.video_id}) {tags} - PAUSED")



        else:
            print(f"No video is currently playing")
        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        

        if playlist_name.lower() not in (name.lower() for name in  self.playlist_dict.keys()):
            pl = Playlist(playlist_name)
            self.playlist_dict[playlist_name] = pl
            print(f"Successfully created new playlist: {pl._name}")
        else:
            print(f"Cannot create playlist: A playlist with the same name already exists")


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_old = playlist_name

        if playlist_name.lower() not in (name.lower() for name in  self.playlist_dict.keys()):
            print("Cannot add video to" , playlist_name + ": " + "Playlist does not exist")
        else:
            for key in self.playlist_dict.keys():
                if key.lower() == playlist_name.lower():
                    playlist_name = key
                
            video_list = self.playlist_dict[playlist_name]._videos

            try:
                video_name = self._video_library.get_video(video_id).title
            except:
                video_name = ""
            
            if not video_name:
                print("Cannot add video to" , playlist_name + ": " + "Video does not exist")
            elif video_id in video_list:
                print("Cannot add video to" , playlist_name + ": " + "Video already added")
            else:
                video_list.append(video_id)
                obj = self.playlist_dict[playlist_name]
                obj.x(video_list)
                self.playlist_dict[playlist_name] = obj
                print("Added video to" , playlist_old + ":", video_name)


    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlist_dict:
            print(f"Showing all playlists:")
            for key in self.playlist_dict.keys():
                # print(self.playlist_dict[key]._videos)
                print(self.playlist_dict[key].)
            
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_old = playlist_name
        if playlist_name.lower() not in (name.lower() for name in  self.playlist_dict.keys()):
            print("Cannot remove video from" , playlist_name + ": " + "Playlist does not exist")
        
        else:
            for key in self.playlist_dict.keys():
                if key.lower() == playlist_name.lower():
                    playlist_name = key
                
            obj = self.playlist_dict[playlist_name]
            video_list = obj._videos
            try:
                video_name = self._video_library.get_video(video_id).title
            except:
                video_name = ""
            
            if video_id in video_list:
                video_list.remove(video_id)
                obj.x(video_list)
                print(f"Removed video from {playlist_old}: {video_name}")
            else:
                if not video_name:
                    print(f"Cannot remove video from {playlist_old}: Video does not exist")
                else:
                    print(f"Cannot remove video from {playlist_old}: Video is not in playlist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
