from utils import return_links, write_transcript, return_links_local
import os

"""
This code scrapes factbase website to get speech transcripts.
-> return_links method: Takes aggregate page and returns address of all the speeches in the page. Example input: 'https://factba.se/transcripts/speeches'
-> return_links_local method: Same as return_links, but takes a local html file as input. I had to do this because Factbase page is infinitely scrolling, so I manually scrolled up to the data I wanted and stored the html in a local file.
-> write_transcript metod: Writes to a file the text transcript in the given url like. Example url input: 'https://factba.se/transcript/donald-trump-speech-economic-club-of-new-york-city-november-12-2019'
"""

"""
# Run this code if you want to scrape from Factbase webpage.
# Factbase page for DT's speeches
url = 'https://factba.se/transcripts/speeches'

# Call return_links to get links for all speeches in a dictionary.
# Key: Speech #
# Value: [Speech #, Speech Title, Speech URL]
data = return_links(url)
"""

# I took the local html file as input.
local_url_file = os.path.join('./data/html', 'FACTBASE.html')
data = return_links_local(local_url_file)

# Print Speech titles and corresponding urls.
# I am interested only in Political Rally
count_rally = 0
for key, val in data.items():
  
  if 'Speech: Donald Trump Holds a Political Rally' in val[1]:
    # Look for Political Rally speeches.
    print('Found Political Rally transcript. Writing speech: ', val[1])
    # Future Enhancement: Parallel writing of files
    write_transcript(val[1],val[2])
    count_rally += 1

print(count_rally)