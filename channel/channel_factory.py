"""
channel factory
"""
from .channel import Channel


def create_channel(channel_type) -> Channel:
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    if channel_type == "wework":
        from channel.wework.wework_channel import WeworkChannel
        ch = WeworkChannel()
    else:
        raise RuntimeError(f"Unsupported channel type: {channel_type}")
    ch.channel_type = channel_type
    return ch
