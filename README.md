# DJT political rally speech generator using Open AI's GPT-2. 

### Getting data

I wanted to get text transcripts of Donald Trump's all political rallies since his announcement of candicacy in 2016. 
[Factbase](https://factba.se/transcripts) has them all, but it doesn't provide an API to get the transcript text. 
I put together a simple script to get the transcript texts. 

Note the [homepage](https://factba.se/transcripts) is infinite scrolling. 
You have to either use selenium or [scrapy](https://scrapy.org/) to automate the scrolling AJAX call. Since I was doing it once,
I just scrolled manually for a few min, saved the resulting HTML file and used that to scrape the address of each individual speech
transcript link. The function is `return_links_local(local_url_link)`

```
links = return_links_local(local_url_file)
```

links is a dictionary. 

I have also provided function to scrape links from the homepage, and it returns 20 links (first page). It's `return_links(url)`.

Once the links are received, all you have to do is call `write_transcript` to save transcript the text. Note in the website the transcript text
is separate by time. 

```
write_transcript(speech_name,speech_url)
```

### GPT-2 finetuning and model deployment in Google Cloud has been discussed in my other [repo](https://github.com/addadda023/GPT-2-text-generation)

Try the app [here.](https://addadda023.github.io/DJT-speech-generator/)
