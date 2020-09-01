from zelos_api import ZelosApi


class RedeemBot(ZelosApi):

    def __init__(self):
        print("Email: ", end="")
        self.email = input()
        print("Password: ", end="")
        self.password = input()
        self.auth_token = self.add_bearer(self.login(self.email, self.password)["token"])
        print("Logged with token: " + self.auth_token)

    def claim_all_achievements(self, token):
        redeemed = False
        for achievement in self.fetch_achievements(token)["achievements"]:
            if achievement["claim_id"] is not None:
                redeemed = True
                print("Achievement: " + achievement["description"], end="")
                print(" => Redeemed") if self.claim_achievement(token, achievement["id"]) is not None else print(
                    " => Couldn't redeem")

        print("All achievements are redeemed!") if redeemed else print("No achievemets could be redeemed")

    def claim_all_missions(self, token):
        redeemed = False
        for mission in self.fetch_missions(token)["missions"]:
            if mission["claim_id"] is not None:
                redeemed = True
                print("Mission: " + mission["name"], end="")
                print(" => Redeemed") if self.claim_mission(token, mission["id"]) is not None else print(
                    " => Couldn't redeem")
        print("All missions are redeemed!") if redeemed else print("No missions could be redeemed")

    def ref_redeem(self, account_to_redeem=5):
        for ref in self.get_referrals(self.auth_token):
            if not ref["claimed"]:
                print("User: " + ref["username"])
                response_login = self.login(email=ref["username"], password=ref["username"])
                if response_login is not None:
                    logged_token = self.add_bearer(response_login["token"])
                    print("Logged with token: " + logged_token)
                    self.poll(logged_token)
                    self.claim_all_missions(logged_token)
                    self.claim_all_achievements(logged_token)
                    account_to_redeem -= 1
                    print("--------------------------------")
            if account_to_redeem <= 0:
                break

    def redeem_account(self):
        self.poll(self.auth_token)
        self.claim_all_missions(self.auth_token)
        self.claim_all_achievements(self.auth_token)


if __name__ == '__main__':
    bot = RedeemBot()
    bot.redeem_account()
    print(
        "------------------------------------------------------------------------------------------------------------")
    bot.ref_redeem(5)
