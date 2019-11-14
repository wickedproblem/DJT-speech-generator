from bs4 import BeautifulSoup
import urllib3
import os


def return_links(url):

  """
  Input: url to Factbase overview page. Example: 'https://factba.se/transcripts/speeches'
  Returns: Dictionary containing speech titles and links for each speeches in the overview page.
  """

  http = urllib3.PoolManager()
  response = http.request('GET', url)
  soup = BeautifulSoup(response.data, features='html.parser')

  # Find elements that contain the data we want.
  found = soup.find_all('h3')
  
  # Extract data from the found elements and store in a dictionary
  data = {}
  i = 0
  for elem in found:
    # https://stackoverflow.com/questions/41745514/getting-the-href-of-a-tag-which-is-in-li
    data[i] = [i, elem.a.text, elem.a.get('href')]
    i += 1

  return data

def return_links_local(url):

  """
  Input: Link to local html page.
  Returns: Dictionary containing speech titles and links for each speeches in the overview page.
  """

  soup = BeautifulSoup(open(url), features='html.parser')

  # Find elements that contain the data we want.
  found = soup.find_all('h3')
  
  # Extract data from the found elements and store in a dictionary
  data = {}
  i = 0
  for elem in found:
    # https://stackoverflow.com/questions/41745514/getting-the-href-of-a-tag-which-is-in-li
    data[i] = [i, elem.a.text, elem.a.get('href')]
    i += 1
  return data

def write_transcript(speech_title, url):

  """
  Writes text transcript in a file using the data from given url.
  speech_title: Used to create a txt file of that name
  url: Input url where speech transcript is stored.
  Return: None
  """

  http = urllib3.PoolManager()
  response = http.request('GET', url)
  soup = BeautifulSoup(response.data, features='html.parser')

  # The text is stored in class ranscript-text-block. There are muliple text blocks, separated by timestamp.
  all_texts = soup.findAll("div", {"class": "transcript-text-block"})

  # Open a txt file to store the transcript.
  filename = speech_title + '.txt'
  filepath = os.path.join('./data/transcripts', filename)
  f = open(filepath, "a")
  
  for text in all_texts:
    f.write(text.text)
    f.write('\n')
  
  print('Finished writing file.')