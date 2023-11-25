from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
    cfg = yaml.safe_load(f)

def check_word(word):
    settings = Settings(strict = False)
    client = Client(wsdl=cfg['soap_url'], settings=settings)
    # print(client.service.checkText(word))
    return client.service.checkText(word)[0]['s']