import requests

class ZelosApi:

    def login(self, email, password):
        url = r'https://api.zelos.gg/api/v3/user/login'

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/login',
            'DNT': '1',
            'Authorization': 'Bearer null',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 '
                          'Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        data = '{"email":"' + email + '","password":"' + password + '","desktop":null}'

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()

    def get_referrals(self, token):
        ref_api_url = r'https://api.zelos.gg/api/v3/user/referrals'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/referral',
            'DNT': '1',
            'Authorization': token}
        referrals = requests.get(ref_api_url, headers=headers)
        if referrals.status_code == 200:
            return referrals.json()

    def add_bearer(self, token):
        return "Bearer " + token

    def poll(self, token):
        poll_api = "https://beta-backend-poll-server.onrender.com/api/v3/poll"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/challenges',
            'DNT': '1',
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 '
                          'Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        data = '{"game":"league"}'
        print("Updating missions...")
        requests.post(poll_api, headers=headers, data=data)
        print("Missions updated!")

    def fetch_achievements(self, token):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/challenges',
            'DNT': '1',
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        }

        response = requests.get('https://api.zelos.gg/api/v3/achievement?game=league', headers=headers)
        if response.status_code == 200:
            return response.json()

    def fetch_missions(self, token):
        get_missions_api = "https://api.zelos.gg/api/v3/mission?game=league"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/challenges',
            'DNT': '1',
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 '
                          'Safari/537.36',
        }
        response = requests.get(get_missions_api, headers=headers)
        if response.status_code == 200:
            return response.json()

    def claim_mission(self, token, mission_id):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/challenges',
            'DNT': '1',
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 '
                          'Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        data = '{"mission":' + str(mission_id) + '}'

        response = requests.post('https://api.zelos.gg/api/v3/mission/claim', headers=headers, data=data)

        if response.status_code == 200:
            return response.json()

    def claim_achievement(self, token, achievements_id):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://zelos.gg/challenges',
            'DNT': '1',
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        data = '{"achievement":' + str(achievements_id) + '}'

        response = requests.post('https://api.zelos.gg/api/v3/achievement/claim', headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
