from bot.zelos_api import *


class RedeemBot:

    def __init__(self):
        """
        It will be asked to give credentials to login in Zelos. Credentials will ONLY be used for getting your Bearer
        token (which is a code that identifies your account), and the token will ONLY be used for redeeming missions!
        """
        print("Email: ", end="")
        self.email = input()
        print("Password: ", end="")
        self.password = input()
        self.auth_token = add_bearer(login(self.email, self.password)["token"])
        print("Logged with token: " + self.auth_token)

    def ref_redeem(self, account_to_redeem=5):
        for ref in get_referrals(self.auth_token):
            if not ref["claimed"]:
                print("User: " + ref["username"])
                response_login = login(email=ref["username"], password=ref["username"])
                if response_login is not None:
                    logged_token = add_bearer(response_login["token"])
                    print("Logged with token: " + logged_token)
                    poll(logged_token)
                    claim_all_missions(logged_token)
                    claim_all_achievements(logged_token)
                    account_to_redeem -= 1
                    print("--------------------------------")
            if account_to_redeem <= 0:
                break

    def redeem_account(self):
        poll(self.auth_token)
        claim_all_missions(self.auth_token)
        claim_all_achievements(self.auth_token)


def claim_all_achievements(token):
    redeemed = False
    for achievement in fetch_achievements(token)["achievements"]:
        if achievement["claim_id"] is not None:
            redeemed = True
            print("Achievement: " + achievement["description"], end="")
            print(" => Redeemed") if claim_achievement(token, achievement["id"]) is not None else print(
                " => Couldn't redeem")

    print("All achievements are redeemed!") if redeemed else print("No achievemets could be redeemed")


def claim_all_missions(token):
    redeemed = False
    for mission in fetch_missions(token)["missions"]:
        if mission["claim_id"] is not None:
            redeemed = True
            print("Mission: " + mission["name"], end="")
            print(" => Redeemed") if claim_mission(token, mission["id"]) is not None else print(
                " => Couldn't redeem")
    print("All missions are redeemed!") if redeemed else print("No missions could be redeemed")


if __name__ == '__main__':
    bot = RedeemBot()
    bot.redeem_account()
    print(
        "------------------------------------------------------------------------------------------------------------")
    bot.ref_redeem(5)
