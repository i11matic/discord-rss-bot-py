import feedparser


class RssReader(object):
    def __init__(self, rss_feed, max_content_length=2000):
        self.rss_feed = rss_feed
        self.parsed_feed = feedparser.parse(rss_feed)
        self.max_content_length = max_content_length
        self.torrent_dict = {}
        self.__make_torrent_dict()

    def __make_torrent_dict(self):
        if 'entries' in self.parsed_feed:
            torrent_list = self.parsed_feed['entries']
            for entry in torrent_list:
                if 'title' in entry and 'link' in entry:
                    self.torrent_dict[entry['title']] = entry['link']

    def get_rss_info(self):
        if 'feed' in self.parsed_feed:
            return self.parsed_feed['feed']

    def get_torrents(self, torrent_list: dict, items=10):
        count = 0
        torrent_dict = {}
        for torrent in self.torrent_dict:
            if count < items:
                torrent_dict[torrent] = self.torrent_dict[torrent]
                count += 1
        return torrent_dict

    def check_content_length(self, torrents):
        if len(torrents) <= self.max_content_length:
            return True
        return False
