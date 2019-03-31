import requests
import json
import sys
import random
import config as c


def find(key, dictionary):
  for k, v in dictionary.items():
    if k == key:
      yield v
    elif isinstance(v, dict):
      for result in find(key, v):
        yield result
    elif isinstance(v, list):
      for d in v:
        if isinstance(d, dict):
          for result in find(key, d):
            yield result


def get_random_word():
  data = request('wordlist/en/registers=Rare')
  # 5000 results are returned by the request
  r = random.randint(0, 5001)
  return data['results'][r]['id']


def get_definitions(word_id):
  data = request('entries/en/' + word_id)
  definitions = [x[0] for x in list(find('definitions', data))]
  return definitions


def request(data_type):
  url = 'https://od-api.oxforddictionaries.com:443/api/v1/' + data_type
  r = requests.get(url, headers={'app_id': c.app_id, 'app_key': c.app_key})

  if(int(r.status_code) != 200):
    print('Downloading data from API failed, exiting')
    exit()

  return r.json()


def display_results(word, definitions):
  print(word)
  for definition in definitions:
    print('> {}'.format(definition))


def main():
  language = 'en'
  try:
    word_id = sys.argv[1].lower()
  except IndexError:
    word_id = get_random_word()

  definitions = get_definitions(word_id)
  display_results(word_id, definitions)


if __name__ == '__main__':
  main()
