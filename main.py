import requests
from wox import Wox

icons_dir = './icons/'
class Main(Wox):
    def request(self, url):
        if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
            proxies = {
                "http": "http://{}:{}".format(self.proxy.get("server"), self.proxy.get("port")),
                "https": "http://{}:{}".format(self.proxy.get("server"), self.proxy.get("port"))}
            return requests.get(url, proxies=proxies)
        else:
            return requests.get(url)

    def query(self, query):
        results = []
        url = "https://api.chucknorris.io/jokes/random"
        r = requests.get(url).json()
        results.append({
            "Title": r["value"],
            "SubTitle": "",
            "IcoPath": icons_dir + "chucknorris.png",
        })
        if not results:
            results.append({
                "Title": 'No suggestions',
                "SubTitle": '',
                "IcoPath": icons_dir + "chucknorris.png"
            })
        return results

if __name__ == "__main__":
    Main()
