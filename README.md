# Recurrent Neural Network on the Yale Daily News Opinion Section

## Scraping the YDN website
`YDN_article_read.py`: scrapes the Yale Daily News website for op-eds dating back 10 years. This provides a dataset of about 5 million words.

## Training a word-rnn on the data
I used [word-rnn-tensorflow](https://github.com/hunkim/word-rnn-tensorflow) for this part of the project.

## Results
The generated text is pretty garbled. It was a stretch in the first place to think that the word-rnn can learn to mimic the style of the YDN in ~10 hours of training. Here are some of my favorite lines:

>When I first got to Yale, sans high school potheads and Superman and charm, I found myself weeping.

>The right to marry is the scourge of stigmatization for a vulgarity perpetuated by a madman who has been tortured [] with the self-betterment or sex-betterment quest.

>It is time for us to rediscover the [] time and effort to befriend the flavors of integration.

>Lin-Manuel Miranda is a Socratic hero who has the right to marry whomever he termed a “racist mob” (although it is official: Saint attacks are cruel.)

>There is a lot to say about the sexualization of the Iraqi people.

>Our president, unfortunately, is not a “product of our keyboard”.

>It is not far-fetched to think that Kiko Milano and eight-dollar sandwiches are mildly superficial.

>New Yorkers have been detained in the War on Cancer.

>According to Judith Butler, the only thing redeeming the divide between athletes and “non-athletes” at Yale is “a quiet, white man with a warm bag of fear.”

>None of these “Asian values” in the dairy industry are trampling freedom of expression.

>It is official: the problem is not ours.

>Conservatives turned a “blind eye to the corruption” and the intrauterine device (IUD), [] a lightning rod for a peaceful inter-religious bomb on the Dakota Access Pipeline.
