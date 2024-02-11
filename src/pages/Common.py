SCREENSHOT_PATH = "screenshots/"
WEBSHOP_URL = "https://qa-task-fe.vercel.app/"
RESET_PASSWORD_URL = "https://qa-task-fe.vercel.app/resetpasword"
LOGIN_URL = "https://qa-task-fe.vercel.app/login"
REGISTER_URL = "https://qa-task-fe.vercel.app/register"

# Define the devices and their viewport sizes
DEVICES = {
    'desktop': {'width': 1920, 'height': 1080,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'},
    'mobile': {'width': 375, 'height': 667,
               'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1'},
    'tablet': {'width': 768, 'height': 1024,
               'user_agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1'},
}


def get_devices():
    return DEVICES


def get_scrn_name(test_id):
    dir = test_id.split("_")[1]
    print(dir)
    if dir == 'login':
        path = SCREENSHOT_PATH + 'login/' + test_id + '.png'
    elif dir == 'registration':
        path = SCREENSHOT_PATH + 'registration/' + test_id + '.png'
    elif dir == 'reset':
        path = SCREENSHOT_PATH + 'reset_password/' + test_id + '.png'
    else:
        raise TypeError("Wrong value!")
    return path


def get_webshop_link():
    return WEBSHOP_URL


def get_reset_password_link():
    return RESET_PASSWORD_URL


def get_register_url():
    return REGISTER_URL


def get_login_url():
    return LOGIN_URL