from plyer import notification
import requests


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:/Users/lenovo/Desktop/python file/first fro ai nad others/icon.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    notifyme("Alan", " lest stop saprate of the corona .corona is sapteating very hingh amount in the world wide wed . that's way to stop the sprationof corona we have help . ")
    myhtmldata = getData('https://www.mohfw.gov.in/')

    print(myhtmldata)
