from bot.zelos_api import *


class CreateBot:
    def __init__(self, invite_link):
        """
        CreateBot will automatically create lot of accounts on Zelos using you referral
        :param invite_link: Your referral link
        """
        self.invite_link = invite_link
