# Russo Ukrainian War Collection of Tweet IDs
 
The repository contains an ongoing collection of tweets IDs associated with the current war between Russia and Ukraine, which we commenced collecting on Februrary 24, 2022. We leveraged Twitter's search API to extract historical tweets, leading our dataset to contain tweets from February 22, 2022. We utilize Twitter’s streaming API to collect dataset based on selected popular hashtags corelated to particullar topic. The list of selected hashtags is presented in "hashtags.txt" file. To comply with Twitter’s [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy), we are only publicly releasing the Tweet IDs of the collected Tweets. The data is released for non-commercial research use. 

The associated paper to this repository can be found here: [TODO: Paper title](TODO: Paper URL)



## Data Organization
The Tweet-IDs are organized as follows:
* Tweet-ID files are stored in folders that indicate the year and month of the collection (YEAR-MONTH). 
* Individual Tweet-ID files contain a collection of Tweet IDs, and the file names all follow the same structure, with a prefix “tweet_ids_day_” followed by the YEAR_MONTH_DATE. 
* Note that Twitter returns Tweets in UTC, and thus all Tweet ID folders and file names are all in UTC as well. 


## Data Statistics and Analysis
We are manage to perform multiple statistical measurments in daily basis over the described dataset such as:
* User Activity (Traffic volume)
* Active users
* Volume of suspended and deactivated accounts
* Traffic volume based on text language
* Traffic of hashtags
* Sentiment analysis between entities of Russia and Ukraine
* Sentiment analysis between entities of Putin and Zelensky

All described analytics are published in [Parasecurity Group webpage](https://alexdrk14.github.io/RussiaUkraineWar/). 

## How to Hydrate

### Hydrating using [Hydrator](https://github.com/DocNow/hydrator) (GUI)
Navigate to the [Hydrator github repository](https://github.com/DocNow/hydrator) and follow the instructions for installation in their README. As there are a lot of separate Tweet ID files in this repository, it might be advisable to first merge files from timeframes of interest into a larger file before hydrating the Tweets through the GUI. 

### Hydrating using [Twarc](https://github.com/DocNow/twarc) (CLI)
Many thanks to Ed Summers ([edsu](https://github.com/edsu)) for writing this script that uses [Twarc](https://github.com/DocNow/twarc) to hydrate all Tweet-IDs stored in their corresponding folders. 

First install Twarc and tqdm
```
pip3 install twarc
pip3 install tqdm
```

Configure Twarc with your Twitter API tokens (note you must [apply](https://developer.twitter.com/en/apply-for-access) for a Twitter developer account first in order to obtain the needed tokens). You can also configure the API tokens in the script, if unable to configure through CLI. 
```
twarc configure
```

Run the script. The hydrated Tweets will be stored in the same folder as the Tweet-ID file, and is saved as a compressed jsonl file
```
python3 hydrate.py
```

# Data Usage Agreement / How to Cite
By using this dataset, you agree to abide by the stipulations in the license, remain in compliance with Twitter’s [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy), and cite the following manuscript: 

Authors and Paper title with arxiv_id
BibTeX:
```bibtex
@misc{TODO}
```


# Statistics Summary (v1.0)
Number of Tweets : **57,759,943**


# Inquiries

Please read through the README and the closed issues to see if your question has already been addressed first. 

If you have any  questions about this dataset/analysis, please contact Alexander Shevtsov at **shevtsov[at]ics[dot]forth[dot]gr**.

