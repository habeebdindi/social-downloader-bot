#Helper module for main.py

def check_link(link: str, platform: str) -> bool:
    return (platform in link)

def is_tweet(link: str) -> bool:
    old_domain = check_link(link, 'twitter.com')
    new_domain = check_link(link, 'x.com')
    return old_domain or new_domain

def is_ig(link: str) -> bool:
    return check_link(link, 'instagram.com')

def is_tiktok(link: str) -> bool:
    return check_link(link, 'tiktok.com')
