import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # ydl.download(['https://tele5.de/mediathek/the-humanity-bureau-flucht-aus-new-america/'])
    ydl.download(['https://pluto.tv/de/on-demand/series/mad-about-you-de/season/1/episode/der-anfang-vom-ende-1991-1-1'])