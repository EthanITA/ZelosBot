from zelos_api import ZelosApi


class CreateBot(ZelosApi):
    def __init__(self, invite_link):
        self.invite_link = invite_link
