import requests
import allure


@allure.feature("管理员权限")
class TestAdmin:


    def get_admin_token(self, api_url):

        data = {
            "username": "admin",
            "password": "123456"
        }


        response = requests.post(
            api_url + "/login",
            json=data
        )


        return response.json()["access_token"]



    @allure.title("管理员查询用户列表")
    def test_get_users(self, api_url):


        token = self.get_admin_token(api_url)


        headers = {
            "Authorization": f"Bearer {token}"
        }


        response = requests.get(
            api_url + "/admin/users",
            headers=headers
        )


        assert response.status_code == 200

        assert isinstance(
            response.json(),
            list
        )



    @allure.title("管理员冻结用户")
    def test_disable_user(self, api_url):


        token = self.get_admin_token(api_url)


        headers = {
            "Authorization": f"Bearer {token}"
        }


        user_id = 2


        response = requests.put(
            api_url + f"/admin/users/{user_id}/disable",
            headers=headers
        )


        assert response.status_code == 200


        assert response.json()["msg"] == "账号已冻结"



    @allure.title("管理员恢复用户")
    def test_enable_user(self, api_url):


        token = self.get_admin_token(api_url)


        headers = {
            "Authorization": f"Bearer {token}"
        }


        user_id = 2


        response = requests.put(
            api_url + f"/admin/users/{user_id}/enable",
            headers=headers
        )


        assert response.status_code == 200


        assert response.json()["msg"] == "账号已恢复"